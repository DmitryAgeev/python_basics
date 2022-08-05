"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = input('Enter positive integer: ')
numeral = 0
i = 0
while i != len(number):
    if int(number[i]) == 9:
        numeral = int(number[i])
        break
    if int(number[i]) > numeral:
        numeral = int(number[i])
    i += 1
print(f'The biggest digit in the number: {numeral}')
