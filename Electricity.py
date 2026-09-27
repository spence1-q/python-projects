#  Define a function named calculate_bill() that accepts units consumed and cost per unit
def calculate_bill(units_consumed, cost_per_unit):
    # Calculate the bill
    bill = units_consumed * cost_per_unit
    
    # Return the calculated bill
    return bill

def main():
    print("--- Electricity Bill Calculator ---")
    
    # user to enter the units consumed and cost per unit
    # Using float to handle both whole numbers and decimals
    units = float(input("Enter the units consumed (kWh): "))
    cost = float(input("Enter the cost per unit ($): "))
    
    # Call the calculate_bill() function
    total_bill = calculate_bill(units, cost)
    
    # Display the calculated electricity bill
    print("\n=================================")
    print("        BILL SUMMARY")
    print("=================================")
    print(f"Units Consumed:    {units:,.2f} kWh")
    print(f"Cost Per Unit:     ${cost:,.2f}")
    print("---------------------------------")
    print(f"Total Electricity Bill: ${total_bill:,.2f}")
    print("=================================")

# Execute the program
if __name__ == "__main__":
    main()
