#!/usr/bin/env python

from Queue import Queue
import threading
import time


class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        #super(Producer, self).__init__(self, name=t_name)
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            print "%s is producing %d ----" % (self.getName(), i)
            self.data.put(i)
            time.sleep(1)

        print "producer finished"

class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        super(Consumer, self).__init__(name=t_name)
        #threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print "%s is consuming %d ----" % (self.getName(), i)
            time.sleep(1)

        print "consumer finished!"

def main():
    queue = Queue()
    producer = Producer('Pro', queue)
    consumer = Consumer('Con', queue)

    producer.start()
    #producer.join()
    consumer.start()

    producer.join()
    consumer.join()
    print "All threads terminate!"


if __name__ == "__main__":
    main()
