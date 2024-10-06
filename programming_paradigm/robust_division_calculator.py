def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denom = float(denominator)
         denominator = numerator / denominator
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error:
