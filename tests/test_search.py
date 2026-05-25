from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSearch():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tu.berlin/en/")

    def teardown_method(self):
        self.driver.quit()
