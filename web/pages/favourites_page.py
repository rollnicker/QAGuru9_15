from selene import browser, have


class FavouritesPage:
    def __init__(self):
        self.title = browser.element('.cmn__title')
        self.item_info_name = browser.element('.basket-item-info-name')

    def check_title_name(self):
        self.title.should(have.title('Избранное'))

    def check_model_name_in_favourites(self, name):
        self.item_info_name.should(have.text(name))
