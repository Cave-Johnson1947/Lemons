num_names = int(input("How many names do you have?: "))  # Store the input in a variable

my_string = ""

for i in range(num_names):  # Use the stored variable
    my_string += input("Enter name: ") + " "  # Add a space instead of a newline

print(my_string.strip())  # Strip trailing space before printing