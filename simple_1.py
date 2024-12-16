# Простой уровень:
# 1) Создайте класс Car, который имеет атрибуты make (марка) и model (модель). Реализуйте метод display_info(), который выводит информацию о марке и модели автомобиля.
# 2) Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота). Реализуйте метод calculate_area(), который возвращает площадь прямоугольника.


class Car:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Марка: {self.make}\nМодель: {self.model}")


class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def calculate_area(self) -> int | float:
        return self.width * self.height
