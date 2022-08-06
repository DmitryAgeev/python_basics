"""
3. Реализовать функцию my_func(),которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(numbers))
    return sum(numbers)


number_1, number_2, number_3 = map(int, input('Enter three numbers separated by space: ').split())

print(f'Sum of the two largest numbers: {my_func(number_1, number_2, number_3)}')
