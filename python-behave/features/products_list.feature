Feature: Product list
    Scenario: Check if products appears after login
        When Login form appears
        And Enter username "standard_user", password "secret_sauce"
        And Click Login button
        Then User is being logged in and products list appears