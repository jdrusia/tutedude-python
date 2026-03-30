# Task 1: Read a file and handle errors

file_name = input("Enter the file name (default: output.txt): ") or "output.txt"

try:
    # open file in read mode
    # with is used so that the file is closed properly, even if there are exceptions
    with open(file_name, "r") as file:
        print("Reading file content:")

        i = 1
        # read file line by line
        for line in file:
            print(f"Line {i}: {line.strip()}")
            i += 1

# exception to catch file not found error
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

# exception to catch other general exceptions
except Exception as e:
    print(f"An error occurred: {e}")
