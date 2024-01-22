import allure

from web.application import app


@allure.title('Тесты верхней панели магазина')
class TestHeaderPanel:
    @allure.title('Тест выбора города')
    def test_city_select(self):
        with allure.step("Oткрыть странцу магазина"):
            app.open_page().close_banner()

        with allure.step("Oткрыть меню выбора города и выбрать"):
            app.header_panel.select_city('Екатеринбург')

        with allure.step("Проверить что выбранный город отображается"):
            app.header_panel.should_have_selected_city_name('Екатеринбург')
