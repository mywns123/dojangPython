import cv2


class VideoWriterWidget(object):
    def __init__(self, video_file_name, src=0):
        self.frame_name = str(src)
        self.video_file = video_file_name
        self.video_file_name = video_file_name + '.avi'
        self.capture = cv2.VideoCapture(src)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))
        self.codec = cv2.VideoWriter_fourcc("M", "J", "P", "G")
        self.output_video = cv2.VideoWriter(self.video_file_name, self.codec, 30, (self.frame_width, self.frame_height))


    def update(self):
        pass

    def seve_frame(self):
        pass

    def start_recording(self):
        pass


if __name__=='__main__':
    src1 = "Your link1"
    video_writer_widget1 = VideoWriterWidget('camera1', src1)