Feature:  Verify APIs and workflow for Login function


Scenario: Successful request for Login
    When I send "POST" request to endpoint "/api/Account/login"
    Then The status code should be "201"
    And The POST response body should contain correct information

