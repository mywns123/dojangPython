# it = [1, 2, 3, 4].__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
#
# str = "Hello world".__iter__()
# print(str.__next__())
# print(str.__next__())
# print(str.__next__())
# print(str.__next__())
#
# set = {1, 2, 3}.__iter__()
# print(set.__next__())
# print(set.__next__())
# print(set.__next__())
#
# dict_a = {'1': 'aaa', '2': 'bbb'}.__iter__()
# print(dict_a.__next__())
# print(dict_a.__next__())
#
# print(range(3).__iter__())

# class Counter:
#     def __init__(self, stop):
#         self.stop = stop
#
#     def __getitem__(self, item):
#         if item < self.stop:
#             return item
#
#         else:
#             raise IndexError
#
#
# c = Counter(3)
# print(c[0])
# print(c[1])
# print(c[2])


# it = iter([30, 40, 50])
# print(next(it))
# print(next(it))
# print(next(it))

import random
it = iter(lambda: random.randint(0, 5), 2)
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))

# for i in iter(lambda: random.randint(0, 5), 2):
#     print(i, end='\n')

# it = iter(range(3))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
# print(next(it, 10))
