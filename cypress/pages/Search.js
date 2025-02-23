class Search {
  get searchInput() {
    return cy.get("#search_query_top");
  }

  typeSearchInput(text) {
    this.searchInput.type(text);
  }

  clearSearchInput() {
    this.searchInput.clear();
  }

  clickItem(item) {
    cy.get(item).first().click();
  }
}

export default new Search();
