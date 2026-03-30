# Task 2: Write and append data to a file

file_name = input("Enter the file name (default: output.txt): ") or "output.txt"

try:
    # take input and write to file
    text = input("Enter text to write to the file: ")
    with open(file_name, "w") as file:
        file.write(text + "\n")
    print(f"Data successfully written to {file_name}.")

    # take input and append to file
    more_text = input("Enter additional text to append: ")
    with open(file_name, "a") as file:
        file.write(more_text + "\n")
    print("Data successfully appended.")

    # read and display final content
    print(f"\nFinal content of {file_name}:")
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

# exception to catch file not found error
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

# exception to catch other general exceptions
except Exception as e:
    print(f"An error occurred: {e}")
