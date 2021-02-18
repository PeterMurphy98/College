def xyz(s):
    """Checks if the string 'xyz', not preceeded by '.', is contained in s."""
    # Check if the first 3 letters are 'xyz'
    if s[0:3] == 'xyz':
        return True
    # Check if the i-th character is 'x'
    for i in range(1, len(s)-2):
        if s[i] == 'x':
            # Check if the next 2 letters are 'yz' and the previous character isn't '.'
            if s[i+1:i+3] == 'yz' and s[i-1] != '.':
                return True
    return False
    
n = input("Enter string: ")
print(xyz(n))