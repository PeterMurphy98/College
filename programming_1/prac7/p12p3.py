def root(x,t):
    for i in range(int(x+1)):
        if (i**2 < x + t and i**2 > x - t):
            print(i)
            break 
        if (i**2 > x):
            print("No root found.")
            break

n = float(input("Enter a number: "))
if (n < 0):
    print("Number was negative.")
    exit()
else:
    root(n, 0.001)