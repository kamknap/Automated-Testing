# 🤖 Automated Testing (Cypress)
## Description
This repository showcases my automated testing skills using Cypress. The tests are structured following the Page Object Model (POM) and focus on an e-commerce store's functionalities. The tests are divided into two main categories: Search Functionality and Cart Functionality.

## Contents
### [**1. Cart Functionality**](https://github.com/kamknap/Automated-Testing/blob/main/cypress/e2e/cart.cy.js)

- **File:** cart.cy.js

- **Description:** 
This file contains tests related to the cart functionality, including adding a product to the cart, increasing the product quantity, and deleting a product from the cart.

- **Test Cases:**

  - Add product to cart: Verifies if a product can be added to the cart and if the product information appears correctly.
  
  - Increase product quantity in cart and verify price change: Ensures that increasing the product quantity in the cart correctly up
  ates the total price.
  
  - Delete product from cart: Checks if a product can be deleted from the cart and if the cart displays an empty message afterward.

### [**2. Search Functionality**](https://github.com/kamknap/Automated-Testing/blob/main/cypress/e2e/search.cy.js)

- **File:** search.cy.js

- **Description:** This file includes tests related to the search functionality, ensuring that the search input works correctly and handles various search scenarios.

- **Test Cases:**

  - Search available product and open its page: Verifies if a known product can be searched and its page opened.

  - Search unavailable product: Ensures that searching for an unavailable product shows the appropriate message.

  - Search available products and check if each contains the search phrase: Confirms that all search results contain the search phrase.
