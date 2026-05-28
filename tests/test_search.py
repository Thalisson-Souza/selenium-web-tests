import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.tu.berlin/en/"


class TestSearch:
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

    def test_campo_de_busca_esta_presente(self):
        campo = self.driver.find_element(By.NAME, "tx_solr[q]")
        assert campo.is_displayed()

    @pytest.mark.visual
    def test_botao_lupa_dispara_busca(self):
        campo = self.driver.find_element(By.NAME, "tx_solr[q]")
        self.destacar(campo)
        campo.send_keys("research")
        botao = self.driver.find_element(By.CSS_SELECTOR, ".search__button")
        self.destacar(botao)
        botao.click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/search"))
        assert "research" in self.driver.current_url.lower()
