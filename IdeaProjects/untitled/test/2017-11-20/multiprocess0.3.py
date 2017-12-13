#!/usr/bin/env python

import threading
from time import sleep


class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print('我是A')
            sleep(1)


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print('我是B')
            sleep(1)


if __name__ == '__main__':
    t1 = A()
    t1.start()
    t2 = B()
    t2.start()
