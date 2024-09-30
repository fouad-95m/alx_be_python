FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        user_input = input("Enter a temperature followed by its unit (C for Celsius, F for Fahrenheit) or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            value, unit = user_input[:-1], user_input[-1].upper()
            temperature = float(value)  # Convert value to float
            
            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp:.2f}°F.")
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp:.2f}°C.")
            else:
                print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
                
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
