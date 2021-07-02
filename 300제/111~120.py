print("# 111번문제")
x = input()
print(x*2)
print("# 112번문제")
x = int(input())
print(x+10)
print("# 113번문제")
x = int(input())
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

print("# 114번문제")
x = int(input()) + 20
if x > 255:
    print(255)
else:
    print(x)
print("# 115번문제")
x = int(input()) - 20
if x > 255:
    print(255)
elif x < 0:
    print(0)
else:
    print(x)
print("# 116번문제")
x = input("현재시간:")
y = x.split(":")
print(y)
if y[1] == 00:
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
print("# 117번문제")
fruit = ["사과", "포도", "홍시"]
x = input("좋아하는 과일은?")
if x in fruit:
    print("정답입니다.")
print("# 118번문제")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
x = input("")
if x in warn_investment_list:
    print("투자 경고 종목이 아닙니다.")
print("# 119번문제")
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
x = input("좋아하는 계절은?")
if x in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
print("# 120번문제")
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
x = input("좋아하는 과일은?")
if x in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")