# coding: utf-8
# license: GPLv3


class Celestial_Body:
    """
    Класс небесного тела.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    def __init__(self, type='', m=0, x=0, y=0, Vx=0, Vy=0, Fx=0, Fy=0, R=0, color='', name=''):
        self.type = type
        """Признак объекта планеты"""

        self.m = m
        """Масса планеты"""

        self.x = x
        """Координата по оси **x**"""

        self.y = y
        """Координата по оси **y**"""

        self.Vx = Vx
        """Скорость по оси **x**"""

        self.Vy = Vy
        """Скорость по оси **y**"""

        self.Fx = Fx
        """Сила по оси **x**"""

        self.Fy = Fy
        """Сила по оси **y**"""

        self.R = R
        """Радиус планеты"""

        self.color = color
        """Цвет планеты"""

        self.name = name
        "Название планеты"

        image = None
        """Изображение планеты"""


class Star(Celestial_Body):
    """Тип данных, описывающий звезду.
     Наследование от класса небесного тела
    """
    def __init__(self):
        super().__init__()
        self.R = 5


class Planet(Celestial_Body):
    """Тип данных, описывающий планету.
    Наследование от класса небесного тела.
    """
    def __init__(self):
        super().__init__()
