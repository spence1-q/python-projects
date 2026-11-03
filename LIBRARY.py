# i & ii. Define the Book class with a constructor to initialize title, author, price, and copies
class Book:
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    # iii. Method to calculate and return the total value of available copies
    def calculate_stock_value(self):
        return self.price * self.copies

    # iv. Method to check whether a book is in stock or out of stock
    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"

    # Helper method to display book details, stock value, and availability status
    def display_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price:,.2f}")
        print(f"Copies Available: {self.copies}")
        print(f"Stock Value: {self.calculate_stock_value():,.2f}")
        print(f"Status: {self.check_stock()}")
        print("-" * 35)


# v. Create two objects of the Book class with the specified sample data and display information
if __name__ == "__main__":
    # Book 1: Python Basics
    book1 = Book(title="Python Basics", author="Gloria Kamau", price=1200, copies=5)
    
    # Book 2: Database Systems
    book2 = Book(title="Database Systems", author="Monica Mueni", price=2500, copies=0)

    print("=== Library Book Management System Records ===")
    print()
    
    # Display details, stock value, and availability status for Book 1
    print("Book 1 Details:")
    book1.display_book_info()

    # Display details, stock value, and availability status for Book 2
    print("Book 2 Details:")
    book2.display_book_info()
