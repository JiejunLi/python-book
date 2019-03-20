#!/usr/bin/env python

import thread
import time

input = None
lock = thread.allocate_lock()

def threadPro():
    while True:
        print "sub thread id: ", thread.get_ident()
        print "sub thread %d wait lock..." % thread.get_ident()
        lock.acquire()
        print "sub thread %d get lock..." % thread.get_ident()
        print "sub thread %d recevice input : %s " % (thread.get_ident(), input)
        print "sbu thread %d release lock..." % thread.get_ident()
        lock.release()
        if input == 'quit':
            break
        time.sleep(1)

thread.start_new_thread(threadProc, ())
print "mian thread id : ", thread.get_ident()

while True:
    print "main thread %d wait lock..." % thread.get_ident()
    lock.acquire()
    print "main thread %d get lock..." % thread.get_ident()
    input = raw_input()
    print "main thread %d release lock..." % thread.get_ident()
    lock.release()
    if input == 'quit':
        break
    time.sleep(1)
