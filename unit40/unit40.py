def number_generator():
    yield 0
    yield 1
    yield 2


# for i in number_generator():
#     print(i)

# g = number_generator()
# print(dir(g))
#
# gg = iter(g)
# print(next(gg))
# print(next(gg))
# print(next(gg))
class A:
    def test(self):
        print("----")


def num_gen(x):
    yield from x


a = A()
b = A()
c = A()

x = [a, b, c]

for i in num_gen(x):
    i.test()