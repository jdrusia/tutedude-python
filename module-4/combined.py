# Module 4: Functions & Modules


from task1 import factorial
from task2 import calculate_values


if __name__ == "__main__":

    while True:
        print("\n===== Module 4 Menu =====")
        print("1. Calculate Factorial")
        print("2. Math Calculations (sqrt, log, sine)")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        try:
            if choice == "1" or choice == "2":
                num = int(input("Enter a number: "))
                if num < 0:
                    print(
                        f"{ 'Factorial' if choice == '1' else 'Logarithm' } is not defined for negative numbers."
                    )
                else:

                    if choice == "1":
                        fact = factorial(num)
                        print(f"Factorial of {num} is: {fact}")

                    elif choice == "2":
                        sqrt_val, log_val, sin_val = calculate_values(num)

                        print(f"Square root: {sqrt_val}")
                        print(f"Logarithm: {log_val}")
                        print(f"Sine: {sin_val}")

            elif choice == "3":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Thank you for using the program!")
