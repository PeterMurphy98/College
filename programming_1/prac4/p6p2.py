num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
num3 = int(input('Number 3: '))

ans = 0
if (num1 % 2 != 0):
    ans = num1

if (num2 % 2 != 0 and num2 > ans):
    ans = num2

if (num3 % 2 != 0 and num3 > ans):
    ans = num3

if (num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0):
    print('No odd numbers.')
    exit()

print('Largest odd number:', ans)
exit()

