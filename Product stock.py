class Product:
    def __init__(self):
        self.product_name = ""
        self.product_code = ""
        self.price = 0.0
        self.quantity = 0

    def setProductDetails(self, name, code, price, quantity):
        self.product_name = name
        self.product_code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        return self.price * self.quantity

    def displayProductDetails(self):
        stock_value = self.calculateStockValue()
        print("\n--- Product Details ---")
        print(f"Product Name : {self.product_name}")
        print(f"Product Code : {self.product_code}")
        print(f"Price        : KSh {self.price:,.2f}")
        print(f"Quantity     : {self.quantity}")
        print(f"Stock Value  : KSh {stock_value:,.2f}")

# Main 
if __name__ == "__main__":
    # Create a Product object
    product = Product()
    
    # Set the product details
    product.setProductDetails("Fifa 22 Cd", "F22-500", 3500.0, 15)
    
    # Calculate the stock value and display the product details
    product.displayProductDetails()
