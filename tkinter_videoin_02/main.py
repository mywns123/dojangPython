import tkinter
from tkCamera import tkCamera


class App:

    def __init__(self, window, window_title, video_sources):
        self.window = window
        self.window.title(window_title)

        self.vids = []

        for source in video_sources:
            vid = tkCamera(window, source, 400, 300)
            vid.pack()
            self.vids.append(vid)

        self.window.mainloop()


if __name__ == '__main__':
    sources = [
        0,
        # 'https://imageserver.webcamera.pl/rec/krupowki-srodek/latest.mp4',
        # 'https://imageserver.webcamera.pl/rec/skolnity/latest.mp4',
        'https://imageserver.webcamera.pl/rec/krakow4/latest.mp4',
    ]

    App(tkinter.Tk(), "Tkinter and OpenCV", sources)

