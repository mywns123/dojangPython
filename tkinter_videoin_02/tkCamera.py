import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from MyVideoCapture import *


class tkCamera(tkinter.Frame):
    def __init__(self, window, video_source=0, width=None, height=None):
        super().__init__(window)
        self.window = window

        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source, width, height)

        self.canvas = tkinter.Canvas(window, width=width, height=height)
        self.canvas.pack()

        self.btn_snapshot = tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        self.delay = 15
        self.update_widget()

    def snapshot(self):
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update_widget(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.image = PIL.Image.fromarray(frame)
            self.photo = PIL.ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update_widget)