import pickle as pi


def ViewHeadLine():
    print("-----------------------------------------------------------------")
    print('|     이름     |           주소           |          나이         |')


def ViewFootLine():
    print("-----------------------------------------------------------------")


def view(student):
    ViewHeadLine()
    for key, value in student.items():
        print("|", f'{key:^9}', "|", end=' ')
        for data in value:
            print(f'{data:^22}', end='|')
        print()
    ViewFootLine()
    return student



def insert(student):
    name = input("이름을 입력하세요 >>> ")
    if name not in student:
        address = input("주소를 입력하세요 >>> ")
        age = int(input("나이를 입력하세요 >>> "))
        print("주소 정보가 입력되었습니다.")
    else:
        print("학생이 존재합니다.")
        return insert(student)

    student[name] = [address, age]
    person = student[name]
    view(student)
    return student


def update(student):
    name = input("수정 할 친구의 이름을 입력하세요. >>> ")
    if name in student:
        address = input("주소를 입력하세요 >>> ")
        age = int(input("나이를 입력하세요 >>> "))
        print("주소 정보가 입력되었습니다.")
        student[name] = [address, age]
        person = student[name]
    else:
        print("해당 이름이 없습니다.")
        return update(student)

    view(student)
    return student


def delete(student):
    name = input("삭제 할 친구의 이름을 입력하세요. >>> ")
    if name in student:
        student.pop(name)
    else:
        print("해당 이름이 없습니다.")
        return delete(student)

    view(student)
    return student


def search(student):
    name = input("검색 할 친구의 이름을 입력하세요. >>> ")
    if name in student:
        ViewHeadLine()
        print('|', f'{name:^10}', end='|')
        for data in student.get(name):
            print(f'{data:^22}', end='|')
        print()
        ViewFootLine()
    else:
        print("해당 이름이 없습니다.")
        return search(student)

    return student


def save(student):
    with open("data.pkl", "wb") as file:
        pi.dump(student, file)  # 인코더
    print("저장 되었습니다.")


def dataLoad(student):
    import os.path
    isFile = os.path.isfile("data.pkl")
    if isFile == False:
        with open("data.pkl", "wb") as file:
            print("파일을 생성하였습니다.")
            pi.dump(student, file)  # 인코더
    else:
        with open("data.pkl", "rb") as file:
                student = pi.load(file)  # 디코더
        return student


def jsonSave():
    pass


def jsonLoad():
    pass


def mainMenu():
    print()
    print("-----------------------------------------------------------------")
    print("|                                                               |")
    print("|                     주소록 관리 프로그램                         |")
    print("|                                                               |")
    print("|         1. 등록         2. 목록         3. 수정                 |")
    print("|         4. 삭제         5. 검색         6. 저장                 |")
    print("|         7. json저장     8. jsonLoad    9. 종료                 |")
    print("|                                                               |")
    print("-----------------------------------------------------------------")
    print()


def main():
    mainMenu()
    student = dict()
    student = dataLoad(student)
    while True:
        select = int(input("1.등록 2.목록 3.수정 4.삭제 5.검색 6.저장 7.json저장 8.json불러오기 9.종료\n"))
        if select == 1:
            student == insert(student)
        elif select == 2:
            student == view(student)
        elif select == 3:
            student == update(student)
        elif select == 4:
            student == delete(student)
        elif select == 5:
            student == search(student)
        elif select == 6:
            student == save(student)
        elif select == 7:
            student == jsonSave(student)
        elif select == 8:
            student == jsonLoad(student)
        else:
            break


if __name__ == "__main__":
    main()
