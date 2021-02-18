def fact(x):
    if x == 0:
        prod = 1
    else:
        prod = x*fact(x-1)

    return prod

n = int(input("Enter a non-negative integer: "))
if (n < 0):
    print("Number was negative.")
    exit()
else:
    print(fact(n))