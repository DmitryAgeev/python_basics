"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
    [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json

with open('files/l5_t7.txt', 'r', encoding='UTF-8') as file:
    income_sum = 0
    res = {}
    lines = file.readlines()
    for line in lines:
        name, form, gain, outcome = line.split()
        income = float(gain) - float(outcome)
        res[name] = income
        if income > 0:
            income_sum += income

res['average_income'] = round(income_sum / len(lines), 2)

with open('files/l5_t7.json', 'w', encoding='UTF-8') as file:
    json.dump(res, file)
