from tkinter import *


# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)


bx = 0
by = 0


def selectV(event):
    value = str(scaleH.get()) + "," + str(scaleV.get())
    buttonQselect.config(text=value)
    buttonQselect.place("위치:", x=scaleH.get(), y=scaleV.get())
    labelV.config(text=str(scaleV.get()))


def selectH(event):
    value = str(scaleH.get()) + "," + str(scaleV.get())
    buttonQselect.config(text=value)
    buttonQselect.place("위치:", x=scaleH.get(), y=scaleV.get())
    labelV.config(text=scaleH.get())


def savelocation():
    value = buttonQselect["text"]
    label.config(text=value)


var1 = IntVar()
var2 = IntVar()

scaleV = Scale(window, variable=var1, orient="vertical", showvalue=True, tickinterval=10, to=400, length=200, command=selectV)
scaleV.pack()

labelV = Label(window, text='0')
labelV.pack()


scaleH = Scale(window, variable=var2, orient="horizontal", showvalue=True, tickinterval=10, to=700, length=200, command=selectH)
scaleH.pack()

labelH = Label(window, text='0')
labelH.pack()

buttonQselect = Button(window, width=10, text=str(bx)+","+str(by), command=savelocation)
buttonQselect.place(x=bx, y=by)


label = Label(window, text='0 , 0', borderwidth=3, relief="sunken" )
label.place(x=350, y=350)

window.mainloop()
