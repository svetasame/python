class Car:
    class_atr = 0

    def __init__(self, label: str, color: str, year: int, audio: str): #функция инициализации
        self.label = label
        self.color = color
        self.year = year
        self.audio = audio
        #селф это значит что мы атрибуты берем у самого объекта

    def drive(self):
        print("Бррррррр")

    def __str__(self):
        return f'Машина марки {self.label} {self.color} цвет {self.year} года выпуска'

my_car = Car("Мазда", "Черный", 2019, "норм")
new_car = Car("Мерседес", "Белый", 2018, "не очень")
old_car = Car("Жигули", "Коричневый", 2000, "более менее")

# print(new_car.label)
print(my_car)
# print(my_car.color)
# print(my_car.year)
# print(my_car.label)


# my_car.drive()

auto_park = [my_car,new_car,old_car]
#
# for car in auto_park:
#     print(car.label)
