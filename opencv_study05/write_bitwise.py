import cv2

capture = cv2.VideoCapture(0)                       # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")


logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]  # 로고 영상 이진화
masks = cv2.split(masks)
fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)

frame =[]
while True:
    ret, frame = capture.read()
    if frame is None: raise Exception("영상 파일 읽기 오류 발생")
    if(frame !=[]):
        if cv2.waitKey(30) >= 0:
            break

    (H, W), (h, w) = frame.shape[:2], logo.shape[:2]
    x, y = (W - w) // 2, (H - h) // 2
    roi = frame[y:y + h, x:x + w]

    background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)

    dst = cv2.add(background, foreground)
    frame[y:y + h, x:x + w] = dst

    cv2.imshow("View Frame from Camera", frame)

