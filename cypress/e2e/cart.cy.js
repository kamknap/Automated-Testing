/// <reference types="cypress" />
import Base from "../pages/Base";
import Home from "../pages/Home";
import Women from "../pages/Women";
import Product from "../pages/Product";
import Cart from "../pages/Cart";
import Results from "../pages/Results";
import { productAddedOk, emptyCart } from "../fixtures/cartData.json";

describe("Cart related tests", function () {
  it("Add product to cart", function () {
    Base.openHomePage();
    Home.clickWomenTab();
    Women.clickSecondItem();
    cy.wait(2000);
    Product.clickWhiteColor();
    cy.wait(2000);
    Product.clickAddToCartBtn();
    cy.wait(2000);
    // Verify if product added information appears
    cy.get(".layer_cart_product > h2").should("contain.text", productAddedOk);
    Product.clickCloseWindow();
    Home.clickCartBtn();
    // Verify if product is in cart
    cy.get("#cart_summary").should("be.visible");
  });

  it("Increase product quantity in cart and verify price change", function () {
    Base.openHomePage();
    Home.clickWomenTab();
    Women.clickSecondItem();
    cy.wait(2000);
    Product.clickWhiteColor();
    cy.wait(2000);
    Product.clickAddToCartBtn();
    cy.wait(2000);
    // Verify if product added information appears
    cy.get(".layer_cart_product > h2").should("contain.text", productAddedOk);
    Product.clickCloseWindow();
    Home.clickCartBtn();
    // Verify if product is in cart
    cy.get("#cart_summary").should("be.visible");

    // Get initial product price and quantity
    Cart.getProductPrice().then((initialProductPrice) => {
      Cart.getProductQuantity().then((initialQuantity) => {
        const initialTotalPrice =
          parseFloat(initialProductPrice.replace("$", "")) *
          parseInt(initialQuantity);

        // Increase product quantity
        Cart.clickIncreaseQuantityBtn();
        cy.wait(2000);

        // Get new product quantity and total price
        Cart.getProductQuantity().then((newQuantity) => {
          Cart.getTotalPrice().then((newTotalPrice) => {
            const expectedTotalPrice =
              parseFloat(initialProductPrice.replace("$", "")) *
                parseInt(newQuantity) +
              7;
            expect(parseFloat(newTotalPrice.replace("$", ""))).to.equal(
              expectedTotalPrice
            );
          });
        });
      });
    });
  });

  it("Delete product from cart", function () {
    Base.openHomePage();
    Home.clickCartBtn();
    Cart.clickDeleteProduct();
    Results.resultAlert.should("contain.text", emptyCart);
  });
});
