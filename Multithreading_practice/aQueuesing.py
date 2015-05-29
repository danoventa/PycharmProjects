__author__ = 'Noventa'

from queue import Queue

dis_queue = Queue(maxsize=0)

dis_queue.put(1)
dis_queue.put(2)
dis_queue.put(3)
print(dis_queue.get())
dis_queue.task_done()
