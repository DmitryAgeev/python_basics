"""
2. Создать текстовый файл (не программно),сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('files/l5_t2.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f'Number of lines in the file: {len(lines)}')
    for i, line in enumerate(lines, 1):
        print(f'Number of words in {i} line: {len(line.split())}')
