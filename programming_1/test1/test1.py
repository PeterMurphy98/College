# asks user for integer
x = int(input("Enter a non-negative integer: "))
if (x < 0):
    print("Error: Number was negative.")
    exit()

# initialise loop counter and divisor counters
i = 1
num_div_3 = num_div_5 = num_div_7 = num_div_11 = 0

while(i < x+1):
    # if i is divisible by 3 add 1 to the counter 
    if (i % 3 == 0):
        num_div_3 += 1
    # if i is divisible by 5 add 1 to the counter
    if (i % 5 == 0):
        num_div_5 += 1
    # if i is divisible by 7 add 1 to the counter
    if (i % 7 == 0):
        num_div_7 += 1
    # if i is divisible by 11 add 1 to the counter
    if (i % 11 == 0):
        num_div_11 += 1
    
    i+=1

print("Number of numbers divisible by 3: ", num_div_3)
print("Number of numbers divisible by 5: ", num_div_5)
print("Number of numbers divisible by 7: ", num_div_7)
print("Number of numbers divisible by 11: ", num_div_11)
print("Finished!")