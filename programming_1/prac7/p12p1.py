def fact(x):
    prod = 1
    if (x == 0):
        return prod
    else:
        for i in range(1,x+1):
            prod *= i
        return prod

n = int(input("Enter a non-negative integer: "))
if (n < 0):
    print("Number was negative.")
    exit()
else:
    print(fact(n))