import allure

from web.application import app


class TestBasket:
    @allure.title('Добавление в корзину через каталог')
    def test_add_to_cart_through_catalog(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Выбрать товар из каталога"):
            app.header_panel.open_catalog()
            app.catalog_menu.select_category("Планшеты")
            app.catalog_menu.select_subcategory("Apple")
            app.catalog_menu.select_product('iPad 10 (2022)')
        with allure.step("Добавить товар в корзину"):
            app.choose_model.add_to_cart("Планшет Apple iPad 10.9 (2022) 256GB Wi-Fi Global (Silver)")

        with allure.step("Проверить что выбранный товар присутствует в корзине"):
            app.header_panel.open_cart().should_have_name('Планшет Apple iPad 10.9 (2022) 256GB Wi-Fi Global (Silver)')

    @allure.title('Добавление в корзину через поиск')
    def test_add_to_cart_through_search(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Найти товар в строке поиска"):
            app.header_panel.open_searched_item('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        with allure.step("Добавить товар в корзину"):
            app.item_page.add_item_to_cart()

        with allure.step("Проверить что выбранный товар присутствует в корзине"):
            app.header_panel.open_cart().should_have_name('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')

    @allure.title('Добавление в корзину через открытие каталога в поиске')
    def test_add_to_cart_through_searched_catalog(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Oткрыть странцу магазина"):
            app.header_panel.open_searched_models('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
            app.choose_model.add_to_cart('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')

        with allure.step("Проверить что выбранный товар присутствует в корзине"):
            app.header_panel.open_cart().should_have_name('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')

    @allure.title('Проверка пустой корзины и очистка корзины')
    def test_delete_all_items_from_cart(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Проверить что изначально корзина пустая"):
            app.header_panel.open_cart().should_have_empty_basket()
        with allure.step("Добавить товар в корзину"):
            app.header_panel.open_searched_models('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
            app.choose_model.add_to_cart('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
            app.header_panel.open_cart().should_have_name('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        with allure.step("Удалить из корзины"):
            app.header_panel.open_cart().remove_all_items()

        with allure.step("Проверить что корзина пустая"):
            app.basket.should_have_empty_basket()


class TestFavourites:
    @allure.title('Добавление в избранное')
    def test_add_to_favourites(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Открыть страницу товара"):
            app.header_panel.open_searched_models('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
            app.choose_model.open_product('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')
        with allure.step("Добавить в избранное"):
            app.item_page.add_item_to_favourites()
        with allure.step("Открыть страницу избранное"):
            app.header_panel.open_favourites()

        with allure.step("Проверить что выбранный товар присутствует в избранном"):
            app.favourites_page.check_model_name_in_favourites('Apple iPad 10.9 (2022) 256GB Wi-Fi Global')


class TestOther:
    @allure.title('Тест выбора города')
    def test_city_select(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Oткрыть меню выбора города и выбрать"):
            app.header_panel.select_city('Екатеринбург')

        with allure.step("Проверить что выбранный город отображается"):
            app.header_panel.should_have_selected_city_name('Екатеринбург')
