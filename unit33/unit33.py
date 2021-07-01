x = 10
print(x)  # 10


def foo():
    print(x)


foo()  # 10
x = 20
foo()  # 20
print(x)  # 20


def print_hello():
    hello = "Hello, world!"

    def print_message():
        print(hello)

    print_message()


print_hello()

x = 10
print("전역 x:", x)


def foo():
    print("foo()x", x)
    y = 20

    def koo():
        nonlocal y
        print("foo()y", y)
        y = 30
        print("koo()y", y)
        global x
        print("foo()x", x)
        x = 40
        print("koo()x", x)

    koo()


foo()
print("전역 x:", x)


def A():
    x = 10
    y = 100

    def B():
        x = 20
        # y = 100
        print(locals())

        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
            print(locals())

        C()

    B()


A()
print(locals())

x = 1


def A():
    x = 10
    print('A:', x)

    def B():
        x = 20
        print('B:', x)

        def C():
            global x
            x = x + 100
            print('C:', x)

        C()

    B()


print('1:', x)
A()
print('2:', x)


def calc():
    a = 3
    b = 5

    def mul_add(x):
        c = a * x + b
        return c

    return mul_add


dd = calc()  # mul_add(x)
print('dd', dd(8))




