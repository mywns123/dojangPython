person_data = ['홍길동', 15, '대구광역시 서구']


def personal_info(*args):  # *args: *person_data
    for arg in args:
        print(arg)


personal_info(*person_data)

person_data_dict = {'name': '홍길동', 'age': '30', 'address': '제주'}


def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('강감찬', 11, '대구')
personal_info(age=20, address='서울', name='강감찬')
personal_info('강감찬', address='전주',  age=24)
personal_info(**person_data_dict)


def personal_info(name, age, address='비공개'):  # 함수정의에서 키워드 값 = 기본값
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('강감찬', 11, '대구')
personal_info('강감찬', 11)




