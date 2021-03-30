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
            objects.append(parse_parameters(line))

    return objects


def parse_parameters(line):
    """Считывает данные о небесном теле из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание небесного тела.
    **star** — объект.
    """
    object_type = line.split()[0].lower()
    if object_type == "star":
        star = Star()
        star.type = line.split()[0]
        star.R = int(line.split()[1])
        star.color = line.split()[2]
        star.m = line.split()[3].format(float)
        star.x = line.split()[4].format(float)
        star.y = line.split()[5].format(float)
        star.Vx = line.split()[6].format(float)
        star.Vy = line.split()[7].format(float)
        return star
    elif object_type == "planet":
        planet = Planet()
        planet.type = line.split()[0]
        planet.R = int(line.split()[1])
        planet.color = line.split()[2]
        planet.m = line.split()[3].format(float)
        planet.x = line.split()[4].format(float)
        planet.y = line.split()[5].format(float)
        planet.Vx = line.split()[6].format(float)
        planet.Vy = line.split()[7].format(float)
        return planet
    else:
        print("Unknown space object")


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
            mass = [obj.type, obj.R, obj.color, obj.mass, obj.x, obj.y, obj.Vx, obj.Vy, obj.Fy, obj.Fy]
            out_file.writelines(' '.join(mass))


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
