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

  get proceedToCheckout() {
    return cy.get('a[title="Proceed to checkout"]');
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

  clickProceedToCheckout() {
    this.proceedToCheckout.click();
  }
}

export default new Product();
