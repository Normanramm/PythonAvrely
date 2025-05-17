# Python program to test
# internet speed
#auto-py-to-exe через это делается запуск в файл
#pyinstaller название файла --one file                    pyinstaller main.py --one file
#-F #создать исполняемый файл в один файл
#-n # задать имя файлу
#--icon=name.ico # присвоить иконку для .exe  (где name - имя картинки)
#-w # отключить консольное окно

import tkinter
from tkinter import *
import speedtest
import tkinter.messagebox

option = ''


def downloadSpeed():
    global option
    option = 'скорость загрузки'
    showSpeed()


def uploadSpeed():
    global option
    option = 'скорость отдачи'
    showSpeed()


def ping():
    global option
    option = 'скорость пинга'
    showSpeed()


def showSpeed():
    global option
    st = speedtest.Speedtest()
    if option == 'скорость загрузки':
        speed = (st.download())

    elif option == 'скорость отдачи':

        speed = (st.upload())

    elif option == 'скорость пинга':

        servernames = []

        st.get_servers(servernames)

        speed = (st.results.ping)
    speedWithUnits = ''
    if (speed < 1000):
        speedWithUnits = str(round(speed, 3)) + " bps"
    elif (speed < 1000000):
        speedWithUnits = str(round(speed / 1000, 3)) + " Kbps"
    elif (speed < 1000000000):
        speedWithUnits = str(round(speed / 1000000, 3)) + " Mbps"
    else:
        speedWithUnits = str(round(speed / 1000000000, 3)) + " Gbps"

    # print( "Hi! Your" +option+" Speed is:"+speedWithUnits)
    tkinter.messagebox.showinfo("Тестер скорости AVI", "Привет! Твоя " + option + " вот такая:" + speedWithUnits)


# Creating the main window
wn = tkinter.Tk()
wn.title("Тестер скорости интернета АVI")
wn.geometry('700x300')
wn.config(bg='azure')

Label(wn, text='Я тестер скорости интернета AVI,выбери нужную опцию', bg='azure',
      fg='black', font=('Courier', 15)).place(x=40, y=10)

Label(wn, text='При выборе опции нужно подождать для получения результата!', bg='azure',
      fg='black', font=('Courier', 12)).place(x=20, y=40)

# Button to convert Audio to PDF form
Button(wn, text="Скорость загрузки", bg='ivory3', font=('Courier', 15), width=20,
       command=downloadSpeed).place(x=230, y=80)

# Button to Check Upload Speed
Button(wn, text="Скорость отдачи", bg='ivory3', font=('Courier', 15), width=20,
       command=uploadSpeed).place(x=230, y=150)

# Button to convert Audio to PDF form
Button(wn, text="Пинг", bg='ivory3', font=('Courier', 15), width=20,
       command=ping).place(x=230, y=220)

# Runs the window till it is closed
wn.mainloop()
