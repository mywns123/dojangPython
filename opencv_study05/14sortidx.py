import numpy as np, cv2

m = np.random.randint(0, 100, 15).reshape(3, 5)           # 임의 난수 생성

m_sort1 = cv2.sortIdx(m, cv2.SORT_EVERY_ROW)        # 행렬 원소의 원본 좌표
m_sort2 = cv2.sortIdx(m, cv2.SORT_EVERY_COLUMN)
m_sort3 = np.argsort(m, axis=0)                         # 세로축 정렬
cv2.imshow("aaaa", m)
print("원본 = \n%s\n" % m)
print("행 정렬 = \n%s\n" % m_sort1)
print("열 정렬 = \n%s\n" % m_sort2)
print("cv2.sort()= \n%s\n" % m_sort3)
