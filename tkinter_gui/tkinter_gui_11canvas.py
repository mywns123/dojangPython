from tkinter import *


# 창 띄우기
window = Tk()
window.title("영남인재 교육원")
window.geometry("800x500+100+100")
window.resizable(False, False)

canvas = Canvas(window, width=200, height=150, bg="white", bd=2)
canvas.pack(fill="both", expand=True)
canvas.pack()

canvas.create_line(0, int(200/2), 100, int(200/2), fill="blue")

window.mainloop()
