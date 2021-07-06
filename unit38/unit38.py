# def ten_dev():
#     x = input("숫자 입력")
#     return 10 / x
#
#
# try:
#     print(ten_dev())
# except:
#     print("예외가 발생하였습니다.")


# def get(key, dataset):
#     try:
#         print(key, dataset)
#         value = dataset[key]
#         print(value)
#     except IndexError as ind:
#         print(ind)
#         return "-----"  # 인덱스가 잘못된 예외
#     except KeyError:
#         return "^^^^^"  # 키가 잘못된 예외
#     else:
#         return value
#
#
# print(get(5, (1, 2, 3)))  # 범위를 벗어난 인덱스 인덱싱
# print(get("age", {'name': '박연오'}))  # 사전에 없는 키 인덱싱

# try:
#     x = int(input('3의 배수를 입력하세요'))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)
# except Exception as e:
#     print('예외가 발생했습니다.', e)

# def three_multiple():
#     x = int(input('3의 배수를 입력하세요'))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)
#
#
# try:
#     three_multiple()
# except Exception as e:
#     print('예외가 발생했습니다.', e)


# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요'))
#         if x % 3 != 0:  # x가 3의 배수가 아니면
#             raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴
#         print(x)
#     except Exception as e:  # 함수 안에서 예외를 처리함
#         print("three_multiple 함수에서 예외가 발생했습니다.", e)
#         raise  # raise로 현재 예외를 다시 발생시켜서 상위 코드 불록으로 넘김
#
#
# try:
#     three_multiple()
# except Exception as e:  # 하위 코드 블록에서 예외가 발생해도 실행됨
#     print('스크립트 파일에서 예외가 발생했습니다.', e)


class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

    def testError(self):
        print("예외 클래스 추가기능 >>")


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요'))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        e.testError()


three_multiple()

