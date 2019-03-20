#!/usr/bin/env python

from threading import Event, Thread
import time

event = Event()

class Pro(Thread):
    def __init__(self, t_name, event):
        super(Pro, self).__init__(name=t_name)
        self.event = event

    def run(self):
        self.event.wait()
        for i in range(5):
            print "%s: ------%d---" % (self.name, i)

class Cur(Thread):
    def __init__(self, t_name, event):
        super(Cur, self).__init__(name=t_name)
        self.event = event

    def run(self):
        for i in range(5):
            print "%s: -----%d----" %  (self.name, i)
        self.event.set()
        #self.event.clear()


if __name__ == "__main__":
    pro = Pro("pro", event)
    cur = Cur("Cur", event)

    pro.start()
    cur.start()
    pro.join()
    cur.join()
