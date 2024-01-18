from selene import browser, have, be


class BasketPage:
    def __init__(self):
        self.item_name = browser.all('.basket-item-info-name')
        self.add_button = browser.element('.product-card__add')
        self.delete_all_button = browser.element('.delete_all')
        self.removed_item_notification = browser.element('.basket-items-list-item-removed-container')
        self.empty_basket_notification = browser.element('.bx-sbb-empty-cart-text')

    def should_have_name(self, item):
        self.item_name[0].should(have.text(item))

    def remove_all_items(self):
        self.delete_all_button.click()

    def should_have_removed_item_notification(self, text):
        self.removed_item_notification.should(have.text(text))

    def should_have_empty_basket(self):
        self.empty_basket_notification.should(be.visible)
