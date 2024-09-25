import math

def calculate_f(x):
    if x >= 5.2:
        return math.exp(3.27 * x**2 - 9) + 1
    elif 0.19 < x < 5.2:
        return math.cos(x) + 1 / math.tan(x) + math.sqrt(abs(x - 7.84))
    elif x <= 0.19:
        return math.sin(x - 0.7) + 3.33 * 2**x

x = float(input("Введіть значення x: "))
print(f"Значення функції f(x): {calculate_f(x)}")
