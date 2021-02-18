def new_base(x, b):
    """Takes a number, x, in base 10 and converts to base b."""
    # Initialise the new number as a string 
    new = '' 
    # While the division result is not equal to 0
    while x != 0:
        # add the remainder to the string
        remainder = x % b
        new += str(remainder)
        x = x // 2
    # Reverse the string
    return new[::-1]

n1 = int(input("Enter number: "))
n2 = int(input("Enter base: "))
print(new_base(n1,n2))