from selene import browser, have

from web.pages.basket_page import BasketPage


class HeaderPanel:
    def __init__(self):
        self.catalog = browser.element('.js-open-catalog-menu')
        self.cart = browser.element('.header__cart .cart__wrapper')
        self.search_line = browser.element('#title-search #title-search-input')
        self.search_results = browser.all('.item-text')
        self.choose_city_button = browser.element('.city-info__choose a')
        self.available_cities = browser.all('.js-city-item')
        self.selected_city = browser.element('.city-info__choose')
        self.favourites_button = browser.element('.header__user [href="/favourites/"]')
        self.authorisation_button = browser.element('.avtorization-call')

    def open_catalog(self):
        self.catalog.click()

    def open_cart(self):
        self.cart.click()
        return BasketPage()

    def open_searched_item(self, item):
        self.search_line.click().send_keys(item)
        self.search_results.element_by(have.text(item)).click()
        return self

    def open_searched_models(self, item):
        self.search_line.send_keys(item).press_enter()

    def select_city(self, city):
        self.choose_city_button.click()
        self.available_cities.element_by(have.text(city)).click()

    def should_have_selected_city_name(self, city):
        self.selected_city.should(have.text(city))

    def open_favourites(self):
        self.favourites_button.click()

    def open_autorisation(self):
        self.authorisation_button.click()

    """
    Не реализовано тестирование авторизации
    нужно выяснить как корректно хранить логин и пароль
    """


class CatalogMenu:
    def __init__(self):
        self.category = browser.all('.catalog-menu__item--cathegory')
        self.subcategory = browser.all('.catalog-menu__item--subcathegory')
        self.catalog_product = browser.all('.active>.catalog-menu__product-item')

    def select_category(self, menu_item):
        self.category.element_by(have.text(menu_item)).click()

    def select_subcategory(self, sub_menu_item):
        self.subcategory.element_by(have.text(sub_menu_item)).click()

    def select_product(self, item):
        self.catalog_product.element_by(have.text(item)).click()
