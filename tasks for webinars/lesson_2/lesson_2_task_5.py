"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
print(f'Rating: {my_list}')
while True:
    newbie = int(input('Enter new rating element: '))
    for i in range(1, len(my_list)):
        if newbie <= min(my_list):
            my_list.append(newbie)
            break
        elif newbie >= max(my_list):
            my_list.insert(0, newbie)
            break
        elif my_list[i - 1] >= newbie > my_list[i]:
            my_list.insert(i, newbie)
            break
    print(f'New rating: {my_list}')
