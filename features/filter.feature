Feature: Filter Product

  Scenario: Filter laptops and write product names to Excel
    Given I open the Amazon homepage
    When I search for "Laptops"
    And I filter the results by brand, price range, CPU, processor count, OS, and item condition
    Then I should write the product names to an Excel file
