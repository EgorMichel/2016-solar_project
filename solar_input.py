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
        star.R = float(line.split()[1])
        star.color = line.split()[2]
        star.m = float(line.split()[3])
        star.x = float(line.split()[4])
        star.y = float(line.split()[5])
        star.Vx = float(line.split()[6])
        star.Vy = float(line.split()[7])
        return star
    elif object_type == "planet":
        planet = Planet()
        planet.type = line.split()[0]
        planet.R = float(line.split()[1])
        planet.color = line.split()[2]
        planet.m = float(line.split()[3])
        planet.x = float(line.split()[4])
        planet.y = float(line.split()[5])
        planet.Vx = float(line.split()[6])
        planet.Vy = float(line.split()[7])
        planet.name = line.split()[10]

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
            mass = [obj.type, str(obj.R), obj.color, str(obj.m), str(obj.x),
                    str(obj.y), str(obj.Vx), str(obj.Vy),
                    str(obj.Fy), str(obj.Fy), obj.name, '\n']
            out_file.writelines(' '.join(mass))
    file = open("Test.txt", "w")
    file.close()


def save_statistics_to_file(file, obj, time):
    """
    Сохранение текущей статистики небесного тела в файл
    param: file: файл для записи данных
    param: obj: объект планеты, данные которой записываются
    param: time: время с начала моделирования движения планет
    """
    mass = [obj.type, str(obj.R), obj.color, str(obj.m), str(obj.x),
            str(obj.y), str(obj.Vx), str(obj.Vy),
            str(obj.Fy), str(obj.Fy), obj.name, str(time), '\n']
    file.writelines(' '.join(mass))


if __name__ == "__main__":
    print("This module is not for direct call!")
