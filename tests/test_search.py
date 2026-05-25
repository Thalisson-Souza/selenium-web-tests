from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSearch:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tu.berlin/en/")

    def teardown_method(self):
        self.driver.quit()

    def test_campo_de_busca_esta_presente(self):
        campo_de_busca = self.driver.find_element(By.NAME, "tx_solr[q]")

        assert campo_de_busca.is_displayed()

    def test_deve_permitir_digitar_no_campo_de_busca(self):
        campo_de_busca = self.driver.find_element(By.NAME, "tx_solr[q]")

        campo_de_busca.send_keys("computer science")
        assert campo_de_busca.get_attribute("value") == "computer science"

    def test_deve_realizar_busca(self):
        campo = self.driver.find_element(By.NAME, "tx_solr[q]")
        campo.send_keys("computer science")
        campo.submit()
        
        assert "/en/search" in self.driver.current_url