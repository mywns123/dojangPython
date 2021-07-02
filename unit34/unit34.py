from typing import Any


class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def greeting(self):
        print("{0} 저는 {1}입니다.".format(self.hello, self.name))

    def getAge(self):
        print("나는 {0}이고 나이는 {1}살입니다.".format(self.name, self.age))

    def getGreeting(self):
        return self.__wallet

    def setGreeting(self, wallet ):
        self.__wallet -= wallet

    def pay(self, amount):
        if amount > self.__wallet:
            print("돈이 모자라네...")
            return
        self.__wallet -= amount


maria = Person('마리아', 20, '서울시 서초구 반포동', 20000)
maria.greeting()
maria.getAge()
print()

james = Person('제임스', 33, '뉴욕', 30000)
james.greeting()
james.getAge()
print()
james.age = 44
james.getAge()

print(maria)
print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)
print('현금:', maria.getGreeting())
maria.setGreeting(5000)
print('현금:', maria.getGreeting())
maria.pay(20000)
print('현금:', maria.getGreeting())

# class Per:
#     def __init__(self, name, level, attack, hp):
#         self.hello = "안녕하세요"
#         self.name = name
#         self.level = level
#         self.attack = attack
#         self.hp = hp
#
#     def info(self):
#         print("제 이름은{0}입니다. 레벨{1}, 공격력{2}입니다.".format(self.name, self.level, self.attack))
#
#     def attacking(self):
#         print("{0}가 {1}데미지를 입혔습니다.".format(self.name, self.attack))
#
#     def thanking(self):
#         print("{0}가 {1}데미지를 입었습니다.".format(self.name, self.attack))
#
#
# jin = Per('jin', 15, 50, 200)
# lu = Per('lu', 10, 30, 150)
# jin.info()
# lu.info()
# jin.attacking()