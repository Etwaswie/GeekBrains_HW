# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __add__(self, other):
        return f'{self.name} уже выехала за {other.name}'

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}.')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости машины {self.name} на {self.speed - 60} км/ч!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости машины {self.name} на {self.speed - 40} км/ч!')

class PoliceCar(Car):
    pass

bobik = PoliceCar(70, 'grey', 'Bobik', True)
bobik.go()
bobik.show_speed()
bobik.turn('налево')

kamaz = WorkCar(80, 'yellow', 'Kamaz', False)
kamaz.show_speed()
kamaz.turn('налево')

print(bobik + kamaz)

kia = TownCar(65, 'red', 'Kia Rio', False)
kia.show_speed()
