from tkinter import *
import math

def leftclickbuttun(event):
    x = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    if x>30:
        Labelresult.configure(text="อ้วนมาก!!!")
    elif x>25<30:
        Labelresult.configure(text="อ้วน!")
    elif x>23<25:
        Labelresult.configure(text="น้ำหนักเกิน")
    elif x>18.5<23:
        Labelresult.configure(text="ปกติ")
    elif x<18.6:
        Labelresult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculatebuttun = Button(MainWindow,text="คำนวณ")
calculatebuttun.bind('<Button-1>',leftclickbuttun)
calculatebuttun.grid(row=2,column=0)
Labelresult = Label(MainWindow,text="ผลลัพธ์")
Labelresult.grid(row=2,column=1)

MainWindow.mainloop()
