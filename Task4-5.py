"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print('Машинка поехала')
    
    def stop(self):
        print('Машинка остановилась')
    
    def turn(self, direction):
        print(f'Машинка повернула {direction}')
    
    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    
    def show_speed(self):
        print(f'Текущая скорость {self.speed}', end='\t')
        if self.speed > 60:
            print('Превышаете!!!')
        else:
            print('Норм.')


class SportCar(Car):
    pass


class WorkCar(Car):
    
    def show_speed(self):
        print(f'Текущая скорость {self.speed}', end='\t')
        if self.speed > 40:
            print('Превышаете!!!')
        else:
            print('Норм.')


class PoliceCar(Car):
    pass


TC = TownCar(80, 'Чёрный', 'Toyota', False)
SC = SportCar(120, 'Красный', 'Porshe', False)
WC = WorkCar(35, 'Белый', 'Nissan', False)
PC = PoliceCar(110, 'Белый', 'Shevrolet', True)

TC.show_speed()
SC.show_speed()
WC.show_speed()
PC.show_speed()

SC.turn('налево')
SC.go()
SC.stop()