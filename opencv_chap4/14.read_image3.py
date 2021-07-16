import cv2
from Common.utils import print_matInfo

title1, title2 = "16bit unchanged", "32bit unchanged"  # 윈도우 이름
color2unchanged1 = cv2.imread("images/read_16.tif", cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread("images/read_32.tif", cv2.IMREAD_UNCHANGED)
if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception("영상파일 읽기 에러")

print("16/32비트 영상 행렬 좌표 (10, 10) 화소값")
print(title1, "원소 자료형 ",  type(color2unchanged1[10][10][0]))   # 원소 좌료형
print(title1, "화소값(3원소) ", color2unchanged1[10, 10] )           # 행렬 내 한 화소 값 표시
print(title2, "원소 자료형 ",  type(color2unchanged2[10][10][0]))
print(title2, "화소값(3원소) ", color2unchanged2[10, 10] )
print()

print_matInfo(title1, color2unchanged1)         # 행렬 정보 출력
print_matInfo(title2, color2unchanged2)
cv2.imshow(title1, color2unchanged1)
cv2.imshow(title2, (color2unchanged2*255).astype("uint8"))
cv2.waitKey(0)