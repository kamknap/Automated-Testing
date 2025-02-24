class Home {
  get womenTab() {
    return cy.get('a[title="Women"]');
  }

  clickWomenTab() {
    this.womenTab.click();
  }
}

export default new Home();
