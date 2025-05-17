from threading import Thread
import PySimpleGUIQt as sg
import pymem
import ctypes
import mem_edit
import PySide2

adress = [0]
adresaDlyaOtseva = []


def scan():
    pm = pymem.Pymem(values[0])
    value = pm.read_int(int(values[1], 0))
    print('Значение адреса ' + str(values[1]) + ' = ' + str(value))


def chagne():
    pm = pymem.Pymem(values[0])
    pm.write_int(int(values[2], 0), int(values[3]))
    print('Значение у адреса ' + str(values[2]) + ' изменено на ' + str(values[3]))


def getadress():
    global adress
    pid = mem_edit.Process.get_pid_by_name(values[0])
    with mem_edit.Process.open_process(pid) as p:
        adress = p.search_all_memory(ctypes.c_int(int(values[4])))
        print('Найдено', len(adress), 'адресов')


def sort():
    adresaDlyaOtseva.clear()
    pm = pymem.Pymem(values[0])
    for odinAdres in adress:
        if pm.read_int(odinAdres) == int(values[5]):
            adresaDlyaOtseva.append(odinAdres)
    print('Адресов найдено:', len(adresaDlyaOtseva))
    adress.clear()
    for i in adresaDlyaOtseva:
        adress.append(i)


sg.theme('DarkGrey6')
layout = [
    [sg.Text('Наименование процесса(notepad.exe):   '), sg.InputText('')],  # values 0

    [sg.InputText('')],  # values 1
    [sg.Button('Получить значение адреса')],

    [sg.Text('Заменить значение адреса', text_color='white')],
    [sg.Text('Адрес:   '), sg.InputText('')],  # values 2
    [sg.Text('Значение:   '), sg.InputText('')],  # values 3
    [sg.Button('Заменить')],

    [sg.Text('Получить адреса с значением:   '), sg.InputText('')],  # values 4
    [sg.Button('Получить')],

    [sg.Text('Отсортировать с изменённым значением: '), sg.InputText('')],  # values 5
    [sg.Button('Отсортировать')], [sg.Button('Вывести адреса')],

]
window = sg.Window('Гипербола', layout)
while True:
    global string
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Выйти':
        break

    if event == "Вывести адреса":
        for xuita in adresaDlyaOtseva:
            print(hex(xuita))

    if event == "Получить значение адреса":
        Thread(target=scan).start()

    if event == "Отсортировать":
        Thread(target=sort).start()

    if event == "Получить":
        Thread(target=getadress).start()

    if event == "Заменить":
        Thread(target=chagne).start()

print()