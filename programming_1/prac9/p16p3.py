def perfect(a):
    """Finds all perfect numbers <= a."""
    perf = ()
    for i in range(1,a+1):
        divisors = ()
        for j in range(1,i):
            if i % j == 0:
                divisors += (j,)
            
        if sum(divisors) == i:
            perf += (i,)

    return perf

x = int(input("Enter a positive integer: "))
print(perfect(x))