num = int(input("Enter a positive integer: "))
if (num <= 0):
    print("Not a posititve number.")
    exit()

i = 1
sum0 = 0
while (i <= num):
    sum0 += i
    i += 1

print(sum0)