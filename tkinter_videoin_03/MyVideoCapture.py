import threading
import time

import cv2


class MyVideoCapture:
    def __init__(self, video_source=0, width=None, height=None, fps=None):
        self.video_source = video_source
        self.width = width
        self.height = height
        self.fps = fps

        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video_source", video_source)

        if not self.width:
            self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        if not self.height:
            self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if not self.fps:
            self.fps = int(self.vid.get(cv2.CAP_PROP_FPS))

        self.ret = False
        self.frame = None

        self.running = True
        self.thread = threading.Thread(target=self.process)
        self.thread.start()

    def process(self):
        while self.running:
            ret, frame = self.vid.read()

            if ret:
                frame = cv2.resize(frame, (self.width, self.height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                print("[MyVideoCapture] stream end:", self.video_source)
                self.running = False
                break

            self.ret = ret
            self.frame = frame

            time.sleep(1/self.fps)

    def get_frame(self):
        return self.ret, self.frame

    def __del__(self):
        if self.running:
            self.running = False
            self.thread.join()

        if self.vid.isOpened():
            self.vid.release()

