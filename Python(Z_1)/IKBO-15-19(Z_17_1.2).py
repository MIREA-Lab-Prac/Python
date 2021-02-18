import math

def Foo (x):
    if x < 70:
        return (40 * (x ** 4) -math.abs(x))
    elif 70 <= x <= 113:
        return (x ** 3 + x**2)
    elif 113 <= x < 137:
        return ((x**3 / 7) + x ** 8 + 44)
    elif x >= 137:
        return (math.log(x ** 3) + x**6)

a = Foo(75)
b = Foo(140)
print (f"{a:.2e}")
print (f"{b:.2e}")