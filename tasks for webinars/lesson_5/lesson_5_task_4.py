"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

numbers_en_to_ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('files/l5_t4_English.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    ru_lines = [f'{numbers_en_to_ru[line.split(" — ")[0]]} - {line.split(" — ")[1]}' for line in lines]
with open('files/l5_t4_Russian.txt', 'w', encoding='UTF-8') as file:
    file.writelines(ru_lines)
