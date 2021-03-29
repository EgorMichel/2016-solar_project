# coding: utf-8
# license: GPLv3
# test
from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            if object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star_massive = line.split()
    for i in range(len(star_massive)):
        if i == 0:
            star.type = star[0]
        if i == 1 or 2 < i <= 7:
            star_massive[i] = int(star_massive[i])
        if i == 2:
            star.color = star[i]
        if i == 1:
            star.R = star_massive[i]
        if i == 3:
            star.m = star_massive[i]
        if i == 4:
            star.x = star_massive[i]
        if i == 5:
            star.y = star_massive[i]
        if i == 6:
            star.Vx = star_massive[i]
        if i == 7:
            star.Vy = star_massive[i]


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet_massive = line.split()
    for i in range(len(planet_massive)):
        if i == 0:
            planet.type = planet[0]
        if i == 1 or 2 < i <= 7:
            planet_massive[i] = int(planet_massive[i])
        if i == 1:
            planet.R = planet_massive[i]
        if i == 2:
            planet.color = planet[i]
        if i == 3:
            planet.m = planet_massive[i]
        if i == 4:
            planet.x = planet_massive[i]
        if i == 5:
            planet.y = planet_massive[i]
        if i == 6:
            planet.Vx = planet_massive[i]
        if i == 7:
            planet.Vy = planet_massive[i]


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
