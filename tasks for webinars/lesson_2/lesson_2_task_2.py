"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

some_list = input('Enter some list items separated by space: ').split()

for i in range(0, len(some_list) - 1, 2):
    some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
print(f'Your list with changed element position: {some_list}')
