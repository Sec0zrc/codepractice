"""
a simple demo for Thread
"""
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def task(name):
    for i in range(100):
        print(f"{name} {i}")


class myThread(Thread):
    def __init__(self, name):
        super(myThread, self).__init__()
        self.name = name

    def run(self):
        for i in range(100):
            print(f"{self.name} {i}")


def func(name, t):
    time.sleep(t)
    return name


def print_res(res):
    print(res.result())


if __name__ == '__main__':
    # t1 = Thread(target=task, args=("tom",))
    # t2 = Thread(target=task, args=("Mary",))
    # t3 = Thread(target=task, args=("Tim",))
    #
    # t1.start()
    # t2.start()
    # t3.start()

    # t1 = myThread("Tom")
    # t2 = myThread("Tim")
    # t3 = myThread("Bob")
    #
    # t1.start()
    # t2.start()
    # t3.start()

    with ThreadPoolExecutor(3) as t:
        # add_done_callback 函数在线程执行完后立即执行，所以获取的结果可能和预期的不一样
        # t.submit(func, "TOM", 3).add_done_callback(print_res)
        # t.submit(func, "Mary", 2).add_done_callback(print_res)
        # t.submit(func, "Bob", 1).add_done_callback(print_res)
        # 输出结果为 Bob Mary Tom

        # map的结果是按照线程顺序的
        result = t.map(func, ["Tom", "Mary", "Bob"], [3, 2, 1])
        for i in result:
            print(i)
        # 输出结果为  Tom Mary Bob
