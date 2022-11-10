import random

# Объявляем участников поединка
user = dict.fromkeys(['name', 'health', 'damage', 'defense'])
enemy = dict.fromkeys(['name', 'health', 'damage', 'defense'])


# Функция случайно распределяет количество очков на заданное количество раз
# Первый аргумент - количество очков. Второй аргумент - количество раз
# Возвращает список распределенных очков


def generator_point(point, bonus):
    bonus_list = list(range(bonus))
    for i in bonus_list:
        if point > 0:  # защита от того, когда очки кончились раньше времени
            used_point = random.randint(1, point)
            bonus_list[i] = used_point  # Было на 1 таб меньше
            point = point - used_point  # Было на 1 таб меньше
    bonus_list[bonus - 1] = bonus_list[bonus - 1] + point
    return bonus_list


# Функция выводит данные персонажа


def print_characteristi(fighter):
    print('-' * 20)
    print(f'Боец под именем {fighter["name"]}')
    print('Характеристики: ')
    print(f"Здоровье - {fighter['health']} \n Атака - {fighter['damage']} \n Защита {fighter['defense']} ")
    print('-' * 20)


# функция случаного заполения характеристик, от заданного количества отчков.
# Первый аргумент - участник (словарь), второй параметор - количество очков


def generator_characteristic(fighter, point):
    fighter['name'] = 'Гладиатор'
    bonus_list = generator_point(point, 3)
    fighter['health'] = 150 + bonus_list[0]
    fighter['damage'] = 10 + bonus_list[1]
    fighter['defense'] = bonus_list[2]


# функция для создания персонажа игрока


def generator_user(fighter, point):
    fighter['health'] = 150
    fighter['damage'] = 10
    fighter['defense'] = 0
    while point > 0:
        print(f'У вас {point} свободных очков. Куда выхотите их потратить? \n 1. Здоровье \n 2. Атака \n 3. Броня')
        flag = input()
        user_point = int(input(f'Сколько вы хотите потратить очков? \n'))

        if user_point > point:
            print('У вас недостаточно очков')
            continue

        if flag == '1':
            fighter['health'] = fighter['health'] + user_point
            point = point - user_point
        elif flag == '2':
            fighter['damage'] = fighter['damage'] + user_point
            point = point - user_point
        elif flag == '3':
            fighter['defense'] = fighter['defense'] + user_point
            point = point - user_point
        else:
            print('Что то пошло не так')
        print_characteristi(fighter)
    print('Отлично, ваш персонаж создан!')


# функция возвращает урон с учетом защиты противника


def armor(damage, defense):
    if defense == 0:
        return damage
    else:
        return int(damage / (defense / 15))


# функция модифизирует здоровье "defencer" после атаки "attaker"


def attack(attacer, defenser):
    defenser['health'] = defenser['health'] - armor(attacer['damage'], defenser['defense'])


# Просто проверяет на смерть. True, если здоровье опустится ниже нуля


def death(fighter):
    if fighter['health'] > 0:
        return False
    else:
        return True


# Основная часть программы


user['name'] = input('Добро пожаловать на гладиаторские бои! \n Введите ваше имя: ')
print("Давайте создадим персонажа. \n")
generator_user(user, 120)
complicacy = input('Выберите сложность: \n 1. Новичек \n 2. Боец \n 3. Гладиатор \n')
if complicacy == '1':
    generator_characteristic(enemy, 70)
elif complicacy == '2':
    generator_characteristic(enemy, 110)
elif complicacy == '3':
    generator_characteristic(enemy, 130)
else:
    print('Что то пошо не так')
print('ваш противник!\n')
print(enemy)
input("Вы готовы? \n (нажмите любую клавишу)")

while True:
    attack(user, enemy)
    if death(enemy) is True:
        print(f'{user["name"]} Победил! \n Поздравляем!')
        break
    attack(enemy, user)
    if death(user) is True:
        print(f'{enemy["name"]} Победил! \n Поздравляем!')
        break
    print_characteristi(user)
    print_characteristi(enemy)
    input("нажмите любую клавишу для продолжения")
