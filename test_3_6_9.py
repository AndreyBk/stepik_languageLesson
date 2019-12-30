import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])

def test_aliens(browser,link):
    browser.get(link)
    button = WebDriverWait(browser, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-lg")))
    assert (button.text=="Añadir al carrito")
