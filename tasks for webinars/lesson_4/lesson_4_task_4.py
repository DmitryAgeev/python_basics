"""
4. Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

input_list = list(map(int, input('Enter numbers for the list, separated by a space: ').split()))
new_list = (number for number in input_list if input_list.count(number) == 1)
print(f'Original list: {list(new_list)}')
print(f'New list: {new_list}')
