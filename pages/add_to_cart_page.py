from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage


class AddToCartPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_RESULT = (By.XPATH, "(//span[@data-component-type='s-product-image'])[1]/a")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    ADD_TO_CART_MESSAGE = (By.XPATH, "//div[@id='attachDisplayAddBaseAlert']")

    def visit_url(self, url):
        self.visit(url)

    def search_with_keyword(self, keyword):
        self.fill_input(self.SEARCH_INPUT, keyword) \
            .click_element(self.SEARCH_BUTTON)

    def click_search_result(self):
        self.click_element(self.SEARCH_RESULT)

    def click_add_to_cart_button(self):
        self.switch_to_window(2) \
            .click_element(self.ADD_TO_CART_BUTTON)

    def verify_add_to_cart_message(self):
        self.verify_element_displayed(self.ADD_TO_CART_MESSAGE)
