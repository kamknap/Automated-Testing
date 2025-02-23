/// <reference types="cypress" />

describe("First automated test", function () {
  it("Open website", function () {
    cy.visit("/");
    cy.get("#search_query_top").type("Tresc {enter}");
  });
});
