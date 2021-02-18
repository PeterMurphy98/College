curr1 = float(input('Currency 1: ')) 
if (curr1 < 0):
    print('Amount must be >= 0. Please try again.')
    quit()
# Euro to Pound sterling
rate = 0.91
curr2 = curr1*rate
print('Currency 2:', curr2)