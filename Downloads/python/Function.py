import math

def f(x):
    if x <= 0:
        raise ValueError("x має бути більшим за 0")
    
    term1 = 2.7 * math.log(math.sin(math.sqrt(x)))
    term2 = 8 / (math.sqrt(x) + math.pow(x, 1/3) + 0.02)
    
    return term1 - term2

x = float(input("Введіть значення x: "))

try:
    result = f(x)
    print(f"Значення функції f(x): {result}")
except ValueError as e:
    print(e)
