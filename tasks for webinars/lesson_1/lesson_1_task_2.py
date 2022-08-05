"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

input_time = int(input('Enter time in seconds: '))

hours = input_time // 3600
minutes = input_time % 3600 // 60
seconds = input_time % 3600 % 60

print(f'Your time: {hours:02}:{minutes:02}:{seconds:02}')
