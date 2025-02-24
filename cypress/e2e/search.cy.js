/// <reference types="cypress" />
import Base from "../pages/Base";
import Search from "../pages/Search";
import {
  searchPhrase,
  notFoundProduct,
  unaviableSearchPhrase,
} from "../fixtures/searchData.json";

describe("Search input related tests", function () {
  it("Search aviable product and open its page", function () {
    Base.openHomePage();
    Search.typeSearchInput(searchPhrase + "{enter}");
    Search.searchInput.should("have.value", "Printed Dress");
    Search.clickFirstItem(
      ".first-in-line.first-item-of-tablet-line > .product-container > .right-block > h5 > .product-name"
    );
    cy.get(".primary_block").should("be.visible");
  });
  it("Search unaviable product", function () {
    Base.openHomePage();
    Search.typeSearchInput(unaviableSearchPhrase + "{enter}");
    Search.searchInput.should("have.value", unaviableSearchPhrase);
    cy.get(".alert").should("be.visible");
  });
  it("Search available products and check if each contains search phrase", function () {
    Base.openHomePage();
    Search.typeSearchInput(searchPhrase + "{enter}");
    Search.searchInput.should("have.value", searchPhrase);
    cy.get("#center_column").each(($el) => {
      cy.wrap($el).should("contain.text", searchPhrase);
    });
  });
});
