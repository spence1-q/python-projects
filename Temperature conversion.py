#  Define the function accepting Celsius as a parameter
def convert_temperature(celsius):
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    
    # Return the Fahrenheit value
    return fahrenheit

def main():
    print("--- Weather Application: Temperature Converter ---")
    
    # User to enter the temperature in Celsius
    try:
        celsius_input = float(input("Enter temperature in Celsius: "))
        
        # Call the function
        fahrenheit_output = convert_temperature(celsius_input)
        
        # Display the converted temperature to two decimal places
        print("--------------------------------------------------")
        print(f"Celsius:    {celsius_input:.2f}°C")
        print(f"Fahrenheit: {fahrenheit_output:.2f}°F")
        print("--------------------------------------------------")
        
    except ValueError:
        print("Invalid input. Please enter a valid numerical temperature.")

# Execute the program
if __name__ == "__main__":
    main()
