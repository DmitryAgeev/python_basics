"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

import random


class Matrix:
    def __init__(self, list_list: list):
        self.list_list = list_list

    def __str__(self):
        for i in self.list_list:
            print(i)
        return ''

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.list_list)):
            new_list = []
            for j in range(len(self.list_list[i])):
                ii = self.list_list[i]
                try:
                    jj = other.list_list[i]
                    new_list.append(ii[j] + jj[j])
                except IndexError:
                    new_list.append(ii[j])
            new_matrix.append(new_list)
        return Matrix(new_matrix)


def generate_matrix(a=1, b=1):
    """Генератор случайного списка списков
    :param a: int, количество списков
    :param b: int, количество елементов в списке
    :return: list, матрица
    """
    matrix_list = [[random.randint(0, 50) for i in range(b)] for i in range(a)]
    return matrix_list


m_list, m_list_el = list(map(int, input("Enter the size of the first matrix: ").split()))
matrix_1 = Matrix(generate_matrix(m_list, m_list_el))
print(f"First matrix ↑\n{matrix_1}")
m_list, m_list_el = list(map(int, input("Enter the size of the second matrix: ").split()))
matrix_2 = Matrix(generate_matrix(m_list, m_list_el))
print(f"Second matrix ↑\n{matrix_2}")
print(f"First + second ↑\n{matrix_1 + matrix_2}")
