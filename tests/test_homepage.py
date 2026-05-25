from selenium import webdriver
from selenium.webdriver.common.by import By

def test_deve_abrir_site_tu_berlin():
    driver = webdriver.Chrome()

    driver.get("https://www.tu.berlin/en/")

    assert "Technische Universität Berlin" in driver.title

    driver.quit()


def test_logo_esta_presente():
    driver = webdriver.Chrome()
    driver.get("https://www.tu.berlin/en/")

    logo = driver.find_element(By.CLASS_NAME, "logo")
    assert logo.is_displayed()

    driver.quit()