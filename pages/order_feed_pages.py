import allure
import helper
from curls import Curls
from locators.main_page_locators import MainPageLocator
from pages.base_pages import BasePage
from locators.order_feed_page_locators import OrderFeedLocator

class OrderFeedPage(BasePage):
    @allure.step('Переход на страницу "Лента заказов"')
    def going_in_feed_order(self):
        self.going_url(Curls.FEED_URL)

    @allure.step('Подождать появления номера заказа в разделе "В работе"')
    def wait_order_in_work(self):
        return self.wait_change_element(OrderFeedLocator.ORDER_IN_WORK_1, 'Все текущие заказы готовы!')

    @allure.step('Получить количества заказов за все время')
    def get_count_orders(self, locator):
        count_orders = self.wait_for_element(locator)
        return count_orders.text

    @allure.step('Получение списка заказов из раздела "В работе"')
    def get_id_order_in_work(self):
        elements = self.wait_load_all_elements(OrderFeedLocator.ORDER_IN_WORK)
        orders_in_work = [element.text for element in elements]
        return orders_in_work
    