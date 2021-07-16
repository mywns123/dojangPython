from tkinter import *
from tkinter import messagebox

# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)

variety1 = StringVar(value="영어")

bt1 = Radiobutton(window, text="국어", variable=variety1, value="국어")
bt2 = Radiobutton(window, text="영어", variable=variety1, value="영어")
bt3 = Radiobutton(window, text="수학", variable=variety1, value="수학")
bt4 = Radiobutton(window, text="과학", variable=variety1, value="과학")

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()


def show():
    messagebox.showinfo("Button Clicked", "item1: {0}\n".format(variety1.get()))


buttonQselect = Button(window, width=10, text="Show", overrelief="solid", command=show)
buttonQselect.pack(side="bottom")

window.mainloop()