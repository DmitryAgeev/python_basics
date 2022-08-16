"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('files/l5_t3.txt', 'r', encoding='UTF-8') as payment_file:
    lines = payment_file.readlines()
    poor_employee = []
    total_salary = 0
    for line in lines:
        employee, salary = line.split()
        salary = float(salary)
        total_salary += salary
        if salary < 20000:
            poor_employee.append(employee)

    print(f'Employees with a salary less than 20000: {poor_employee}')
    print(f'Average employee income: {round(total_salary / len(lines), 1)}')
