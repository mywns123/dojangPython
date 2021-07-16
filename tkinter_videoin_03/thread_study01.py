import threading


def first_task(data):
    for i in data:
        print("first_task :", i)


def second_task(data1, data2):
    for i, j in zip(data1, data2):
        print("second_task :", i, j)


task1 = threading.Thread(target=first_task, args=(range(5),))
task2 = threading.Thread(target=second_task, args=(range(5), range(5)))

print("START")
task1.start()
task2.start()
print("END")