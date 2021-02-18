n = int(input("Enter a number: "))
for x in range(2, n+1):
    for i in range (2, x):
        if x % i == 0:
            print(x, "=", i, "*", x//i)
            break
    else:
        print(x, "is a prime number.")