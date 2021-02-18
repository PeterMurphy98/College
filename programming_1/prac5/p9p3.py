num = int(input("Enter a positive integer: "))
if (num <= 0):
    print("Not a posititve number.")
    exit()

fact = num
for i in range(1,num):
    fact = fact*i

print(fact)    