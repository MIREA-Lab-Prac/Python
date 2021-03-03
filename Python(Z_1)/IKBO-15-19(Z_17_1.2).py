import math

def f12 (x):
    result = 0
    if x < 70:
        result = (40 * (x ** 4) - abs(x))
        return result
    elif 70 <= x < 113:
        result = (x ** 3 + x**2)
        return result
    elif 113 <= x < 137:
        result = ((x**3 / 7) + x ** 8 + 44)
        return result
    elif x >= 137:
        result = (math.log(x ** 3) + x**6)
        return result
