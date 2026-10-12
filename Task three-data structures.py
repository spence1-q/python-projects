# Create a set named categories, including two duplicate categories
categories = {"Electronics", "Fashion", "Home & Living", "Electronics", "Books", "Beauty", "Fashion"}

# Display the set
print("Initial Categories Set (Duplicates automatically removed):", categories)

# Add a new product category using add()
categories.add("Groceries")

# Remove one category using remove()[cite: 3]
categories.remove("Books")

# Display the final set[cite: 3]
print("Final Categories Set:", categories)
