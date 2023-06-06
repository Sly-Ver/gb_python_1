# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.


from itertools import cycle
from time import sleep


class TrafficLight:
    __color = cycle([
        {'signal': 'Красный', 'duration': 7},
        {'signal': 'Желтый', 'duration': 2},
        {'signal': 'Зеленый', 'duration': 4},
        {'signal': 'Желтый', 'duration': 2}
    ])

    def running(self):
        light = next(self.__color)
        print(f"Сигнал {light['signal']}, пауза {light['duration']} сек.")
        sleep(light['duration'])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()