# print("# 121번문제")
# x = input()
# if x.islower():
#     print(x.upper())
# else:
#     print(x)
#     x.upper()
# print("# 122번문제")
# x = int(input("score:"))
# if 81 <= x <= 100:
#     print("grade is A")
# elif 61 <= x <= 80:
#     print("grade is B")
# elif 41 <= x <= 60:
#     print("grade is C")
# elif 21 <= x <= 40:
#     print("grade is D")
# else:
#     print("grade is E")
# print("# 123번문제")
# 환율 = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
# x = input("입력:")
# y = x.split()
# a = (float(y[0]) * 환율[y[1]])
# print(a, "원")
# num, currency = x.split()
# print(float(num) * 환율[currency], "원")
# print("# 124번문제")
# a = int(input("input number1: "))
# b = int(input("input number2: "))
# c = int(input("input number3: "))
# print(max(a, b, c))
# print("# 125번문제")
#
# print("# 126번문제")
#
# print("# 127번문제")
#
# print("# 128번문제")

# print("# 129번문제")
# x = input("주민등록번호:")
# y = x.replace("-", "")
# print(y[0])
print("# 130번문제")
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)
