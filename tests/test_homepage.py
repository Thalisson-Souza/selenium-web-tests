from selenium import webdriver

def test_deve_abrir_site_tu_berlin():
    driver = webdriver.Chrome()

    driver.get("https://www.tu.berlin/en/")

    assert "Technische Universität Berlin" in driver.title

    driver.quit()