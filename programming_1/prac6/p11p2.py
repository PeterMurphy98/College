n = int(input("Enter an integer: "))
if (n == 0):
    print("")
elif (n == 1):
    print("1,")
elif (n ==2):
    print("1, 1,")
else:
    i = a = b = 1 
    print(a, end=', ')
    print(b, end=', ')
    while (i < n-1):
        x = a + b
        a, b = b, x
        print(x, end=', ')
        i +=1
    