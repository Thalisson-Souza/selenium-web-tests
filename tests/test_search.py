from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSearch():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tu.berlin/en/")

    def teardown_method(self):
        self.driver.quit()

    def test_campo_de_busca_esta_presente(self):
        campo_de_busca = self.driver.find_element(By.NAME, "rx_solr[q]")

        assert campo_de_busca.is_displayed()
