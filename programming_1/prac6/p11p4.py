n = int(input("Enter an integer: "))
if (n <= 0):
    print("Number must be positive.")
elif (n==1):
    print("1")
else:
    print("1")
    C_old = 1
    for i in range (1,n):
        C_new = 2*(2*i-1)/(i+1) *C_old
        C_old = C_new
        print(int(C_new))
