count_0 = count_0_20 = count_20_40 = count_40_60 = count_60_80 = count_80_100 = count_100 = 0
num =1 
while (num >=0):
    num = int(input("Enter a number: "))
    if (num > 100):
        count_100 += 1
    elif (num > 80 and num <= 100):
        count_80_100 += 1
    elif (num > 60 and num <= 80):
        count_60_80 += 1
    elif (num > 40 and num <= 60):
        count_40_60 += 1
    elif (num > 20 and num <= 40):
        count_20_40 += 1
    elif (num > 0 and num <= 20):
        count_0_20 += 1
    elif (num == 0):
        count_0 += 1
        
print("Numbers = 0                ", count_0)
print("Numbers > 0  and <= 20     ", count_0_20)
print("Numbers > 20 and <= 40     ", count_20_40)
print("Numbers > 40 and <= 60     ", count_40_60)
print("Numbers > 60 and <= 80     ", count_60_80)
print("Numbers > 80 and <= 100    ", count_80_100)
print("Numbers > 100              ", count_100)    
