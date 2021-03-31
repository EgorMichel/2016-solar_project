import numpy as np
import matplotlib.pyplot as plt
import pylab


def equal_size(array1, array2):
    if len(array1) < len(array2):
        temp = []
        temp = array2
        array2 = temp[:-(len(array2) - len(array1))]
        print(len(array1), len(array2))
    if len(array2) < len(array1):
        temp = []
        temp = array1
        array1 = temp[:-(len(array1) - len(array2))]
        print(len(array2), len(array1))
    return array1, array2


def draw_graphics(file_name, mass, ):
    x_star = np.array([])
    y_star = np.array([])
    v_star = np.array([])
    x_planet = np.array([])
    y_planet = np.array([])
    v_planet = np.array([])
    time = np.array([])

    # star.type = line.split()[0]
    # star.R = float(line.split()[1])
    # star.color = line.split()[2]
    # star.m = float(line.split()[3])
    # star.x = float(line.split()[4])
    # star.y = float(line.split()[5])
    # star.Vx = float(line.split()[6])
    # star.Vy = float(line.split()[7])
    with open(file_name) as input_file:
        for line in input_file:
            time = np.append(line.split()[10])
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
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
                        x_planet = np.append(x_planet, float(line.split()[4]))
                        y_planet = np.append(y_planet, float(line.split()[5]))
                        vx = float(line.split()[6])
                        vy = float(line.split()[7])
                        v = (vx ** 2 + vy ** 2)**0.5
                        v_planet = np.append(v_planet, v)

    # if len(x_star) > len(x_planet):
    #     print('sosi2')
    #     temp = []
    #     temp = x_star
    #     x_star = temp[:-(len(x_star) - len(x_planet))]
    #     print(len(x_star), len(x_planet))
    # if len(x_star) < len(x_planet):
    #     print('sosi3')
    #     temp = []
    #     temp = x_planet
    #     x_planet = temp[:-(len(x_planet) - len(x_star))]
    #     print(len(x_star), len(x_planet))
    #
    # if len(y_star) > len(y_planet):
    #     print('sosi4')
    #     temp = []
    #     temp = y_star
    #     y_star = temp[:-(len(y_star) - len(y_planet))]
    #     print(len(y_star), len(y_planet))
    #
    # if len(y_star) < len(y_planet):
    #     print('sosi5')
    #     temp = []
    #     temp = y_planet
    #     y_planet = temp[:-(len(y_planet) - len(y_star))]
    #     print(len(y_star), len(y_planet))

    x_star, x_planet = equal_size(x_star, x_planet)
    y_star, y_planet = equal_size(y_star, y_planet)

    ro = np.sqrt((x_star - x_planet) ** 2 + (y_star - y_planet) ** 2)

    if len(ro) < len(v_planet):
        print("sosi6")
        temp = []
        temp = v_planet
        v_planet = temp[:-(len(v_planet) - len(ro))]
        print(len(ro), len(v_planet))

    if len(ro) > len(v_planet):
        print("sosi7")
        temp = []
        temp = ro
        ro = temp[:-(len(ro) - len(v_planet))]
        print(len(ro), len(v_planet))

    ro, v_planet = equal_size(x_star, x_planet)
    pylab.subplot(221)
    plt.plot(ro, v_planet)

    time, v_planet = equal_size(time, v_planet)
    pylab.subplot(222)
    plt.plot(time, v_planet)

    time, ro = equal_size(time, v_planet)
    pylab.subplot(223)
    plt.plot(time, ro)


    plt.xlabel('Расстояние, м')
    plt.ylabel('Скорость, м/с')
    plt.title('Зависимость скорости спутника \n от расстояния до звезды')
    plt.grid()
    plt.savefig('velocity(distance).png')
    plt.show()
