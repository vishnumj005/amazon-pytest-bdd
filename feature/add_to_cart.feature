@feature_add_to_cart
Feature: Verify add to cart functionality of amazon website

  @sc_add_to_cart
  Scenario Outline: Validate add to cart feature
    Given url is loaded
    When user attempts search with <keyword>
    And user clicks on the search result
    And user clicks on add to cart button
    Then verify the search result is shown
    Examples:
    |keyword |
    |mobile  |
