class Cart {
  get deleteProduct() {
    return cy.get(".icon-trash");
  }

  get increaseQuantityBtn() {
    return cy.get(".icon-plus");
  }

  get productPrice() {
    return cy.get(".cart_unit li.price");
  }

  get totalPrice() {
    return cy.get("#total_price");
  }

  get productQuantity() {
    return cy.get(".cart_quantity_input");
  }

  clickDeleteProduct() {
    this.deleteProduct.click();
  }

  clickIncreaseQuantityBtn() {
    this.increaseQuantityBtn.click();
  }

  getProductPrice() {
    return this.productPrice.invoke("text");
  }

  getTotalPrice() {
    return this.totalPrice.invoke("text");
  }

  getProductQuantity() {
    return this.productQuantity.invoke("val");
  }
}

export default new Cart();
