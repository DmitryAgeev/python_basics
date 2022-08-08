"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Division by 0!')
        return


dividend, divisor = map(int, input('Enter dividend and divisor separated by space: ').split())

print(division(dividend, divisor))
