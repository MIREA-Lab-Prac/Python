import math

def Foo(n, m):
    a = 0
    b = 0
    for i in range(1 ,n+1):
        a += (75 * (i**2)) - (17 * (i ** 8))
    for i in range(1, n+1):
        for j in range(1, m+1):
            b += (65 * (i ** 7)) - math.cos(j)
    b /= 44
    return a - b

s = Foo(95, 75)
d = Foo(92, 91)
print (f"{s:.2e}")
print (f"{d:.2e}")
