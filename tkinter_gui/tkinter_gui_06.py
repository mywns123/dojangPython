from tkinter import *
from tkinter import messagebox

# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)

variety1 = IntVar()
variety2 = IntVar()
variety3 = IntVar()


bt1 = Checkbutton(window, text="item1", variable=variety1)
bt2 = Checkbutton(window, text="item2", variable=variety2)
bt3 = Checkbutton(window, text="item3", variable=variety3)

bt1.pack()
bt2.pack()
bt3.pack()


def show():
    messagebox.showinfo("Button Clicked", "item1: {0},\nitem2: {1},\nitem3: {2}\n".format(
        variety1.get(), variety2.get(), variety3.get()))


def selectAll():
    bt1.select()
    bt2.select()
    bt3.select()


def checkClear():
    bt1.deselect()
    bt2.deselect()
    bt3.deselect()


buttonQselect = Button(window, width=10, text="Show", overrelief="solid", command=show)
buttonQselect.pack()

buttonAll = Button(window, width=10, text="전체선택", overrelief="solid", command=selectAll)
buttonAll.pack()

buttonClear = Button(window, width=10, text="전체취소", overrelief="solid", command=checkClear)
buttonClear.pack()

window.mainloop()