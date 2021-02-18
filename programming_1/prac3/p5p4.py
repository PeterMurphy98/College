n = int(input('Enter integer: '))
if (n == 0):
    print('Number is 0.')
elif (n > 0 and n <= 20):
    print('Number is between 1 and 20')
elif (n > 20 and n <= 40):
    print('Number is between 21 and 40')
elif (n > 40 and n <= 60):
    print('Number is between 41 and 60')
elif (n > 60 and n <= 80):
    print('Number is between 61 and 80')
elif (n > 80 and n <= 100):
    print('Number is between 81 and 100')
elif (n > 100):
    print('Number is greater than 100')
else:
    print('Number is negative')