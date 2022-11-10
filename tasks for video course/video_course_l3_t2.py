"""
2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""


def get_max(a, b, c):
    result = max([a, b, c])
    return result


first_digit, second_digit, third_digit = input("Введите 3 числа: ").split()
print("Наибольшее из них: ", get_max(int(first_digit), int(second_digit), int(third_digit)))
