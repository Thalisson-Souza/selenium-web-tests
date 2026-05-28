import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.tu.berlin/en/"


class TestHomepage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def teardown_method(self):
        self.driver.quit()

    def destacar(self, elemento):
        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({block: 'center'});
            arguments[0].style.border = '4px solid red';
            arguments[0].style.backgroundColor = 'yellow';
            """,
            elemento,
        )
        time.sleep(1)

    def test_deve_abrir_site_tu_berlin(self):
        titulo = self.driver.find_element(By.CSS_SELECTOR, "main h1")
        assert "Technische Universität Berlin" in titulo.text
        assert "Technische Universität Berlin" in self.driver.title

    def test_logo_esta_presente(self):
        logo = self.driver.find_element(By.CLASS_NAME, "logo")
        assert logo.is_displayed()

    def test_menu_principal_tem_links(self):
        links = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".navigation__item--level1 > .navigation__itemLink--level1",
        )
        textos = {link.text.strip().upper() for link in links if link.text.strip()}

        assert len(links) >= 5
        assert {"STUDYING", "RESEARCH", "CAREERS AND JOBS", "ABOUT"}.issubset(textos)

    @pytest.mark.visual
    def test_troca_idioma_para_alemao(self):
        link_de = self.driver.find_element(
            By.CSS_SELECTOR, ".languageMenu a[title='Deutsch']"
        )
        self.destacar(link_de)
        link_de.click()
        WebDriverWait(self.driver, 10).until_not(EC.url_contains("/en/"))
        url = self.driver.current_url
        assert "/en/" not in url
        assert "tu.berlin" in url

    @pytest.mark.visual
    def test_dropdown_servicos_online_tem_opcoes(self):
        label = self.driver.find_element(By.ID, "servicesMenu__label")
        self.destacar(label)
        assert label.text.strip() == "Online-Services"

        lista = self.driver.find_element(By.ID, "servicesMenu__linkList")
        label.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of(lista))
        self.destacar(lista)

        links = lista.find_elements(By.CSS_SELECTOR, "li a")
        textos = [link.text.strip() for link in links]
        assert textos == ["TU Portal", "Webmail", "Intranet"]
        assert all(link.get_attribute("href").startswith("http") for link in links)

    @pytest.mark.visual
    def test_dropdown_faculdades_abre_e_navega(self):
        label = self.driver.find_element(By.ID, "facultyMenu__label")
        self.destacar(label)
        assert label.text.strip() == "Faculties / Central Institutes"

        lista = self.driver.find_element(By.ID, "facultyMenu__linkList")
        itens = lista.find_elements(By.CSS_SELECTOR, "li a")
        assert len(itens) == 7

        label.click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of(lista))
        self.destacar(lista)

        faculdade_eecs = lista.find_element(
            By.XPATH,
            ".//a[contains(., 'Electrical Engineering and Computer Science')]",
        )
        self.destacar(faculdade_eecs)
        faculdade_eecs.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/en/eecs"))
        assert "/en/eecs" in self.driver.current_url

    def test_botao_hamburguer_existe(self):
        burger = self.driver.find_element(By.ID, "menu-burger-button")
        assert burger.get_attribute("aria-label") == "Menu"
        assert burger.get_attribute("aria-controls") == "menu-wrapper"
        assert burger.get_attribute("aria-expanded") == "false"

    def test_link_easy_read_acessibilidade(self):
        wrapper = self.driver.find_element(By.CLASS_NAME, "accessibilityLink")
        link = wrapper.find_element(By.CSS_SELECTOR, "a.js-metaEasyLanguageLink")

        href = link.get_attribute("href") or ""
        texto = link.get_attribute("textContent") or ""

        assert "accessibility/easy-read-version" in href
        assert "Easy Read" in texto

    @pytest.mark.visual
    def test_slider_principal_avanca(self):
        slider = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-slider-main"))
        )
        self.destacar(slider)
        slides = slider.find_elements(By.CSS_SELECTOR, ".swiper-slide")
        assert len(slides) > 1

        ativo_antes = slider.find_element(
            By.CSS_SELECTOR, ".swiper-slide-active"
        ).get_attribute("data-swiper-slide-index")

        botao_next = slider.find_element(By.CSS_SELECTOR, ".swiper-button-next")
        self.destacar(botao_next)
        self.driver.execute_script("arguments[0].click();", botao_next)

        WebDriverWait(self.driver, 5).until(
            lambda d: slider.find_element(
                By.CSS_SELECTOR, ".swiper-slide-active"
            ).get_attribute("data-swiper-slide-index")
            != ativo_antes
        )

    def test_navegacao_do_slider_tem_itens(self):
        nav = self.driver.find_element(By.CSS_SELECTOR, ".js-slider-nav")
        itens = nav.find_elements(By.CSS_SELECTOR, ".slider__item")

        assert len(itens) >= 3
        assert itens[0].get_attribute("data-index") == "0"

    def test_lista_de_noticias_tem_cards(self):
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".news_list-item")
        assert len(cards) >= 1

    def test_teaser_newsroom_tem_link_explore(self):
        teaser = self.driver.find_element(
            By.XPATH,
            "//article[contains(@class, 'teaser')]"
            "[.//h3[contains(., 'The Newsroom')]]",
        )
        link = teaser.find_element(By.CSS_SELECTOR, "a.teaser__link")

        assert "Explore" in link.text
        assert link.get_attribute("href").endswith("/en/news")

    def test_evento_possui_dia_e_mes(self):
        evento = self.driver.find_element(By.CSS_SELECTOR, ".event__teaserbox")
        dia = evento.find_element(
            By.XPATH, ".//*[contains(@class,'event__listItemDate--day')]"
        )
        mes = evento.find_element(
            By.XPATH, ".//*[contains(@class,'event__listItemDate--month')]"
        )
        assert dia.text.strip().isdigit()
        assert mes.text.strip() != ""

    def test_botao_ver_todos_eventos_tem_link(self):
        botao = self.driver.find_element(By.CSS_SELECTOR, ".event .show-more a")

        assert botao.text.strip() == "show all"
        assert botao.get_attribute("href").endswith("/en/events")

    def test_teaser_international_affairs_tem_link(self):
        teaser = self.driver.find_element(
            By.XPATH,
            "//article[contains(@class, 'teaser')]"
            "[.//h3[normalize-space()='International Affairs']]",
        )
        link = teaser.find_element(By.CSS_SELECTOR, "a[title='International Affairs']")
        imagem = teaser.find_element(By.CSS_SELECTOR, "img[alt='Globe']")

        assert link.get_attribute("href").endswith("/en/topics/international-affairs")
        assert imagem.get_attribute("src").startswith("http")

    def test_teaser_knowledge_exchange_tem_link(self):
        teaser = self.driver.find_element(
            By.XPATH,
            "//article[contains(@class, 'teaser')]"
            "[.//h3[normalize-space()='Knowledge Exchange']]",
        )
        link = teaser.find_element(By.CSS_SELECTOR, "a[title='Knowledge Exchange']")
        imagem = teaser.find_element(By.CSS_SELECTOR, "img[alt='Graphic recording']")

        assert link.get_attribute("href").endswith("/en/topics/knowledge-exchange")
        assert imagem.get_attribute("src").startswith("http")

    @pytest.mark.visual
    def test_redes_sociais_no_rodape(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        redes_sociais = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".footer__socialMedia"))
        )
        self.destacar(redes_sociais)
        links = self.driver.find_elements(By.CSS_SELECTOR, ".footer__socialMedia a")

        assert len(links) >= 4

        titulos = {link.get_attribute("title") for link in links}
        assert {"Instagram", "YouTube", "LinkedIn"}.issubset(titulos)

        for link in links:
            href = link.get_attribute("href") or ""
            assert href.startswith("http")
            assert link.get_attribute("target") == "_blank"

    def test_menu_meta_do_rodape_tem_links_institucionais(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        links = self.driver.find_elements(By.CSS_SELECTOR, ".footer__metaMenu a")
        textos = {link.text.strip().upper() for link in links}

        assert len(links) >= 5
        assert {"CONTACT", "SITE CREDITS", "DATA PROTECTION"}.issubset(textos)
        assert all(link.get_attribute("href").startswith("http") for link in links)
