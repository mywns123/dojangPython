import pickle as pi

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:
    pi.dump(name, file)
    pi.dump(age, file)
    pi.dump(address, file)
    pi.dump(scores, file)


with open('james.p', 'rb') as file:
    name = pi.load(file)
    age = pi.load(file)
    address = pi.load(file)
    scores = pi.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
