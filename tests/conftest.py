import pytest
from selenium import webdriver
from curls import Curls
import data

from locators.login_page_locator import LoginPageLocator
from locators.main_page_locators import MainPageLocator
from pages.base_pages import BasePage


@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    """Фикстура для запуска браузеров Chrome и Firefox по очереди"""
    driver = None
    try:
        if request.param == "Chrome":
            driver = webdriver.Chrome()
        elif request.param == "Firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Неизвестный браузер: {request.param}")
        driver.maximize_window()
        driver.get(Curls.MAIN_URL)
        yield driver
    finally:
        if driver is not None:
            driver.quit()
            
@pytest.fixture()
def login_driver(driver):
    login_driver = BasePage(driver)
    login_driver.going_url(Curls.LOGIN_URL)
    login_driver.wait_hide_element(MainPageLocator.OVERLAY)
    login_driver.send_text_to_input(LoginPageLocator.FIELD_EMAIL, data.Authorization.EMAIL)
    login_driver.send_text_to_input(LoginPageLocator.FIELD_PASSWORD, data.Authorization.PASSWORD)
    login_driver.click_on_element(LoginPageLocator.BUT_LOGIN)
    login_driver.wait_for_element(MainPageLocator.TEXT_COLLECT_BURGER)
    return driver