num = 1
while (num >=0):
    num = int(input("Enter a number: "))
    if (num < 0):
        break
    if (num % 2 == 0):
        print("Divisible by 2.")
    if (num % 3 == 0):
        print("Divisible by 3.")
    if (num % 5 == 0):
        print("Divisible by 5.")
    if (num % 7 == 0):
        print("Divisible by 7.")
    