Feature: Search Product
  Scenario: Print search results to a text file
    Given I open the Amazon homepage
    When I search for "iPhone 15"
    Then I should print the search results with 4+ ratings to a text file
