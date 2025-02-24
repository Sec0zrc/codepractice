from multiprocessing import Process


def task(name):
    for i in range(1000):
        print(f"{name}: {i}")


if __name__ == '__main__':
    p1 = Process(target=task, args=("Bob",))
    p2 = Process(target=task, args=("Tim",))
    p3 = Process(target=task, args=("Mary",))
    p1.start()
    p2.start()
    p3.start()
