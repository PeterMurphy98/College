def myfn(N):
    def term(n):
        if n == 1:
            print("term", n)
            return 2
        elif n > 1:
            print("term", n)
            return 2*term(n-1)

    for i in range(1,N+1):
        print(term(i))


x = int(input("Enter an integer >= to 1: "))
while x >= 1:
    myfn(x)
    x = int(input("Enter an integer >= to 1: "))