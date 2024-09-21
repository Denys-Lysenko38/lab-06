import sys

def similar_triangle(sides, coefficient):
    return [side * coefficient for side in sides]

a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))
coefficient = float(input("Введіть коефіцієнт пропорційності: "))

new_sides = similar_triangle([a, b, c], coefficient)
print(f"Сторони подібного трикутника: {new_sides}")