"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
from abc import ABC


class NegativeNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def chekNumber(number):
        if number < 0:
            raise NegativeNumber('Action is impossible! Account less than zero!')


class Warehouse:
    office_equi = {}  # 90
    warehouse_equi = {}  # 10
    defect = {}  # 9999

    def __str__(self):
        return 'Office' + str(self.office_equi) + '\n' \
               + 'Stock' + str(self.warehouse_equi) + '\n' \
               + 'Marriage Warehouse' + str(self.defect)

    def appequi(self, equipment):
        self.warehouse_equi[equipment.name] = equipment.quantity

    def storageArea(self, cls, area: int):
        """ Перемещение на складах 90 -> 10  or 10 -> 90
        :param cls: дочерний класс OfficeEquipment
        :param area: int, перемещение на какой склад по номеру 90 or 10
        :return: None
        """
        if area == 90:
            try:
                result = self.warehouse_equi[cls.name] - cls.quantity
                NegativeNumber.chekNumber(result)
                try:
                    self.office_equi[cls.name] += cls.quantity
                except KeyError:
                    self.office_equi[cls.name] = cls.quantity
            except NegativeNumber as err:
                print(err)
            else:
                self.warehouse_equi[cls.name] = result
        elif area == 10:
            try:
                result = self.office_equi[cls.name] - cls.quantity
                NegativeNumber.chekNumber(result)
                try:
                    self.warehouse_equi[cls.name] += cls.quantity
                except KeyError:
                    print('Position not previously posted')
                    self.appequi(cls)
            except NegativeNumber as err:
                print(err)
            else:
                self.office_equi[cls.name] = result
        else:
            print('Invalid move code')

    def defected(self, cls, area: int):
        """ Перемещение в брак со склада 90 or 10
        :param cls: дочерний класс OfficeEquipment
        :param area: int, перемещение на какой склад по номеру 90 or 10
        :return: None
        """
        if area == 90:
            try:
                result = self.office_equi[cls.name] - cls.quantity
                NegativeNumber.chekNumber(result)
                try:
                    self.defect[cls.name] += cls.quantity
                except KeyError:
                    self.defect[cls.name] = cls.quantity
            except NegativeNumber as err:
                print(err)
            else:
                self.office_equi[cls.name] = result
        elif area == 10:
            try:
                result = self.warehouse_equi[cls.name] - cls.quantity
                NegativeNumber.chekNumber(result)
                try:
                    self.defect[cls.name] += cls.quantity
                except KeyError:
                    self.defect[cls.name] = cls.quantity
            except NegativeNumber as err:
                print(err)
            else:
                self.warehouse_equi[cls.name] = result
        else:
            print('Invalid move code')


class OfficeEquipment(ABC):
    name: str

    def __init__(self, quantity: int):
        try:
            self.quantity = quantity
            NegativeNumber.chekNumber(quantity)
        except NegativeNumber as err:
            print(err)
            self.quantity = 0

    @property
    def action(self):
        pass


class Calc(OfficeEquipment):
    name = 'Calculator'

    @property
    def action(self):
        return print('Performs a calculation')


class CashRegister(OfficeEquipment):
    name = 'Cash machine'

    @property
    def action(self):
        return print('Operations with cash')


class MultifunctionDevice(OfficeEquipment):
    name = 'МФУ'

    @property
    def action(self):
        return print('Copies, prints, scans')


if __name__ == '__main__':
    one = Calc(10)
    two = CashRegister(3)
    three = MultifunctionDevice(10)
    error_equip = Calc(-2)
    one.action
    two.action
    three.action

    print(error_equip.quantity)
    one_defect = Calc(15)
    warehouse = Warehouse()
    warehouse.appequi(one)
    warehouse.appequi(two)
    warehouse.appequi(three)
    print(warehouse)
    warehouse.storageArea(one, 90)
    print(warehouse)
    warehouse.defected(one_defect, 90)
    print(warehouse)
