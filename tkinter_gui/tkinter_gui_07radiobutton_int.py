from tkinter import *
from tkinter import messagebox

# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)

variety1 = IntVar()
variety2 = IntVar()

bt1 = Radiobutton(window, text="item1", variable=variety1, value=1)
bt2 = Radiobutton(window, text="item2", variable=variety1, value=2)
bt3 = Radiobutton(window, text="item3", variable=variety2, value=3)
bt4 = Radiobutton(window, text="item4", variable=variety2, value=4)

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()


def show():
    messagebox.showinfo("Button Clicked", "item1: {0},\nitem2: {1}".format(variety1.get(), variety2.get()))


buttonQselect = Button(window, width=10, text="Show", overrelief="solid", command=show)
buttonQselect.pack()

window.mainloop()