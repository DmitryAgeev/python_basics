"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = int(input('Enter the revenue of the firm: '))
costs = int(input('Enter the costs of the firm: '))
if revenue > costs:
    profit = (revenue - costs) / revenue
    print(f'The firm makes a profit! Revenue profitability: {round(profit, 2)}')
    employees = int(input('Enter the number of employees in the company: '))
    margin = profit / employees
    print(f'Profit of the company per employee: {round(margin, 2)}')
elif revenue < costs:
    print('The firm is operating at a loss!')
else:
    print('Revenues equal costs.')
