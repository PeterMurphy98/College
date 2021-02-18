n = int(input("Enter an integer: "))
while (n >= 0):
    if (n == 0):
        print("")
    elif (n == 1):
        print("1,")
    elif (n ==2):
        print("1, 1,")
    else:
        a = 1
        b = 1 
        print(a, end=', ')
        print(b, end=', ')
        for i in range(n-2):
            x = a + b
            a, b = b, x
            print(x, end=', ')
            i +=1
        print("")
        
    n = int(input("Enter an integer: "))