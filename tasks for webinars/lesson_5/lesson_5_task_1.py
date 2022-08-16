"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open(input('Enter file name: '), 'w', encoding='UTF-8') as some_file:
    while True:
        input_text = input('Enter data or press Enter to end the recording: ')
        if input_text == '':
            break
        some_file.write(f'{input_text}\n')
