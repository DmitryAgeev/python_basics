"""
3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
"""

import video_course_l4_t2
from video_course_l4_t1 import create_folder, remove_folder

create_folder()
remove_folder()
print(video_course_l4_t2.get_random(input("Введите элементы для списка через пробел: ").split()))
