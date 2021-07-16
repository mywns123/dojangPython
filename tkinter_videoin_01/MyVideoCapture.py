import cv2


class MyVideoCapture:
    def __init__(self, video_source=0, width=None, height=None):
        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError("Unable to open video_source", video_source)

        # self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        # self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = width
        self.height = height

        # if not self.width:
        #     self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        # if not self.height:
        #     self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.resize(frame, (400, 300))
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None

