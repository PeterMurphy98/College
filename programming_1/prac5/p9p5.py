top_pos = int(input("Enter the number of possible toppings: "))
top_per = int(input("Enter the number of toppings per pizza: "))
if(top_per <=0 or top_pos <=0):
    print("Topping numbers must be positive.")
    exit()

comb = 1
for i in range (top_pos+1 - top_per, top_pos+1):
    comb = comb*i
for i in range (1,top_per+1):
    comb = comb/i

print("Number of different combinations: ", int(comb))