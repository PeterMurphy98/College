from os import path
# Prompt user for filename
filename = input("Enter file name: ")
if filename == "":
    filename = "lines.txt"
if path.exists(filename) != True:
    # Exit program if file doesn't exist
    print("File not found.")
    exit()
# Read file line by line into list
f = open(filename, "r")
lines = f.readlines()
# Prompt user for string to search for
text = input("Enter a string (empty string to exit): ")
# While the string is non-empty
while text != "":
    # Initialise lines found count to 0
    lines_found = 0
    # Check if string is contained in each line
    for line in lines:
        # If it is found, print the line and add one to the lines found count
        if line.count(text) != 0:
            print(text, " found in following line: ")
            print(line)
            lines_found += 1
    # If no lines were found and the string length is greater than 5, remove the last character
    if lines_found == 0 and len(text) > 5:
        text = text[:-1]
    else:
        if lines_found == 0:
            print("No match found.")
        # Prompt user for new string
        text = input("Enter a string (empty string to exit): ")
print("Finished!")