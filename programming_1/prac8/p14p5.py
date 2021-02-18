x = int(input("Enter a positive integer: "))
while x > 0:
    def fib(N):
        def term(n):
            if n == 1:
                print("term", n)
                return 0
            elif n == 2:
                print("term", n)
                return 1
            elif n > 2:
                print("term", n)
                return term(n-1) + term(n-2)
        for i in range(1,N+1):
            print(term(i))

    fib(x)
    x = int(input("Enter a positive integer: "))