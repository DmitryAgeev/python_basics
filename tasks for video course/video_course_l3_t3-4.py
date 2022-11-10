player = {"name": input("Введите имя игрока: "), "health": 100, "damage": 20, "armor": 1.2}
enemy = {"name": input("Введите имя противника: "), "health": 50, "damage": 10, "armor": 1.2}


def attack(attacker, defender):
    defender["health"] -= real_damage(attacker["damage"], defender["armor"])


def real_damage(damage, armor):
    return damage / armor


attack(player, enemy)
attack(enemy, player)
print("Игрок атаковал противника, противник атаковал игрока. \nРезультат боя: ", player, enemy)
