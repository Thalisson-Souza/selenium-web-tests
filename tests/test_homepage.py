from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHomepage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tu.berlin/en/")

    def teardown_method(self):
        self.driver.quit()

    def test_deve_abrir_site_tu_berlin(self):
        assert "Technische Universität Berlin" in self.driver.title

    def test_logo_esta_presente(self):
        logo = self.driver.find_element(By.CLASS_NAME, "logo")
        
        assert logo.is_displayed()
