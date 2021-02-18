# Define a function to return a list of all the factors of a number x.
def divisor(x):
    """Finds the divisors of a."""
    # Initialise the list of divisors with 1 and x
    divisors = (1,x)
    # Check if i divides x, from i = 1 up to i = x/2.
    # If it does, add i to the divisors list.
    for i in range(2, int(x/2) +1):
        if x % i == 0:
            divisors += (i,)
    # Return the list of divisors.
    return divisors

n = int(input("Enter a positive integer: "))
print(divisor(n))