/// <reference types="cypress" />
import Base from "../pages/Base";
import Search from "../pages/Search";
import Home from "../pages/Home";
import Women from "../pages/Women";
import Product from "../pages/Product";
import { productAddedOk } from "../fixtures/cartData.json";

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
    // cy.get('span[title="Close window"]').should("be.visible");
    cy.get(".layer_cart_product > h2").should("contain.text", productAddedOk);
    Product.clickCloseWindow();
    Product.clickCartBtn();

    cy.get("#cart_summary").should("be.visible");
  });
});

//span[class="button ajax_add_to_cart_button btn btn-default disabled"
