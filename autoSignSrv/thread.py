import _thread
import time

#多线程并发

def req(ThreadName,nd2):
    time.sleep(1)
    print("%s : %d" % (ThreadName,time.time()*1000000))

_thread.start_new_thread(req,("NO.1",1))
_thread.start_new_thread(req,("NO.2",1))
_thread.start_new_thread(req,("NO.3",1))
_thread.start_new_thread(req,("NO.4",1))
_thread.start_new_thread(req,("NO.5",1))
_thread.start_new_thread(req,("NO.6",1))
_thread.start_new_thread(req,("NO.7",1))
_thread.start_new_thread(req,("NO.8",1))
_thread.start_new_thread(req,("NO.9",1))
_thread.start_new_thread(req,("NO.10",1))
_thread.start_new_thread(req,("NO.11",1))
_thread.start_new_thread(req,("NO.12",1))   

while 1:
   pass