from tkinter import *


# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)


def close():
    window.quit()
    window.destroy()


menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New File")
menu1.add_command(label="Open...")
menu1.add_separator()
menu1.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=True, selectcolor="red")
menu2.add_radiobutton(label="Undo", state="disable")
menu2.add_radiobutton(label="Redo")
menu2.add_radiobutton(label="Cut")
menubar.add_cascade(label="Edit", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_checkbutton(label="Python Shell")
menu3.add_checkbutton(label="Check Module")
menu3.add_checkbutton(label="Run Module")
menubar.add_cascade(label="Run", menu=menu3)

menu4 = Menu(menubar, tearoff=0, selectcolor="red")
menu4.add_checkbutton(label="1")
menu4.add_checkbutton(label="2")
menu4.add_checkbutton(label="3")
menubar.add_cascade(label="Number", menu=menu4)

window.config(menu=menubar)

menubutton = Menubutton(window,text="메뉴 메뉴버튼", relief="raised", direction="right")
menubutton.pack()

menu = Menu(menubutton, tearoff=0)
menu.add_command(label="New File")
menu.add_command(label="Open...")
menu.add_separator()
menu.add_command(label="Exit", command=close)

menubutton["menu"] = menu   # 메뉴버튼과 메뉴를 연결
window.mainloop()
