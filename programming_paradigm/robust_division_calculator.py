def safe_divide(numerator, denominator):
    """Perform division with error handling for non-numeric inputs and division by zero."""
    try:
        # Convert both inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error:
