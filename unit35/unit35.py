# class Person:
#     bag = []  # 클래스 변수
#
#     def __init__(self, name):
#         self.name = name  # 인스턴스 변수
#
#     def put_bag(self, stuff):
#         self.bag.append(stuff)
#
#     def put_bag_class(self, stuff):
#         Person.bag.append(stuff)
#
#
# james = Person("제임스")
# james.put_bag("책")
#
# maria = Person("마리아")
# maria.put_bag("열쇠")
#
# Person.bag.append("연필")
#
# print("james :", james.name)
# print("james :", james.bag)
# print("Person :", Person.bag)
# print("maria :", maria.name)
# print("maria :", maria.bag)
# print("Person :", Person.bag)
#
# print(james.__dict__)
# print(Person.__dict__)
#
#
# class clac:
#     @staticmethod
#     def add(a, b):
#         print(a+b)
#
#     @ staticmethod
#     def mul(a, b):
#         print(a * b)
#
#     def sub(self, a, b):
#         print(a - b)
#
#
# clac.add(2, 5)
# # clac.sub(2, 5)
# cc = clac()
# cc.sub(5, 3)

#
# class Person:
#     count = 0
#
#     def __init__(self):
#         Person.count += 1
#
#     @classmethod
#     def print_count(cls):
#         print("{0}개의 객체가 생성되었습니다.".format(cls.count))
#
#
# james = Person()
# maria = Person()
#
# Person.print_count()
# print(Person.count)
#
# class Counter:
#     def __init__(self, value=0):
#         self.value = value
#
#     def increment(self, delta=1):
#         self.value += delta
#
#     def decrement(self, delta=1):
#         self.value -= delta
#
#
# cc = Counter()
# cc.value = 10
#
# dd = Counter()
# dd.value = 20
#
# print(cc.value)
# print(dd.value)

#
# class User:
#     def __init__(self, email, password):
#         self.email = email
#         self.password = password
#
#     @classmethod
#     def fromTuple(cls, tup):
#         return cls(tup[0], tup[1])
#
#     @classmethod
#     def fromDictionary(cls, dic):
#         return cls(dic["email"], dic["password"])
#
#
# user1 = User('aa@a.com', '1111')
# user2 = User('dd@a.com', '2222')
# print("user1 : ", user1.email)
# print("user2 : ", user2.email)
#
# user3 = User.fromTuple(('user@a.com', '1111'))
# print("user3 : ", user3.email)
# print("user3 : ", user3.password)
#
# user4 = User.fromDictionary({'email':'userczcxxx@a.com', 'password': '1111'})
# print("user4 : ", user4.email)
# print("user4 : ", user4.password)

class StringUtils:
    @staticmethod
    def toCamelcase(text):
        words = iter(text.split("_"))
        return next(words) + "".join(i.title() for i in words)

    @staticmethod
    def toSnakecase(text):
        letters = ["_" + i.lower() if i.isupper() else i for i in text]
        return "".join(letters).lstrip("_")


print(StringUtils.toCamelcase("abc_dae_de"))
print(StringUtils.toSnakecase("abc_dae_de"))