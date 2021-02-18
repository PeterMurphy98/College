def isPal(text):
    # Initialise new string 
    new = ""
    # Add all letters, numbers and spaces from input string to new string
    for i in range (len(text)):
        if text[i].isalnum() or text[i] == " ":
            new += text[i]
    # Check if new string is the same when reversed
    if new == new[::-1]:
        print(text, "is a palindrome.")
    else:
        print(text, "is not a palindrome.")

# Prompt user for string
text = input("Enter a string (empty string to exit): ")      
# While string is non-empty
while text != "":
    # Check if it is a palindrome
    isPal(text)
    text = input("Enter a string (empty string to exit): ")
print("Finished!")  