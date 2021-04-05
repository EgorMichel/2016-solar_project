import numpy as np
import matplotlib.pyplot as plt
import pylab


def equal_size(array1, array2):
    """
    Приведение двух массивов к одному размеру
    param: array1:
    param: array2:
    return: два массива одинаковых размеров
    """
    if len(array1) > len(array2):
        temp = []
        temp = array1
        array1 = temp[:-(len(array1) - len(array2))]
    elif len(array2) > len(array1):
        temp = []
        temp = array2
        array2 = temp[:-(len(array2) - len(array1))]
    return array1, array2


def draw_graphics(file_name, mass):
    """
    Рисует графики, считывая данные из файла
    param: file_name: имя файла для чтения данных
    param: mass: масса планеты, для которой строится график
    """
    x_star = np.array([])
    y_star = np.array([])
    v_star = np.array([])
    x_planet = np.array([])
    y_planet = np.array([])
    v_planet = np.array([])
    time = np.array([])
    name = ''

    with open(file_name) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            if len(line) < 140:
                continue
            else:
                if line.split()[0] == "Star":
                    x_star = np.append(x_star, float(line.split()[4]))
                    y_star = np.append(y_star, float(line.split()[5]))
                    vx = float(line.split()[6])
                    vy = float(line.split()[7])
                    v = (vx**2 + vy**2)**0.5
                    v_star = np.append(v_star, v)

                if line.split()[0] == "Planet":
                    if float(line.split()[3]) == mass:
                        time = np.append(time, float(line.split()[11]))
                        name = line.split()[10]
                        x_planet = np.append(x_planet, float(line.split()[4]))
                        y_planet = np.append(y_planet, float(line.split()[5]))
                        vx = float(line.split()[6])
                        vy = float(line.split()[7])
                        v = (vx ** 2 + vy ** 2)**0.5
                        v_planet = np.append(v_planet, v)

    x_star, x_planet = equal_size(x_star, x_planet)
    y_star, y_planet = equal_size(y_star, y_planet)

    ro = np.sqrt((x_star - x_planet) ** 2 + (y_star - y_planet) ** 2)

    plt.figure(figsize=(30, 10))

    ro, v_planet = equal_size(ro, v_planet)
    pylab.subplot(221)
    plt.plot(ro, v_planet)

    plt.xlabel('Distance, m')
    plt.ylabel('Velocity, m/s')
    plt.title('Dependence of the velocity of ' + name + '\n on the distance to the Star')
    plt.grid()

    time, v_planet = equal_size(time, v_planet)
    pylab.subplot(222)
    plt.plot(time, v_planet)

    plt.xlabel('Time, s')
    plt.ylabel('Velocity, m/s')
    plt.title('Dependence of the velocity of ' + name + '\n on the time')
    plt.grid()

    time, ro = equal_size(time, ro)
    pylab.subplot(223)
    plt.plot(time, ro)

    plt.xlabel('Time, m')
    plt.ylabel('Distance, m/s')
    plt.title('Dependence of the distance to the Star of ' + name + '\n on the time')
    plt.grid()

    plt.subplots_adjust(hspace=0.5, wspace=0.5)

    plt.savefig('graphics.png')
    plt.show()
