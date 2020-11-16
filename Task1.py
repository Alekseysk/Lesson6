"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight():
    __ord_color = ['красный', 'жёлтый', 'зелёный']
    __timers = [7, 2, 4]
    _color = __ord_color[0]
    
    def running(self, color):
        if (color in self.__ord_color) and \
                        (self.__ord_color.index(color) - self.__ord_color.index(self._color)) in [1, -2]:
            ltimer = self.__timers[self.__ord_color.index(self._color)]
            print(f'Please wait {ltimer} seconds, switch to {color} in progress', end='\t')
            sleep(ltimer)
            print(f'... done!')
            self._color = color
        else:
            print('Wrong color or order!!!')
            
            
seen_TL = TrafficLight()

colors = ['красный', 'жёлтый', 'красный', 'жёлтый', 'жёлтый', 'зелёный', 'красный', 'жёлтый', 'зелёный']
for color in colors:
    seen_TL.running(color)