# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greeting(self):
#         print("안녕하세요")
#
#
# class Student(Person):
#     def __init__(self, person):
#         self.person = person
#
#     def study(self):
#         print('공부합니다.')
#
#
# class Person_list():
#     def __init__(self):
#         self.person_list = []  #[jildong, gamssan]
#
#     def append_person(self, person):
#         self.person_list.append(person)
#
#
# class Policeman(Person):  # is-a
#     def __init__(self, person, num):
#         self.person = person
#         self.gun = Gun(num)  # has-a
#
#     def emp(self):
#         print("근무합니다.")
#
#
# class Gun():
#     def __init__(self, num):
#         self.num = num
#
#     def shooting(self):
#         print('권총 발사')

# class Student2(Student):
#     def study2(self):
#         print('공부하기2')

# st = Student2()
# st.greeting()
# st.study()
# st.study2()

# pl = Person_list()
# jildong = Person('홍길동')
# gamssan = Person('강감찬')
#
# pl.append_person(jildong)
# pl.append_person(gamssan)
#
# pl.person_list[0].greeting()
# print(pl.person_list[0].name)


# person1 = Person("을지문덕경관")
# person2 = Person('홍길동 학생')
# po1 = Policeman(person1, 4)
# po1.greeting()
# po1.emp()
# print(po1.gun.num)
# po1.gun.shooting()
#
#
# st1 = Student(person2)
# st1.greeting()
# st1.study()
# print(st1.__dict__)


