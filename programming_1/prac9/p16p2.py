x = int(input("Enter a positive integer: "))
y = int(input("Enter another positive integer: "))

def divisor(a,b):
    """Finds the common divisors of a and b."""
    divisors = ()
    for i in range(1, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            divisors += (i,)
    return divisors

print(divisor(x,y))