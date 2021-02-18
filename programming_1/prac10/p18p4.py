def end_compare(s1, s2):
    """Checks if each string is cotained in the end of the other string."""
    # Change both strings to lower-case
    s1 = s1.lower()
    s2 = s2.lower()
    # If s2 is longer or they are the same length
    if (len(s1) <= len(s2)):
        # Check if s1 matches the end of s2
        if s2[-(len(s1)):] == s1:
            return True
        else:
            return False
    # If s1 is longer
    elif (len(s2) < len(s1)):
        # Check if s2 matches the end of s1
        if s1[-(len(s2)):] == s2:
            return True
        else:
            return False


n1 = input("Enter string 1: ")
n2 = input("Enter string 2: ")
print(end_compare(n1,n2))