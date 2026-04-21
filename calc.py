# Автор: Ольга Андросова

import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # внесены изменения
    return a * b

def sqrt(x):
    # внесены изменения
    if x < 0:
        return "Ошибка! Нельзя извлечь квадратный корень из отрицательного числа."
    else:
        return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
    print(f"2 - 2 = {subtract(2, 2)}")
    print(f"2 * 2 = {multiply(2, 2)}")
    print(f" Квадратный корень из 4 = {sqrt(4)}")
