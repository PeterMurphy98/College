n = 1
sum1 = 0
while (n < 10001):
    if ((n % 3 == 0) or (n % 5 == 0)):
        sum1 += n
        
    n += 1

print(sum1)