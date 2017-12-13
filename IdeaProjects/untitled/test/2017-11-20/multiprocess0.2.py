#!/usr/bin/env python

import threading
import datetime
from time import sleep


def music():
    for i in range(25):
        print('%s,I am listening something A-%s' % (str(datetime.datetime.now()), i))
        sleep(1)

def move():
    for j in range(20):
        print('%s,he is watching something B-%s' % (str(datetime.datetime.now()), j))
        sleep(1)


threads = []
t1 = threading.Thread(target=music, args=())
threads.append(t1)
t2 = threading.Thread(target=move, args=())
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
        t.join()

    print('all is over %s' % datetime.datetime.now())
