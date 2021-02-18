num = 1

while (num != 0):
    num = int(input("Enter a non-zero integer: "))
    i = 0
    while (i < abs(num)):
        if (i**3 == num):
            print("Cube root: ",i)
            break
        elif (-i**3 == num):
            print("Cube root: ", -i)
            break    
        
        if (abs(i**3) > abs(num)):
            print("Not a perfect cube.")
            break
        
        i+=1
