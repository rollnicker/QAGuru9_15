from selene import browser, be, have


class ItemPage:
    def __init__(self):
        self.add_button = browser.element('.product-item__add')
        self.add_to_fav_button = browser.element('.purchase__header-menu button')
        self.title = browser.element('cmn__title')

    def add_item_to_cart(self):
        self.add_button.should(be.visible).click()

    def add_item_to_favourites(self):
        self.add_to_fav_button.should(be.visible).click()

    def check_itme_name(self, name):
        self.title.should(have.text(name))
