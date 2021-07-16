import numpy as np, cv2

m = np.random.rand(3,5) * 1000//10  # 0~100미만의 난수

reduce_sum1 = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_SUM) # 0 - 열방향 축소
reduce_sum2 = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_SUM) # 1 - 행방향 축소
reduce_avg = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_AVG) # 1 - 행방향 축소
reduce_max = cv2.reduce(m, dim=0, rtype=cv2.REDUCE_MAX)
reduce_min = cv2.reduce(m, dim=1, rtype=cv2.REDUCE_MIN)

print("[m1] = \n%s\n" %m)

print("[m_reduce_sum1] =", reduce_sum1.flatten())
print("[m_reduce_sum2] =", reduce_sum2.flatten())
print("[m_reduce_avg] =", reduce_avg.flatten())
print("[m_reduce_max] =", reduce_max.flatten())
print("[m_reduce_min] =", reduce_min.flatten())
