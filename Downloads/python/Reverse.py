import sys

num1 = int(input("Введіть перше двоцифрове число: "))
num2 = int(input("Введіть друге двоцифрове число: "))

def reverse_digits(num):
    tens = num // 10
    units = num % 10
    return units * 10 + tens

reversed_num1 = reverse_digits(num1)
reversed_num2 = reverse_digits(num2)

print(f"Змінене перше число: {reversed_num1}")
print(f"Змінене друге число: {reversed_num2}")