def print_max():
    def max(x, y):
        if x>y:
            return x
        else:
            return y

    n1 = float(input("Enter a number: "))
    n2 = float(input("Enter another number: "))
    print("Larger number =",max(n1, n2))

print_max()