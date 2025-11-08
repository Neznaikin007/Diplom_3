from selenium.webdriver.common.by import By

class MainPageLocator:
    OVERLAY = (By.XPATH, '//div[@class="Modal_modal__P3_V5"]/div[@class="Modal_modal_overlay__x2ZCr"]')
    TEXT_COLLECT_BURGER = (By.XPATH, '//h1[contains(text(), "Соберите бургер")]')
    TEXT_FEED_ORDER = (By.XPATH, '//h1[contains(text(), "Лента заказов")]')
    BUT_CONSTRUCTOR = (By.XPATH, '//a[@href="/"]/descendant::p[contains(text(), "Конструктор")]')
    BUT_FEED_ORDER = (By.XPATH, '//a[@href="/feed"]')
    HEAD_INGREDIENT_DETAIL = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    BUT_CROSS = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BURGER_CONSTRUCTOR = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket__list__l9dp_")]')
    BUT_CREATE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')
    INGREDIENT_LOCATOR = {'buns': [['bun_1', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')],
                                   ['bun_2', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')]],

                          'souses': [['souses_1', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')],
                                     ['souses_2', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]')]],

                          'toppings': [['topping_1', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')],
                                       ['topping_2', (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]')]]
                          }
    