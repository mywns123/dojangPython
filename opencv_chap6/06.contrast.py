import numpy as np, cv2

image = cv2.imread("images/contrast.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

noimage = np.zeros(image.shape[:2], image.dtype)        # 더미 영상
avg = cv2.mean(image)[0]/2.0                            # 영상 화소 평균의 절반
print(cv2.mean(image))
print(cv2.mean(image)[0])
print(cv2.mean(image)[0]/2.0)

dst1 = cv2.scaleAdd(image, 0.2, noimage) + 20               # 영상대비 감소
dst2 = cv2.scaleAdd(image, 2.0, noimage)                # 영상대비 증가
dst3 = cv2.addWeighted(image, 0.5, noimage, 0, avg)     # 명암대비 감소
dst4 = cv2.addWeighted(image, 2.0, noimage, 0,-avg)     # 명암대비 증가

# 영상 띄우기
cv2.imshow("image", image)
cv2.imshow("dst1 - decrease contrast", dst1)
cv2.imshow("dst2 - increase contrast", dst2)
cv2.imshow("dst3 - decrease contrast using average", dst3)
cv2.imshow("dst4 - increase contrast using average", dst4)

cv2.imwrite("dst.jpg",dst1)
cv2.waitKey(0)


