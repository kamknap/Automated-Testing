class Product {
  get whiteColor() {
    return cy.get("#color_8");
  }

  get addToCartBtn() {
    return cy.get(".exclusive > span");
  }

  get closeWindow() {
    return cy.get(".cross");
  }

  get cartBtn() {
    return cy.get('[title="View my shopping cart"]');
  }

  clickWhiteColor() {
    this.whiteColor.click();
  }

  clickAddToCartBtn() {
    this.addToCartBtn.click();
  }

  clickCloseWindow() {
    this.closeWindow.click();
  }

  clickCartBtn() {
    this.cartBtn.click();
  }
}

export default new Product();
