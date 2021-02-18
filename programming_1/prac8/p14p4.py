n = int(input("Enter a number: "))
for x in range(2, n+1):
    a = 0
    for i in range (2, x):
        if x % i == 0:
            print(x, "=", i, "*", x//i)
            a += 1
    else:
        if a == 0:
            print(x, "is a prime number.")