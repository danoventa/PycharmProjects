__author__ = 'Noventa'

from queue import Queue
from threading import Thread

dis_queue = Queue(maxsize=0)

dis_queue.put(1)
dis_queue.put(2)
dis_queue.put(3)
print(dis_queue.get())
dis_queue.task_done()

''' this appears to be a way to get through the queue '''
def read_queue (d_q):
    while not d_q.empty():
        print(d_q.get())
        d_q.task_done()

d_q = Queue(maxsize=0)
for x in range(20):
    d_q.put(x)

read_queue(d_q)