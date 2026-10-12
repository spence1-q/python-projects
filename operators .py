# Initialize an empty list to store the names
names = []

print("Enter names one by one (type 'done' when finished):")

# Prompt the user to enter names and append them to the list
while True:
    user_input = input("Enter a name: ")
    if user_input.lower() == 'done' or user_input == "":
        break
    names.append(user_input)

# Count the total number of names entered before removing duplicates
total_count = len(names)

# Remove duplicates using set(), then convert back to a list and sort alphabetically
unique_sorted_names = sorted(list(set(names)))

# Display the total count and the final sorted list
print("\n--- Results ---")
print(f"Total number of names entered: {total_count}")
print("Final sorted list (duplicates removed):", unique_sorted_names)
