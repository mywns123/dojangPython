y = {1: 'one', 2: 'two', 3: "three"}
for i in y.items():
    print(i)


keys = {'a', 'b', 'c', 'd'}
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items():
#     if value == 20:
#         print(x)
#         del x[key]
#         print(x)


# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# for key, value in x.items():
#     if value == 20:
#         print(x)
#         x.popitem()
#         print(x)


x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)





