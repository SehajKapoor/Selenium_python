Feature: Navigate Product

  Scenario: Navigate product catalogue and reviews page
    Given I open the Amazon homepage
    When I search for "Nokia c22"
    Then I should print product catalogue images and 3-star reviews to a text file
