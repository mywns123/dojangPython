# import hello
# import calcpkg.geometry as cgo
# import calcpkg.operation as cop
from calcpkg import *


def main():
    print("모듈 시작")
    print("hello.py __name__:", __name__)
    print("모듈 끝")


if __name__ == '__main__':
    main()
# cop.add(3, 4)
# print(cgo.triangle_area(10, 20))

add(4, 5)
print(rectangle_area(4, 6))
mul(4, 4)
print(dir())

