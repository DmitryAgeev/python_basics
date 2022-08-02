"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
"""
distance = float(input('Enter the number of kilometers on the first day: '))
last_distance = float(input('Enter the desired number of kilometers: '))
day = 1
while distance < last_distance:
    print(f'{day} day: {round(distance, 2)} km')
    distance *= 1.1
    day += 1
print(f'{day} day: {round(distance, 2)} km')
print(f'Answer: on day {day}, the athlete achieved a result of at least {last_distance} km.')
