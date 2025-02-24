class Home {
  get womenTab() {
    return cy.get('a[title="Women"]');
  }

  get cartBtn() {
    return cy.get('[title="View my shopping cart"]');
  }

  clickWomenTab() {
    this.womenTab.click();
  }

  clickCartBtn() {
    this.cartBtn.click();
  }
}

export default new Home();
