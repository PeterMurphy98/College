amount = float(input('Amount: '))
am1 = amount*0.6
am2 = amount*0.4
tax1 = am1*0.135
tax2 = am2*0.23
tot = amount+tax1+tax2
print('Amount:', amount) 
print('Tax1:', tax1) 
print('Tax2:', tax2) 
print('Total tax:', tax1+tax2)
print('Total amount:', tot)