# coding: utf-8
# license: GPLv3


class CelestialBody:
    """
    Класс небесного тела.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, type='', m=0, x=0, y=0, vx=0, vy=0, fx=0, fy=0, r=0, color='', name=''):
        self.type = type
        """Признак объекта планеты"""

        self.m = m
        """Масса планеты"""

        self.x = x
        """Координата по оси **x**"""

        self.y = y
        """Координата по оси **y**"""

        self.Vx = vx
        """Скорость по оси **x**"""

        self.Vy = vy
        """Скорость по оси **y**"""

        self.Fx = fx
        """Сила по оси **x**"""

        self.Fy = fy
        """Сила по оси **y**"""

        self.R = r
        """Радиус планеты"""

        self.color = color
        """Цвет планеты"""

        self.name = name
        "Название планеты"

        image = None
        """Изображение планеты"""


class Star(CelestialBody):
    """Тип данных, описывающий звезду.
     Наследование от класса небесного тела
    """
    def __init__(self):
        super().__init__()
        self.R = 5


class Planet(CelestialBody):
    """Тип данных, описывающий планету.
    Наследование от класса небесного тела.
    """
    def __init__(self):
        super().__init__()
