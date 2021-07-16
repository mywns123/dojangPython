import tkinter
from math import *

# 창 띄우기
window = tkinter.Tk()
window.title("영남인재 교육원")
window.geometry("800x1000+100+100")
window.resizable(False, False)

count = 0


def countUP():
    global count
    count += 1
    label1.config(text=str(count))


def countDown():
    global count
    count -= 1
    label1.config(text=str(count))


def calc(event):
    print("##",entry.get() )
    label1.config(text="결과="+str(eval(entry.get())))


label = tkinter.Label(window, anchor="ne", text="안녕하세요.", width=10, height=5, fg="red", relief="solid", bg="blue")
label.pack()

button = tkinter.Button(window, text="+", overrelief="solid", width=15, command=countUP,
                        repeatdelay=1000, repeatinterval=100)
button.pack()

button = tkinter.Button(window, text="-", overrelief="solid", width=15, command=countDown,
                        repeatdelay=1000, repeatinterval=100)
button.pack()

entry = tkinter.Entry(window)
entry.bind("<Return>", calc)
entry.pack()

label1 = tkinter.Label(window)
label1.pack()


def getEntry11():
    return entry11.get()


def getEntry12():
    return entry12.get()


def pluse():
    a = int(getEntry11()) + int(getEntry12())
    entry13.config(text="결과=" + str(a))


def entryBox(event):
    ent = entry21.get()
    txt.insert(tkinter.END, '\n'+ent)
    entry21.delete(0, tkinter.END)


photo = tkinter.PhotoImage(file="")

entry11 = tkinter.Entry(window)
entry11.pack()
entry12 = tkinter.Entry(window)
entry12.pack()
entry13 = tkinter.Label(window)
entry13.pack()
button11 = tkinter.Button(window, command=pluse, text="더하기", width=100, image=photo, height=50)
button11.bind("<Button-1>")
button11.pack()

entry21 = tkinter.Entry(window)
entry21.place(x=10, y=10, width=30, height=100)
entry21.bind("<Return>", entryBox)
entry21.pack()


txt = tkinter.Text(window, width=30, height=20)
txt.insert(tkinter.END, "글자를 입력하세요")
txt.pack()

listbox = tkinter.Listbox(window, selectmode="extended", height=0)
listbox.insert(0, "대한민국")
listbox.insert(1, "만만세!!")
listbox.insert(2, "동해물과")
listbox.insert(3, "백두산이")
listbox.insert(tkinter.END, "마르고")
listbox.pack()


def btncmd():
    # print(listbox.get(0, 2))
    # print(listbox.curselection()[0])
    print(listbox.get(listbox.curselection()[0]))
    # listbox.delete(tkinter.END)
    entry21.insert(0, listbox.get(listbox.curselection()[0]))
    # entry21.config(text=listbox.get(listbox.curselection()[0]))
    # txt.config(text=listbox.get(listbox.curselection()[0]))


btn11 = tkinter.Button(window, text="삭제", command=btncmd)
btn11.pack()


window.mainloop()
