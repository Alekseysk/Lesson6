"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income = {'инженер': {"wage": 25000, "bonus": 10000},
                'мл. инженер': {"wage": 15000, "bonus": 3000},
                'ст. инженер': {"wage": 35000, "bonus": 15000},
                'гл. инженер': {"wage": 55000, "bonus": 20000}}
    
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
    
    
class Position(Worker):
    
    def get_full_name(self):
        print(f'Работник - {self.name} {self.surname}')
    
    def get_total_income(self):
        if self.position in self._income.keys():
            print(f'Доход = {self._income[self.position]["wage"] + self._income[self.position]["bonus"]} руб.')
        else:
            print('Позиция такая не найдена')
            

Petrov = Position('Василий', 'Петров', 'ст. инженер')
Petrov.get_full_name()
Petrov.get_total_income()