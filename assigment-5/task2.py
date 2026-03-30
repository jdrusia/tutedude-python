# Task 2: Demonstrate List Slicing

# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

print("Original list:", numbers)

#  Extracts the first five elements from the list.
first_five = numbers[:5]
print("Extracted first five elements:", first_five)

# Reverse these extracted elements.
reversed_first_five = first_five[::-1]
print("Reversed extracted elements:", reversed_first_five)
