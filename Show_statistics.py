import numpy as np
import matplotlib.pyplot as plt
import math


def draw_graphics(file_name):
    x_star = np.array([])
    y_star = np.array([])
    v_star = np.array([])
    x_planet = np.array([])
    y_planet = np.array([])
    v_planet = np.array([])
    time_star = np.array([])
    time_planet = np.array([])

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
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            if len(line) < 140:
                pass
            else:
                if line.split()[0] == "Star":
                    print(line)
                    x_star = np.append(x_star, float(line.split()[4]))
                    y_star = np.append(y_star, float(line.split()[5]))
                    vx = float(line.split()[6])
                    vy = float(line.split()[7])
                    v = math.sqrt(vx**2 + vy**2)
                    v_star = np.append(v_star, v)
                    # time_star = np.append(time_star, float(line[4]))

                if line.split()[0] == "Planet":
                    print(line)
                    x_planet = np.append(x_star, float(line.split()[4]))
                    y_planet = np.append(y_star, float(line.split()[5]))
                    vx = float(line.split()[6])
                    vy = float(line.split()[7])
                    v = math.sqrt(vx ** 2 + vy ** 2)
                    v_planet = np.append(v_planet, v)
    if len(x_star) != len(x_planet) or len(y_star) != len(y_planet):
        np.resize(x_star, len(x_planet))
        np.resize(y_star, len(y_planet))
    ro = np.sqrt((x_star - x_planet) ** 2 + (y_star - y_planet) ** 2)
    plt.plot(ro, v_planet)
    plt.xlabel('Расстояние, м')
    plt.ylabel('Скорость, м/с')
    plt.title('Зависимость скорости спутника \n от расстояния до звезды')
    plt.grid()
    plt.savefig('velocity(distance).png')
    plt.show()
