# Task 1: Calculate Factorial


# Function to calculate factorial
def factorial(n):
    result = 1

    # loop to calculate factorial
    for i in range(1, n + 1):
        result = result * i
    return result


if __name__ == "__main__":
    try:
        # take input
        num = int(input("Enter a number: "))

        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            # call function
            fact = factorial(num)

            # print  result
            print(f"Factorial of {num} is: {fact}")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
