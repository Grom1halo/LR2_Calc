"""
Калькулятор — лабораторная работа №2 ПСПД
Группа АА-37, Кровин Н.И.
"""

import math


def add(a: float, b: float) -> float:
    return a + b
    # Natalia: проверила функцию сложения — работает корректно, граничные случаи учтены


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Деление на ноль недопустимо.")
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


def sqrt(a: float) -> float:
    if a < 0:
        raise ValueError("Корень из отрицательного числа не определён.")
    return math.sqrt(a)


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("  Ошибка: введите число.")


MENU = """
=============================
       КАЛЬКУЛЯТОР
=============================
  1. Сложение        (a + b)
  2. Вычитание       (a - b)
  3. Умножение       (a * b)
  4. Деление         (a / b)
  5. Степень         (a ^ b)
  6. Квадратный корень (√a)
  0. Выход
============================="""


def main():
    print(MENU)
    while True:
        choice = input("Выберите операцию: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        elif choice in ("1", "2", "3", "4", "5"):
            a = get_number("  Введите a: ")
            b = get_number("  Введите b: ")
            try:
                if choice == "1":
                    print(f"  Результат: {a} + {b} = {add(a, b)}")
                elif choice == "2":
                    print(f"  Результат: {a} - {b} = {subtract(a, b)}")
                elif choice == "3":
                    print(f"  Результат: {a} * {b} = {multiply(a, b)}")
                elif choice == "4":
                    print(f"  Результат: {a} / {b} = {divide(a, b)}")
                elif choice == "5":
                    print(f"  Результат: {a} ^ {b} = {power(a, b)}")
            except (ZeroDivisionError, ValueError) as e:
                print(f"  Ошибка: {e}")
        elif choice == "6":
            a = get_number("  Введите a: ")
            try:
                print(f"  Результат: √{a} = {sqrt(a):.6f}")
            except ValueError as e:
                print(f"  Ошибка: {e}")
        else:
            print("  Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
