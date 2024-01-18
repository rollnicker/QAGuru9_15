import allure

from web.application import app


class TestBasket():
    @allure.title('Добавление в корзину через каталог')
    def test_add_to_cart_through_catalog(self):
        app.open_page().close_banner()
        app.header_panel.open_catalog()
        app.catalog_menu.select_category("Планшеты")
        app.catalog_menu.select_subcategory("Apple")
        app.catalog_menu.select_product('iPad 10 (2022)')
        app.choose_model.add_to_cart("Планшет Apple iPad 10.9 (2022) 256GB Wi-Fi Global (Silver)")
        app.header_panel.open_cart().should_have_name('Планшет Apple iPad 10.9 (2022) 256GB Wi-Fi Global (Silver)')

    @allure.title('Добавление в корзину через поиск')
    def test_add_to_cart_through_search(self):
        app.open_page().close_banner()
        app.header_panel.open_searched_item('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        app.item_page.add_item_to_cart()
        app.header_panel.open_cart().should_have_name('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')

    @allure.title('Добавление в корзину через открытие каталога в поиске')
    def test_add_to_cart_through_searched_catalog(self):
        app.open_page().close_banner()
        app.header_panel.open_searched_models('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        app.choose_model.add_to_cart('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        app.header_panel.open_cart().should_have_name('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')

    @allure.title('Проверка пустой корзины и очистка корзины')
    def test_delete_all_items_from_cart(self):
        app.open_page().close_banner()
        app.header_panel.open_cart().should_have_empty_basket()
        app.header_panel.open_searched_models('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        app.choose_model.add_to_cart('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        app.header_panel.open_cart().should_have_name('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        app.header_panel.open_cart().remove_all_items()
        app.basket.should_have_empty_basket()


@allure.title('Тест выбора города')
def test_city_select():
    app.open_page().close_banner()
    app.header_panel.select_city('Екатеринбург')
    app.header_panel.should_have_selected_city_name('Екатеринбург')


@allure.title('Добавление в избранное')
def test_add_to_favourites():
    app.open_page().close_banner()
    app.header_panel.open_searched_models('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
    app.choose_model.open_product('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
    app.item_page.add_item_to_favourites()
    app.header_panel.open_favourites()
    app.favourites_page.check_model_name_in_favourites('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
