import allure

from web.application import app


@allure.title('Проверка работы добавления в избранное')
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
