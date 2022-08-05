"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_months_list = ['stub', 'winter', 'winter', 'spring', 'spring', 'spring',
                       'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
seasons_months_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
}
month = int(input('Enter the month number(1-12): '))
print(f'Season of this month is {seasons_months_dict[month]} (dictionary search)')
print(f'Season of this month is {seasons_months_list[month]} (list search)')
