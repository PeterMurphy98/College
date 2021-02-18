year = int(input('Year: '))
if (year >= 0):
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        print('This is a leap year.')
    else:
        print('Not a leap year.')