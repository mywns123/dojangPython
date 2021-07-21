import threading
import time
import cv2
import numpy as np
from Common.histogram import draw_histo, draw_histo_hue


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
        elif text == "histogram":
            self.thread = threading.Thread(target=self.processhistogram)
        elif text == "Zakopane, Poland":
            self.thread = threading.Thread(target=self.processGray)
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
                # dst2 = cv2.equalizeHist(frame)
                # hist2 = cv2.calcHist([dst2], [0], None, bins, ranges)
                # hist_img2 = draw_histo(hist2)
                # cv2.imshow("OpenCV_hist", hist_img2)
                #  흑백사진
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
                # white = np.array([255, 255, 255], np.uint8)
                # CMY_img = white - frame
                # CMY = cv2.split(CMY_img)
                # frame = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))
                
                #  리플라시안 에지
                # frame = cv2.Laplacian(frame, cv2.CV_16S, 1)
                th = 50
                rep_image = cv2.repeat(frame, 1, 2)  # 가로 반복 복사
                rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)  # 명암도 영상 변환
                rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)  # 가우시안 블러링
                rep_edge = cv2.Canny(rep_edge, th, th * 2, 5)  # 캐니 에지 검출
                h, w = frame.shape[:2]
                cv2.rectangle(rep_edge, (0, 0), (w, h), 255, -1)  # 흰색 사각형 그리기

                color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)
                frame=color_edge


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

    def processhistogram(self):

        while self.running:
            ret, frame = self.vid.read()
            hsize, ranges = [32], [0, 256]
            if ret:
                frame = cv2.resize(frame, (self.width, self.height))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                frame = cv2.calcHist([frame], [0], None, [18], [0, 180])
                frame = draw_histo_hue(frame, (200, 360, 3))
            else:
                print("[MyVideoCapture] stream end:", self.video_source)
                self.running = False
                break

            self.ret = ret
            self.frame = frame

            time.sleep(1 / self.fps)

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

    def make_palette(rows):
        # 리스트 생성 방식
        hue = [round(i * 180 / rows) for i in range(rows)]  # hue 값 리스트 계산
        hsv = [[(h, 255, 255)] for h in hue]  # (hue, 255,255) 화소값 계산
        hsv = np.array(hsv, np.uint8)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    def draw_histo_hue(hist, shape=(200, 256, 3)):
        hsv_palate = hist.make_palette(hist.shape[0])  # 색상 팔레트 생성
        hist_img = np.full(shape, 255, np.uint8)
        cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)  # 정규화

        gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기
        for i, h in enumerate(hist):
            x, w = int(round(i * gap)), int(round(gap))
            color = tuple(map(int, hsv_palate[i][0]))  # 정수형 튜플로 변환
            cv2.rectangle(hist_img, (x, 0, w, int(h)), color, cv2.FILLED)  # 팔레트 색으로 그리기

        return cv2.flip(hist_img, 0)