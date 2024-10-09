import math

def f(x):
    return math.exp(x) / (x**2 + 0.11)

a = float(input("Введіть початкове значення a: "))
b = float(input("Введіть кінцеве значення b: "))
h = float(input("Введіть крок h: "))

print("\nПробатування функції за допомогою циклу for:")
results_for = []
x = a
while x <= b:
    result = f(x)
    results_for.append(result)
    print(f"f({x}) = {result}")
    x += h

print("\nПробатування функції за допомогою циклу while:")
results_while = []
x = a
while x <= b:
    result = f(x)
    results_while.append(result)
    print(f"f({x}) = {result}")
    x += h

print("\nСписок значень функції (з циклу while):")
print(' '.join(map(str, results_while)))

results_while.sort(reverse=True)
print("\nВідсортований список за спаданням:")
print(' '.join(map(str, results_while)))

mid_index = len(results_while) // 2

list1 = results_while[:mid_index]
list2 = results_while[mid_index:]

if list1:
    print("\nПерший список:")
    print(' '.join(map(str, list1)))

if list2:
    print("Другий список:")
    print(' '.join(map(str, list2)))