import math

def calculate_L(a, x, y, z):
    term1 = 6 * a * x**3
    term2 = math.sin(y) * math.cos(z)
    term3 = math.tan(x + math.pi / 3)
    
    return term1 + term2 + term3

a = float(input("Введіть значення a: "))
x = float(input("Введіть значення x: "))
y = float(input("Введіть значення y: "))
z = float(input("Введіть значення z: "))

result_L = calculate_L(a, x, y, z)
print(f"Значення L: {result_L}")