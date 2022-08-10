"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

start = int(input('Enter the number from which you want to start generating: '))
end = int(input('Enter the number to stop at: '))
counter = count(start)
for i in range(start, end + 1):
    print(next(counter))

list_cycle = cycle(list(map(int, input('Enter elements for the list, separated by a space: ').split())))
action = None
print('q - to exit, Enter - to continue')
while action != 'q':
    print(next(list_cycle), end='')
    action = input()
