import pytest
from pytest_bdd import scenario, when, then, given, parsers

from pages.add_to_cart_page import AddToCartPage
from globals import GlobalVars as glob


@pytest.mark.addtocart
@scenario('../feature/add_to_cart.feature', 'Validate add to cart feature')
def test_add_to_cart_feature():
    pass


@given('url is loaded')
def step_impl(request):
    AddToCartPage().visit_url(request.session.url)


@when(parsers.parse('user attempts search with {keyword}'))
def step_impl(keyword):
    glob.keyword = keyword
    AddToCartPage().search_with_keyword(glob.keyword)


@when("user clicks on the search result")
def step_impl():
    AddToCartPage().click_search_result()


@when("user clicks on add to cart button")
def step_impl():
    AddToCartPage().click_add_to_cart_button()


@then("verify the search result is shown")
def step_impl():
    AddToCartPage().verify_add_to_cart_message()
