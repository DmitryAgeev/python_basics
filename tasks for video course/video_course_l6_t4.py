"""
4. Написать функцию которая принимает на вход число от 1 до 100.
Если число равно 13, функция поднимает исключительную ситуации ValueError иначе возвращает введенное число,
возведенное в квадрат.
Далее написать основной код программы. Пользователь вводит число.
Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.
"""


def square(input_number):
    if input_number == 13:
        raise ValueError("Unlucky number!")
    else:
        return input_number ** 2


number = int(input("Enter the number(1 - 100): "))
try:
    new_number = square(number)
except ValueError:
    print("Unlucky number entered!")
else:
    print(new_number)
