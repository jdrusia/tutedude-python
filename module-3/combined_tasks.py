# Module 3: Control Structures in Python


# Function to check whether a number is even or odd
def check_even_odd():
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")


# Function to calculate sum from 1 to 50
def sum_1_to_50():
    total_sum = 0

    for number in range(1, 51):
        total_sum += number

    print(f"The sum of integers from 1 to 50 is: {total_sum}")


print("\n===== Module 3 Menu =====")
print("1. Check if a Number is Even or Odd")
print("2. Find the Sum of Integers from 1 to 50 Using a Loop")

choice = input("Enter your choice (1-2): ")

# Run selected option
if choice == "1":
    check_even_odd()

elif choice == "2":
    sum_1_to_50()

else:
    print("Invalid choice.")
