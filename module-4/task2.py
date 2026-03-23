# Task 2: Using the Math Module for Calculations

import math  # import math module


# Function to perform calculations
def calculate_values(n):
    square_root = math.sqrt(n)
    log_value = math.log(n)
    sine_value = math.sin(n)

    return square_root, log_value, sine_value


if __name__ == "__main__":
    try:
        # take input
        num = float(input("Enter a number: "))

        if num <= 0:
            print("Logarithm is not defined for zero or negative numbers.")
        else:
            # call function
            sqrt_val, log_val, sin_val = calculate_values(num)

            # print results
            print(f"Square root: {sqrt_val}")
            print(f"Logarithm: {log_val}")
            print(f"Sine: {sin_val}")

    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
