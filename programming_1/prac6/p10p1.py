num = int(input("Enter an integer: "))
if (num < 0):
    print("Number was negative.")
    exit()
i = 0
while (i < num):
    if (i**2 == num):
        print("Square root: ",i)
        break
    
    if (i**2 > num):
        print("Not a perfect square.")
        break
    
    i+=1
