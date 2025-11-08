import allure
import pytest
from locators.order_feed_page_locators import OrderFeedLocator
from pages.main_pages import MainPage
from pages.order_feed_pages import OrderFeedPage

class TestOrderFeed:
    @pytest.mark.parametrize('locator, name_test',
                             [(OrderFeedLocator.COUNT_ORDERS_ALL_TIME, 'Тест увеличения счетчика "Выполнено за всё время"'),
                             (OrderFeedLocator.COUNT_ORDERS_TODAY, 'Тест увеличения счетчика "Выполнено за сегодня"')])
    def test_count_orders_in_feed_order_page(self, login_driver, locator, name_test):
        allure.dynamic.title(name_test)
        order_feed_page = OrderFeedPage(login_driver)
        order_feed_page.going_in_feed_order()
        old_value = order_feed_page.get_count_orders(locator)
        main_page = MainPage(login_driver)
        main_page.going_main_page()
        main_page.add_ingredient_in_burger()
        main_page.click_but_create_order()
        main_page.wait_load_order_card()
        order_feed_page.going_in_feed_order()
        new_value = order_feed_page.get_count_orders(locator)
        assert old_value < new_value

    @allure.title('Тест появления номера заказа в разделе "В работе" после оформления заказа')
    def test_display_order_(self, login_driver):
        main_page = MainPage(login_driver)
        main_page.add_ingredient_in_burger()
        main_page.click_but_create_order()
        order_id = main_page.wait_load_order_card()
        order_feed_page = OrderFeedPage(login_driver)
        order_feed_page.going_in_feed_order()
        order_feed_page.wait_order_in_work()
        orders_in_work = order_feed_page.get_id_order_in_work()
        assert order_id in orders_in_work