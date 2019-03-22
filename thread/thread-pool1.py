from Queue import Queue
import threading
from threading import Thread
import time

#创建队列实例，用来存储任务
queue = Queue()

# 具体要执行的任务，这里只是打印 print
def do_job():
    while True:
        i = queue.get()
        time.sleep(1)
        print "index %s, current: %s" % (i, threading.current_thread())
        queue.task_done()

if __name__ == "__main__":

    # 初始化3个线程的线程池
    for i in range(3):
        t = Thread(target=do_job)
        t.setDaemon(True)  # 设置daemon，主进程退出，线程也退出
        t.start()

    time.sleep(3)
    # 往队列里面放入10个任务
    for i in range(10):
        queue.put(i)

    queue.join()
