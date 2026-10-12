# Create a tuple named customer containing customer details
customer = ("Obed Jones", "CID-5049", "+254712345678", "obed.jones@gmail.com")

# Display the complete tuple
print("Complete Customer Tuple:", customer)

# Access and display the customer's name and telephone number using their indexes[cite: 2]
print("Customer Name (index 0):", customer[0])
print("Telephone Number (index 2):", customer[2])

# Display the number of items in the tuple using len()[cite: 2]
print("Number of items in tuple:", len(customer))

# Attempt to modify the customer's telephone number[cite: 2]
print("\nAttempting to modify the telephone number...")
try:
    customer[2] = "+254798765432"
except TypeError as e:
    print("TypeError caught:", e)
