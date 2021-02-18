import math

def Foo (x, y):
    return 75 * (x ** 2) - 17 * (y ** 8) + math.sqrt((65 * (x ** 7) - math.cos(x)) / ((x ** 6) / 7) + x**8 + 44) - math.sqrt((math.log(y) + y**4) / (87*(x**8) + math.sin(y) - 40))

a = Foo(52, 21)
b = Foo(64, 48)
print (f"{a:.2e}")
print (f"{b:.2e}")