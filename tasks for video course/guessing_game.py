import random

number = random.randint(1, 100)
# print(number)
player_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input("Выберите уровнь сложности 1-3: "))
max_count = levels[level]
player_count = int(input("Введите количество игроков: "))
players = []
for i in range(player_count):
    player_nik = input(f"Введите имя {i + 1} игрока: ")
    players.append(player_nik)
is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print("Вы проиграли")
        break
    print(f"Попытка №{count}")
    for player in players:
        print(f"Ход игрока: {player}")
        player_number = int(input("Угадайте число от 1 до 100: "))
        if player_number == number:
            is_winner = True
            winner_name = player
            break
        elif player_number < number:
            print("Ваше число меньше загаданного")
        else:
            print("Ваше число больше загаданного")
else:
    print(f"Победил {winner_name}!")
