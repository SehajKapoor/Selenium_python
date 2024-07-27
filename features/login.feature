Feature: Amazon Login

  Scenario Outline: Login with valid and invalid credentials
    Given I open the Amazon homepage
    When I enter username "<username>" and password "<password>"
    Then I should see the homepage if credentials are "<validity>"

    Examples:
      | username         | password      | validity |
      | valid_user       | valid_pass    | valid    |
      | invalid_user     | invalid_pass  | invalid  |
