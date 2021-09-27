import threading
import time
import cv2


class MyVideoCapture:
    def __init__(self, text="", video_source=0, width=None, height=None, fps=None):
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
        print("text2:", text)
        if text == "me":
            self.thread = threading.Thread(target=self.process)
        elif text == "Zakopane, Poland":
            self.thread = threading.Thread(target=self.process)
        else:
            self.thread = threading.Thread(target=self.processGray)
        self.thread.start()

    def process(self):

        while self.running:
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (self.width*2, self.height))
                #  컬러사진
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                th = 50
                rep_image = cv2.repeat(frame, 1, 2)  # 가로 반복 복사
                rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
                rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)  # 가우시안 블러링
                rep_edge = cv2.Canny(rep_edge, th, th * 2, 5)  # 캐니 에지 검출
                h, w = frame.shape[:2]
                cv2.rectangle(rep_edge, (0, 0), (w, h), 255, -1)  # 흰색 사각형 그리기

                color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)
                frame = color_edge

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

    def processGray(self):

        while self.running:
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (self.width, self.height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
                frame = cv2.Canny(frame, 100, 150)
            else:
                print("[MyVideoCapture] stream end:", self.video_source)
                self.running = False
                break

            self.ret = ret
            self.frame = frame

            time.sleep(1 / self.fps)


