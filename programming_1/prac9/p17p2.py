# Define a function that returns the list of common divisors of x and y.
def divisor(x,y):
    """Finds the common divisors of x and y."""
    # Check if x or y divide each other.
    if max(x,y) % min(x,y) != 0:
        # If not, initialise the list of common divisors with 1.
        divisors = (1,)
        # Check if i divides both x and y, from i = 1 up to half of the lower number.
        # If it does, add i to the list of common divisors.
        for i in range(2, int(min(x,y)/2) +1):
            if x % i == 0 and y % i == 0:
                divisors += (i,)
        # Return the list of common divisors.
        return divisors
    # If x or y divides the other, 
    # Use the algorithm from p17p1.py to find the list of divisors of the lower number.
    else:
        divisors = (1, min(x,y))
        for i in range(2, int(min(x,y)/2) +1):
            if min(x,y) % i == 0:
                divisors += (i,)
        return divisors

n1 = int(input("Enter a positive integer: "))
n2 = int(input("Enter another positive integer: "))
print(divisor(n1,n2))