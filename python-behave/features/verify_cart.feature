Feature: Verify the functionality of the shopping cart

    Scenario: Add a product to the cart
        Given The user see a list of products
        When The user adds a product to the shopping cart
        Then The product appears in the shopping cart

    Scenario: Remove a product from the cart
        Given The user has a product added to the shopping cart
        When The user removes a product from the cart
        Then The products disappears from the shopping cart