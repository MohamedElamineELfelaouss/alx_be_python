# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction
def main():
    # Prompt the user to enter a temperature
    temperature_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature_input)
    except ValueError:
        # If the user entered a wrong input, raise an error
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Prompt the user to specify the unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'C':
        # Call the appropriate conversion function
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        # Call the appropriate conversion function
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
