import math

def find_farthest_point(A, B, C):
    distance_A = abs(A[0]) + abs(A[1])
    distance_B = abs(B[0]) + abs(B[1])
    distance_C = abs(C[0]) + abs(C[1])

    if distance_A >= distance_B and distance_A >= distance_C:
        return "A"
    elif distance_B >= distance_A and distance_B >= distance_C:
        return "B"
    else:
        return "C"

A = tuple(map(float, input("Введіть координати точки A (використовуючи пробіл): ").split()))
B = tuple(map(float, input("Введіть координати точки B (використовуючи пробіл): ").split()))
C = tuple(map(float, input("Введіть координати точки C (використовуючи пробіл): ").split()))

print(f"Точка з найбільшою відстанню до осей координат: {find_farthest_point(A, B, C)}")