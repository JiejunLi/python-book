#!/usr/bin/env python

import threading
import time
import random

semaphore = threading.Semaphore(0)

def cursumer():
    print("consumer is waiting.")
    semaphore.acquire()
    print("Consumer notify: consumed item number %s." % item)

def producer():
    global item
    time.sleep(2)
    item = random.randint(1, 100)
    print("producer notify: produced item number %s." % item)
    semaphore.release()


if __name__ == "__main__":
    for i in range(5):
        pro = threading.Thread(target=producer)
        cur = threading.Thread(target=cursumer)
        pro.start()
        cur.start()
        pro.join()
        cur.join()
