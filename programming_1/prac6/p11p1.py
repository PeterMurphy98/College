def fact(x):
    if (x >= 0):
        res = 1
        for i in range(1, x+1):
            res *= i
        return res
        
    else:
        return "Error: negative number entered."
        

n = int(input("Enter a non-negative integer: "))
print(fact(n))