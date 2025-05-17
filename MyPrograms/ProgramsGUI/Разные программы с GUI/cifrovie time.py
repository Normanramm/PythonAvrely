import datetime
import math
import tkinter
import time

window = tkinter.Tk()
window.title('часы')
canvas = tkinter.Canvas(window, width=200, height=200)
canvas.pack()
hours=canvas.create_text(100, 100, text='', font=('Arial', 30)) #Нужно для работы цифровых часов и проверки ботом, если не нужны, можно закоментировать
Sarrow=canvas.create_line(100, 100, 100, 10, fill='black')
Marrow=canvas.create_line(100, 100, 100, 20, fill='black', width=3)
Harrow=canvas.create_line(100, 100, 100, 30, fill='black', width=5)

for i in range (1,13):
    x=math.ceil(90*math.sin(i/6*math.pi))
    y=math.ceil(90*math.cos(i/6*math.pi))
    canvas.create_text(100+x, 100-y, text=i, fill='black', font=('Arial', 20))  #Для проверки ботом закоментировать

pi = math.pi

while True:
    rcnt_time=datetime.datetime.now()
    time_=rcnt_time.strftime("%X")      #Нужно для работы цифровых часов и проверки ботом, если не нужны, можно закоментировать

    scnds=rcnt_time.second+rcnt_time.microsecond/1000000
    mints=rcnt_time.minute+scnds/60
    hrs=rcnt_time.hour+mints/60


    Hx=round(70*math.sin(hrs/6*pi))
    Hy=round(70*math.cos(hrs/6*pi))
    Mx=round(80*math.sin(mints/30*pi))
    My=round(80*math.cos(mints/30*pi))
    Sx=round(90*math.sin(scnds/30*pi))
    Sy=round(90*math.cos(scnds/30*pi))
    canvas.itemconfig(hours, text=time_)    #Нужно для работы цифровых часов и проверки ботом, если не нужны, можно закоментировать
    canvas.coords(Harrow, 100, 100, 100+Hx, 100-Hy)
    canvas.coords(Marrow, 100, 100, 100+Mx, 100-My)
    canvas.coords(Sarrow, 100, 100, 100+Sx, 100-Sy)
    canvas.update()
#    time.sleep(1-rcnt_time.microsecond/1000000) #sleep с синхронизацией по микросекундам раскомментировать если плавный ход не нужен
#    time.sleep(0.05)

