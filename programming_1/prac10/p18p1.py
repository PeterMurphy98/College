# Assuming the input is from the toChars function, i.e. lower-case letters only
def isPal(text):
    """Returns true if the text is the same when reversed."""
    # Check if the i-th character is equal to the i-th character from the end
    for i in range(int(len(text)/2)):
        # If the letters match, continue to the next one
        if text[i] == text[-(i+1)]:
            continue
        # Else, return False
        else:
            return False
    # If all letters match, return True
    return True
    
n = input("Enter text: ")
print(isPal(n))