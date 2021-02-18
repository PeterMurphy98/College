def max(x, y):
    if x>y:
        return x
    else:
        return y

n1 = float(input("Enter a number: "))
n2 = float(input("Enter another number: "))
lar = max(n1, n2)
print("Larger number =", lar)
