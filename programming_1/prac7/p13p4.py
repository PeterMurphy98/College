def f(x):
    print('In function f:')
    x += 1
    y = 1
    print('x is', x)
    print('y is', y)
    print('z is', z)
    return x

x, y, z = 5, 10, 15

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)

z = f(x)

print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
