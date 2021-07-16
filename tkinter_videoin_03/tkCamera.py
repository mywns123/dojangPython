import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from MyVideoCapture import *


class tkCamera(tkinter.Frame):
    def __init__(self, window, text="", video_source=0, width=None, height=None):
        super().__init__(window)
        self.window = window

        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source, width, height)

        self.label = tkinter.Label(self, text=text)
        self.label.pack()

        self.canvas = tkinter.Canvas(self, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        self.btn_snapshot = tkinter.Button(self, text="Start", command=self.start)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, side='left')

        self.btn_snapshot = tkinter.Button(self, text="Stop", command=self.stop)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, side='left')

        self.btn_snapshot = tkinter.Button(self, text="Snapshot", command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, side='left')

        self.delay = int(1000/self.vid.fps)

        print("[tkCamera] source:", self.video_source)
        print("[tkCamera] fps:", self.vid.fps, 'delay:', self.delay)

        self.image = None

        self.running = True
        self.update_frame()

    def start(self):
        if not self.running:
            self.running = True
            self.update_frame()

    def stop(self):
        if self.running:
            self.running = False

    def snapshot(self):
        if self.image:
            self.image.save(time.strftime("frame-%d-%m-%Y-%H-%M-%S.jpg"))

    def update_frame(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.image = PIL.Image.fromarray(frame)
            self.photo = PIL.ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        if self.running:
            self.window.after(self.delay, self.update_frame)