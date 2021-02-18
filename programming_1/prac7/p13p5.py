def f(x):
    print('In function f:')
    x *= 5
    y = 2
    # It prints the local x *= 5 instead of the global x = 10, so when the function ends, it goes back to the local x = 10.
    print('x is', x)

    # It prints the local y = 2 instead of the global y = 20, so when the function ends, it goes back to the local y = 20.
    print('y is', y)

    # Prints the global z 
    print('z is', z)
    return x

x, y, z = 10, 20, 30

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)

# z is assigned the value x*5  by the function
z = f(x)

print('After function f:')
# Now the local x = 50 in the function is gone, so it prints the global x = 10
print('x is', x)
# Now the local y = 2 in the function is gone, so it prints the global y = 20
print('y is', y)
# z was assigned a new value = 10*5
print('z is', z)
