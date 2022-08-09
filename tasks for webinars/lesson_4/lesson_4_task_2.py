"""
2. Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def numbers_in_order(some_list):
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i - 1]:
            yield some_list[i]


input_list = list(map(int, input('Enter numbers for the list, separated by a space: ').split()))
print(f'Original list: {input_list}')
new_list = [number for number in numbers_in_order(input_list)]
print(f'New list: {new_list}')
