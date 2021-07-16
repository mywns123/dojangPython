import tkinter
from tkCamera import tkCamera


class App:
    def __init__(self, window, window_title, video_sources):
        self.window = window
        self.window.title(window_title)

        self.vids = []

        columns = 2
        for number, source in enumerate(video_sources):
            text, stream = source
            vid = tkCamera(self.window, text, stream, 400, 300)
            x = number % columns
            y = number // columns
            vid.grid(row=y, column=x)
            self.vids.append(vid)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def on_closing(self, event=None):
        print("[APP] stoping threads")
        for source in self.vids:
            source.vid.running = False
        print("[APP] exit")
        self.window.destroy()


if __name__ == '__main__':
    sources = [
        ('me', 0),
        ('Zakopane, Poland', 'https://imageserver.webcamera.pl/rec/krupowki-srodek/latest.mp4'),
        ('Kraków, Poland', 'https://imageserver.webcamera.pl/rec/krakow4/latest.mp4'),
        ('Warszawa, Poland', 'https://imageserver.webcamera.pl/rec/warszawa/latest.mp4'),
        # ('Baltic See, Poland', 'https://imageserver.webcamera.pl/rec/chlopy/latest.mp4'),
        # ('Mountains, Poland', 'https://imageserver.webcamera.pl/rec/skolnity/latest.mp4'),
    ]

    App(tkinter.Tk(), "Tkinter and OpenCV", sources)

