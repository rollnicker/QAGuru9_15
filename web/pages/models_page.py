from selene import browser, have, be


class ModelChoosePage:
    def __init__(self):
        self.product = browser.all('.product-card')
        self.add_button = browser.element('.product-card__add')

    def add_to_cart(self, item):
        self.product.element_by(have.text(item)).element('.product-card__add').should(be.clickable).click()

    def open_product(self, name):
        self.product.element_by(have.text(name)).click()
