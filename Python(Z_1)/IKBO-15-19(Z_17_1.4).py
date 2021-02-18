import math

def Foo(n):
    a = 4
    if (n != 0):
        a = 1/46 * Foo(n - 1) + math.tan(Foo(n - 1)) + 75
    return a

s = Foo(11)
d = Foo(7)
print (f"{s:.2e}")
print (f"{d:.2e}")