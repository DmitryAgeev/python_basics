"""
6. Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word: str):
    return f'{word[0].upper()}{word[1:]}'


def capitalize_func(text: str):
    words = text.split()
    return ' '.join(list(map(lambda word: int_func(word), words)))


string = input('Enter text: ')
print(capitalize_func(string))

# In Python 3.6+ it's much easier.
print(string.title())
