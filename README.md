# Selenium Web Tests - TU Berlin

Este projeto contém testes automatizados com Selenium + pytest feitos no site da universidade [Technische Universität Berlin](https://www.tu.berlin/en/).

## Como executar

Antes de rodar, é necessário ter o **Python 3** e o **Google Chrome** instalados.

### 1. Criar ambiente virtual

- Windows

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

- Linux/MacOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Rodar os testes

- Todos os testes

```bash
pytest tests/ -v
```

- Testes mais visuais, usando @pytest.mark.visual

```bash
pytest -m visual -v
```

## Itens cobertos

| #   | Item                                    | Arquivo            | Seletor                                      | Teste                                               |
| --- | --------------------------------------- | ------------------ | -------------------------------------------- | --------------------------------------------------- |
| 1   | Título principal da página              | `test_homepage.py` | `CSS_SELECTOR` `main h1`                     | `test_deve_abrir_site_tu_berlin`                    |
| 2   | Logo do cabeçalho                       | `test_homepage.py` | `CLASS_NAME` `logo`                          | `test_logo_esta_presente`                           |
| 3   | Menu principal                          | `test_homepage.py` | `CSS_SELECTOR` `.navigation__item--level1`   | `test_menu_principal_tem_links`                     |
| 4   | Seletor de idioma EN/DE                 | `test_homepage.py` | `CSS_SELECTOR` `.languageMenu`               | `test_troca_idioma_para_alemao`                     |
| 5   | Dropdown Online-Services                | `test_homepage.py` | `ID` `servicesMenu__label`                   | `test_dropdown_servicos_online_tem_opcoes`          |
| 6   | Dropdown Faculties / Central Institutes | `test_homepage.py` | `ID` `facultyMenu__label` / `XPATH`          | `test_dropdown_faculdades_abre_e_navega`            |
| 7   | Botão hambúrguer                        | `test_homepage.py` | `ID` `menu-burger-button`                    | `test_botao_hamburguer_existe`                      |
| 8   | Link Easy Read                          | `test_homepage.py` | `CLASS_NAME` `accessibilityLink`             | `test_link_easy_read_acessibilidade`                |
| 9   | Slider principal                        | `test_homepage.py` | `CSS_SELECTOR` `.js-slider-main`             | `test_slider_principal_avanca`                      |
| 10  | Navegação do slider                     | `test_homepage.py` | `CSS_SELECTOR` `.js-slider-nav`              | `test_navegacao_do_slider_tem_itens`                |
| 11  | Lista de notícias                       | `test_homepage.py` | `CSS_SELECTOR` `.news_list-item`             | `test_lista_de_noticias_tem_cards`                  |
| 12  | Teaser do Newsroom                      | `test_homepage.py` | `XPATH` por texto                            | `test_teaser_newsroom_tem_link_explore`             |
| 13  | Lista de eventos                        | `test_homepage.py` | `CSS_SELECTOR` `.event__teaserbox` / `XPATH` | `test_evento_possui_dia_e_mes`                      |
| 14  | Botão show all dos eventos              | `test_homepage.py` | `CSS_SELECTOR` `.event .show-more a`         | `test_botao_ver_todos_eventos_tem_link`             |
| 15  | Teaser International Affairs            | `test_homepage.py` | `XPATH` por texto / `CSS_SELECTOR`           | `test_teaser_international_affairs_tem_link`        |
| 16  | Teaser Knowledge Exchange               | `test_homepage.py` | `XPATH` por texto / `CSS_SELECTOR`           | `test_teaser_knowledge_exchange_tem_link`           |
| 17  | Redes sociais do rodapé                 | `test_homepage.py` | `CSS_SELECTOR` `.footer__socialMedia a`      | `test_redes_sociais_no_rodape`                      |
| 18  | Menu meta do rodapé                     | `test_homepage.py` | `CSS_SELECTOR` `.footer__metaMenu a`         | `test_menu_meta_do_rodape_tem_links_institucionais` |
| 19  | Campo de busca                          | `test_search.py`   | `NAME` `tx_solr[q]`                          | `test_campo_de_busca_esta_presente`                 |
| 20  | Botão da lupa                           | `test_search.py`   | `CSS_SELECTOR` `.search__button`             | `test_botao_lupa_dispara_busca`                     |

## Seletores usados

- `ID`: itens 5, 6, 7
- `NAME`: item 19
- `CLASS_NAME`: itens 2, 8
- `CSS_SELECTOR`: itens 1, 3, 4, 5, 9, 10, 11, 14, 17, 18, 20
- `XPATH`: itens 6, 12, 13, 15, 16
