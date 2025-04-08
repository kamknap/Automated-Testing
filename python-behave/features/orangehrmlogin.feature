Feature: OrangeHRM Login

    Scenario: Login to OrangeHRM with valid parameters
        Given Launch chrome browser
        When Open OrangeHRM homepage
        And Enter username Admin and password admin123
        And Click the Login button
        Then User successfully login to dashboard page

    Scenario Outline: Login to OrangeHRM with multiple parameters
        Given Launch chrome browser
        When Open OrangeHRM homepage
        And Enter username "<username>" and password "<password>"
        And Click the Login button
        Then User successfully login to dashboard page
    
    Examples:
        | username  | password   |
        | Admin     | admin123   |
        | Admin123  | admin123   |
        | Adminxyz  | admin      |
        | Admin     | adminxyz   |
