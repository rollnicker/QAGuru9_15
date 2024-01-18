from selene import browser, be

from web.components.header_panel import HeaderPanel, CatalogMenu
from web.pages.basket_page import BasketPage
from web.pages.favourites_page import FavouritesPage
from web.pages.item_page import ItemPage
from web.pages.models_page import ModelChoosePage


class Application:

    def __init__(self):
        self.header_panel = HeaderPanel()
        self.catalog_menu = CatalogMenu()
        self.choose_model = ModelChoosePage()
        self.basket = BasketPage()
        self.item_page = ItemPage()
        self.favourites_page = FavouritesPage()

    def open_page(self):
        browser.open('')
        return self

    def close_banner(self):
        if browser.element('.city-ask__wrapper').should(be.visible):
            browser.element('.city-ask__wrapper').element('.close-button').click()
        return self


app = Application()
