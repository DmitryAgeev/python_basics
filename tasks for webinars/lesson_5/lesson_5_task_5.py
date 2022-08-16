"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

some_file = 'files/l5_t5.txt'
with open(some_file, 'w', encoding='UTF-8') as file:
    file.write(input('Enter numbers separated by spaces: '))

with open(some_file, 'r', encoding='UTF-8') as file:
    numbers_string = file.read()
    print(sum([float(number) for number in numbers_string.split()]))
