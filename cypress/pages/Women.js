class Woman {
  get secondItem() {
    return cy.get(
      ":nth-child(2) > .product-container > .right-block > h5 > .product-name"
    );
  }

  clickSecondItem() {
    this.secondItem.click();
  }
}

export default new Woman();
