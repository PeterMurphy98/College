def new_base(x, b):
    """Takes a number and it's base and converts to base 10."""
    # Initialise new number to 0 and input number into a string
    new = 0
    x = str(x)
    # For each character in the string, multiply it by the base to the correct power and add it to the total
    for i in range(len(x)):
        new += int(x[-(i+1)], b)*(b**i)
    return new

n1 = input("Enter number: ")
n2 = int(input("Enter base: "))
print(new_base(n1,n2))