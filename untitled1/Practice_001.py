__author__ = 'Executor'
import os
import time
import webbrowser

print("Hello, World")
print("start time: " + time.ctime())
for i in range(0, 3):
    time.sleep(1)
    webbrowser.open("www.google.com")
print("end time: " + time.ctime())

def rename_files():
    file_list = os.listdir(r"insert file here")
    print(file_list)
    pass
