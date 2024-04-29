try:
    # Code block where exceptions may occur
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code block to handle the specific exception
    print("Error: Division by zero occurred!")
