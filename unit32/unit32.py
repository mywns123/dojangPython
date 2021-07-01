la = lambda x: x + 10
print('la', la(10))
print((lambda x: x + 10)(20))


a = list(map(int, [1.2, 2.3, 4.3]))
print(a)


def plus_ten(x):
    return x + 10


a = list(map(plus_ten, [1.2, 2.3, 4.3]))
print(a)

a = list(map(lambda x: x + 10, [1.2, 2.3, 4.3]))
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

la = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(la)