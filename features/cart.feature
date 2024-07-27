Feature: Cart Operations

  Scenario: Add items to cart and proceed to checkout
    Given I open the Amazon homepage
    When I search for "Nokia c22" and add it to the cart
    And I search for "keyboard wireless" and add "Dell USB Wireless Keyboard" to the cart
    Then I should validate the cart and proceed to checkout
