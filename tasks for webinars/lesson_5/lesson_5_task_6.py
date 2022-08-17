"""
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —

Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def get_count_lessons_by_subject(lesson):
    if lesson != '—':
        return int(lesson.split('(')[0])
    return 0


def get_sum_lessons(lessons):
    return sum([get_count_lessons_by_subject(lesson) for lesson in lessons])


with open('files/l5_t6.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    school_dict = {}
    for line in lines:
        subj_name, *lessons = line.strip().split()
        school_dict[subj_name.split(':')[0]] = get_sum_lessons(lessons)
    print(school_dict)
