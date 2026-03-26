# Task 1: Read a file and handle errors

file_name = input("Enter the file name (default: output.txt): ") or "output.txt"

try:
    # open file in read mode
    with open(file_name, "r") as file:
        print("Reading file content:")

        # read file line by line
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
