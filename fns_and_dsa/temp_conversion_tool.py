 Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_temperature_input():
    """Get temperature input from the user."""
    while True:
        user_input = input("Enter a temperature to convert (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            return None, None  # Signal to exit
        try:
            temperature = float(user_input)
            return temperature, input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def main():
    while True:
        temperature, unit = get_temperature_input()
        if temperature is None:  # Exit condition
            print("Goodbye!")
            break
        
        if unit not in ('C', 'F'):
            print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
            continue
        
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F.")
        else:  # unit == 'F'
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C.")

if __name__ == "__main__":
    main()
