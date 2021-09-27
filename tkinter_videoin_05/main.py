import copy
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import threading
import random
import pytesseract
import numpy as np
import pyautogui
import os

from readd import *


class App:

    def __init__(self, window, window_title):
        self.window = window
        self.window.geometry("+1000+0")
        self.window.title(window_title)
        self.frame = None

        self.count = 0
        self.count1 = 0

        self.a = int(1000 / 15)

        self.frame1 = tkinter.Frame(self.window, relief="solid", bd=6)
        self.frame1.grid(row=0, column=0)

        # self.frame2 = tkinter.Frame(self.window, relief="solid", bd=6)
        # self.frame2.grid(row=1, column=0)
        #
        # self.frame3 = tkinter.Frame(self.window, relief="solid", bd=6)
        # self.frame3.grid(row=2, column=0)
        #
        # self.frame4 = tkinter.Frame(self.window, relief="solid", bd=6)
        # self.frame4.grid(row=0, column=1)
        #
        # self.frame5 = tkinter.Frame(self.window, relief="solid", bd=6)
        # self.frame5.grid(row=1, column=1)
        #
        # self.frame6 = tkinter.Frame(self.window, relief="solid", bd=6)
        # self.frame6.grid(row=2, column=1)

        self.vid = readd1()

        self.canvas = tkinter.Canvas(self.frame1, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # self.canvas1 = tkinter.Canvas(self.frame2, width=self.vid.width, height=self.vid.height)
        # self.canvas1.pack()
        #
        # self.canvas2 = tkinter.Canvas(self.frame3, width=self.vid.width, height=self.vid.height)
        # self.canvas2.pack()
        #
        # self.canvas3 = tkinter.Canvas(self.frame4, width=self.vid.width, height=self.vid.height)
        # self.canvas3.pack()
        #
        # self.canvas4 = tkinter.Canvas(self.frame5, width=self.vid.width, height=self.vid.height)
        # self.canvas4.pack()
        #
        # self.canvas5 = tkinter.Canvas(self.frame6, width=self.vid.width, height=self.vid.height)
        # self.canvas5.pack()

        self.delay = int(1000 / 60)

        self.image = None
        self.image1 = None
        self.image2 = None
        self.image3 = None
        self.image4 = None
        self.image5 = None
        self.photo = None
        self.photo1 = None
        self.photo2 = None
        self.photo3 = None
        self.photo4 = None
        self.photo5 = None

        self.running = True
        self.update_frame()
        # self.update_frame5()
        self.window.mainloop()

    def update_frame(self):
        # widgets in tkinter already have method `update()` so I have to use different name -

        # Get a frame from the video source
        self.frame = self.vid.get_frame()

        if self.frame is None:
            pass
        else:
            self.image = PIL.Image.fromarray(self.frame)
            self.photo = PIL.ImageTk.PhotoImage(image=self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor='nw')

            # a1 = copy.deepcopy(self.frame)
            # a1[:,:,1] = 0
            # a1[:, :, 2] = 0
            # self.image1 = PIL.Image.fromarray(a1)
            # self.photo1 = PIL.ImageTk.PhotoImage(image=self.image1)
            # self.canvas1.create_image(0, 0, image=self.photo1, anchor='nw')

            # a2 = copy.deepcopy(self.frame)
            # a2[:, :, 0] = 0
            # a2[:, :, 2] = 0
            # self.image2 = PIL.Image.fromarray(a2)
            # self.photo2 = PIL.ImageTk.PhotoImage(image=self.image2)
            # self.canvas2.create_image(0, 0, image=self.photo2, anchor='nw')
            #
            # a3 = copy.deepcopy(self.frame)
            # a3[:, :, 1] = 0
            # a3[:, :, 0] = 0
            # self.image3 = PIL.Image.fromarray(a3)
            # self.photo3= PIL.ImageTk.PhotoImage(image=self.image3)
            # self.canvas3.create_image(0, 0, image=self.photo3, anchor='nw')
            #
            # a4 = copy.deepcopy(self.frame)
            # a4[:, :, 1] = 0
            # self.image4 = PIL.Image.fromarray(a4)
            # self.photo4 = PIL.ImageTk.PhotoImage(image=self.image4)
            # self.canvas4.create_image(0, 0, image=self.photo4, anchor='nw')
            #
            # a5 = copy.deepcopy(self.frame)
            # a5[:, :, 2] = 0
            # self.image5 = PIL.Image.fromarray(a5)
            # self.photo5 = PIL.ImageTk.PhotoImage(image=self.image5)
            # self.canvas5.create_image(0, 0, image=self.photo5, anchor='nw')

        if self.running:
            self.window.after(self.delay, self.update_frame)

    # def update_frame1(self):
    #     self.frame_vid1 = copy.deepcopy(self.frame)
    #     if self.frame_vid1 is None:
    #         pass
    #     else:
    #         self.image1 = PIL.Image.fromarray(self.frame_vid1)
    #         self.photo1 = PIL.ImageTk.PhotoImage(image=self.image1)
    #         self.canvas1.create_image(0, 0, image=self.photo1, anchor='nw')
    #
    #     if self.running:
    #         self.window.after(self.delay, self.update_frame1)

    # def update_frame2(self):
    #
    #     self.frame_vid2 = copy.deepcopy(self.frame)
    #     if self.frame_vid2 is None:
    #         pass
    #     else:
    #
    #         self.image1 = PIL.Image.fromarray(self.frame_vid2)
    #         self.photo1 = PIL.ImageTk.PhotoImage(image=self.image1)
    #         self.canvas2.create_image(0, 0, image=self.photo1, anchor='nw')
    #
    #     if self.running:
    #         self.window.after(self.delay, self.update_frame2)
    #
    # def update_frame3(self):
    #
    #     self.frame_vid3 = copy.deepcopy(self.frame)
    #     if self.frame_vid3 is None:
    #         pass
    #     else:
    #         self.frame33 = self.frame
    #
    #         self.image1 = PIL.Image.fromarray(self.frame_vid3)
    #         self.photo1 = PIL.ImageTk.PhotoImage(image=self.image1)
    #         self.canvas3.create_image(0, 0, image=self.photo1, anchor='nw')
    #
    #     if self.running:
    #         self.window.after(self.delay, self.update_frame3)
    #
    # def update_frame4(self):
    #
    #     self.frame_vid4 = copy.deepcopy(self.frame)
    #     if self.frame_vid4 is None:
    #         pass
    #     else:
    #         self.frame44 = self.frame
    #
    #         self.image1 = PIL.Image.fromarray(self.frame_vid4)
    #         self.photo1 = PIL.ImageTk.PhotoImage(image=self.image1)
    #         self.canvas4.create_image(0, 0, image=self.photo1, anchor='nw')
    #
    #     if self.running:
    #         self.window.after(self.delay, self.update_frame4)
    #
    # def update_frame5(self):
    #
    #     if self.frame is None:
    #         pass
    #     else:
    #         frame5 = copy.deepcopy(self.frame44)
    #
    #         self.image1 = PIL.Image.fromarray(frame5)
    #         self.photo1 = PIL.ImageTk.PhotoImage(image=self.image1)
    #         self.canvas5.create_image(0, 0, image=self.photo1, anchor='nw')
    #
    #     if self.running:
    #         self.window.after(self.delay, self.update_frame5)

    def callback(self, event):
        print("clicked at", event.x, event.y)

    def snapshot1(self):
        # Get a frame from the video source

        self.count += 1
        cv2.imwrite("frame-" + str(self.count) + ".jpg",
                    cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR))


if __name__ == '__main__':
    App(tkinter.Tk(), "Tkinter and OpenCV")
