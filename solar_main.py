# coding: utf-8
# license: GPLv3

import tkinter
import tkinter.filedialog
import solar_vis
import solar_model
import solar_input
import Show_statistics

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""

Scale = 0

file_name = "Test.txt"
file = open(file_name, "w")
file.close()

file = open(file_name, "a+")


def click(event):
    """
    Обработка нажатия на планету
    """
    for obj in space_objects:
        if obj.type == "Planet":
            x = int(obj.x * Scale) + solar_vis.window_width//2
            y = solar_vis.window_height//2 - int(obj.y*Scale)
            if (event.x - x) ** 2 + (event.y - y) ** 2 < obj.R ** 2:
                Show_statistics.draw_graphics(file_name, obj.m)


def execution():
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    global displayed_time
    solar_model.recalculate_space_objects_positions(space_objects, time_step.get())
    for body in space_objects:
        solar_vis.update_object_position(space, body)
        solar_input.save_statistics_to_file(file, body, float(displayed_time.get()[:-13]))

    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")

    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    print('start')
    global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution

    execution()
    print('Started execution...')


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')


def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global perform_execution
    global Scale

    perform_execution = False
    for obj in space_objects:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = tkinter.filedialog.askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = solar_input.read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])

    Scale = solar_vis.calculate_scale_factor(max_distance)

    for obj in space_objects:
        if obj.type == 'Star':
            solar_vis.create_star_image(space, obj)
        elif obj.type == 'Planet':
            solar_vis.create_planet_image(space, obj)
        else:
            print(obj.type)
            raise AssertionError()

    filel = open("Test.txt", "w")
    filel.close()


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    out_filename = tkinter.filedialog.asksaveasfilename(filetypes=(("Text file", ".txt"),))
    solar_input.write_space_objects_data_to_file(out_filename, space_objects)


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=solar_vis.window_width, height=solar_vis.window_height, bg="black")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    space.bind('<1>', click)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(10)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()
    print('Modelling finished!')


if __name__ == "__main__":
    main()
