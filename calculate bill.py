
def calculate_bill(units):
    """Calculates electricity charge using tiered rate slabs."""
    if units < 100:
        charge = units * 15
    elif units <= 300:
        charge = (100 * 15) + ((units - 100) * 20)
    else:
        charge = (100 * 15) + (200 * 20) + ((units - 300) * 25)
    return charge



if __name__ == "__main__":
    #  Prompt user for number of electricity units consumed
    units = float(input("Enter the number of electricity units consumed: "))

    # Call the function calculate_bill(units)
    electricity_charge = calculate_bill(units)

    # Calculate total bill by adding fixed service charge of KSh 100
    service_charge = 100
    total_bill = electricity_charge + service_charge

    # Display the required details
    print("\n--- Electricity Bill Summary ---")
    print(f"Units Consumed:     {units}")
    print(f"Electricity Charge: KSh {electricity_charge:.2f}")
    print(f"Total Bill Payable: KSh {total_bill:.2f}")
