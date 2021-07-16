from tkinter import *


# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)

frame1 = Frame(window, relief="solid", bd=2)
frame1.pack(side="left", fill="both", expand=True)

frame2 = Frame(window, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=True)

frame3 = Frame(window, relief="solid", bd=2)
frame3.pack(side="left", fill="both", expand=True)

frame3 = Frame(window, relief="solid", bd=2)
frame3.pack(side="right", fill="both", expand=True)

label1 = Label(frame1, text='Hello')
label1.pack()

label2 = Label(frame2, text='World!')
label2.pack()

buttonQselect = Button(frame2, width=10, text="-------", )
buttonQselect.pack()

window.mainloop()
