Feature: Contact form
    Scenario: Check if contact form is working properly
        Given launch browser
        When contact form page opens
        And enter username "user", password "pass123", text in textarea "test text 123", click Checkbox1 and Checkbox2, unclick Checkbox3 
        And click the "Submit" button
        Then user is directed to new page and displayed information equals written by user