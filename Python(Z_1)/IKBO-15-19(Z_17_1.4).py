import math

def f14(n):
    a = 4
    if (n != 0):
        a = 1/46 * Foo(n - 1) + math.tan(Foo(n - 1)) + 75
    return a