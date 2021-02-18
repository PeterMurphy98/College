# Define a funtion that returns true if the string is a palindrome.
def isPalindrome(s):
    """Checks if s is a palindrome."""
    # Define a function that changes the letters to lowercase and removes non-letters.
    def toChars(s):
        """Converts string to lower case and removes non-letters."""
        # Changes s to lowercase.
        s = s.lower()
        chars = ""
        # Removes non-letters.
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                chars += c
        # Returns new string.
        return chars
    # Define a function that checks if the string is the same when it is reversed.
    def isPal(s):
        """Checks if the first and last letters of s are the same. 
           Then uses recursion to check the rest of the string"""
        # If the string is of length 0 or 1, return True.
        if len(s) <= 1:
            return True
        # Else, check if the first and last characters are the same. 
        # Then, use recursion to check the rest of the string.
        else:
            # If the first and last letters match, and the rest of the string mathes, return True.
            return s[0] == s[-1] and isPal(s[1:-1])
    # Use toChars to change the string, and use isPal to check if it's a palindrome.
    return isPal(toChars(s))

text = input("Enter a string: ")
print(isPalindrome(text))