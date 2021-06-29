import json
import pickle as pi

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


a = set('apply')
print(a)
print(a)
print(a)

b = set(range(5))
print(b)
print(b)
print(b)


c = {'aaa', 'bbb', 'ccc', 'bbb'}
d = {}
e = {'aaa'}
f = set('aaa')
g = set({'aaa'})
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print(type(g), g)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("a | b >>> ", a | b)
c = set.union(a, b)
print("union >>> ", c)
print(" a & b >>> ", a & b)
c = set.intersection(a, b)
print("intersection >>> ", c)
print("a - b >>> ", a - b)
c = set.difference(a, b)
print("difference >>> ", c)
print("b - a >>> ", b - a)
c = set.difference(b, a)
print("difference >>> ", c)
print("a ^ b >>> ", a ^ b)
c = set.symmetric_difference(a, b)
print("difference >>> ", c)


a = {1, 2, 3, 4}
a |= {5}
print(a)

a = {1, 2, 3, 4}
# a.update(5)
# a.update(set(5))
a.update({5})
print(a)
a.update(set('5'))
print(a)

a = {1, 2, 3, 4}
b = a <= {1, 2, 3, 4}
print(b)
b = a.issubset({1, 2, 3, 4, 5})
print(b)

customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

jsonString = json.dumps(customer)

file = open("test2.txt", "w")
file.write(jsonString)
file.close()

customer = {
    'id': '152352',
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
file = open("data.pkl", "wb")
pi.dump(customer, file)  # 인코더
file.close()

file = open("data.pkl", "rb")
dict = pi.load(file)  # 디코더
file.close()

with open("data.pkl", "wb") as file:
    pi.dump(customer, file)  # 인코더

with open("data.pkl", "rb") as file:
    dict = pi.load(file)  # 디코더

print(dict)


lines = ['하하하하\n', '호호호호호\n', "야야야야야\n"]

with open("hello.txt", 'w') as file:
    file.writelines(lines)

lines = [[10, 20, 30], [40, 50, 60],]

with open("hello.txt", 'w') as file:
    for aa in lines:
        print(aa)
        file.writelines(aa)




