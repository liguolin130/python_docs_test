#
#
# # 两个while循环一起执行
# # 说明：创建子线程时，只需要传入一个执行函数或者是函数的参数，
# #     创建一个Process实例，再用start（）方法启动
#
# import multiprocessing
# import time
# def pro():
#     while True:
#         print("pro zi")
#         time.sleep(1)
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=pro)
#     p.start()
#     while True:
#         print("pro fu")
#         time.sleep(1)
#
#
#
# # 进程pid（os.getpid()）获取
# import multiprocessing
# import time
# import os
# def pros():
#     print("获取子进程的进程号 pid = %s" %os.getpid())
#     print("子进程将要结束")
# if __name__ == '__main__':
#     print("获取父进程的进程号 pid = %s" %os.getpid())
#     p = multiprocessing.Process(target=pros,name ='one')
#     p.start()
#
#
# # 给指定的子进程传递参数
#
# import multiprocessing
# import time
# import os
# def proc(name,age,**kwargs):
#     for a in range(10):
#         print("子进程 name=%s age=%d,pid=%s" %(name,age,os.getpid()))
#         print(kwargs)
#         time.sleep(0.2)
#
# if __name__ =='__main__':
#     p = multiprocessing.Process(target=proc,args=('name',10),kwargs={'m':20})
#     p.start()
#     time.sleep(1)
#     p.terminate() # 让子进程停下来
#     p.join()
#
#
# # 进程间不同享全局变量，两个进程互不相关
# import multiprocessing
# import os
# import time
# nums = [10,20,30]
# def procs1():
#     print("开始的 nums=%s,pid=%d" %(nums,os.getpid()))
#     for a in range(3):
#         nums.append(a)
#         time.sleep(1)
#         print("进程1 nums=%s,pid=%d " %(nums,os.getpid()))
# def procs2():
#     print("进程2 nums=%s,pid=%d" %(nums,os.getpid()))
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=procs1)
#     p1.start()
#     time.sleep(1)
#     p1.join() # 是否等待子线程执行结束，或者等待多少秒
#
#     p2 = multiprocessing.Process(target=procs2)
#     p2.start()
#
# # 进程间通信Queue
# import  multiprocessing
# q = multiprocessing.Queue(3)  # 初始化一个Queue对象，最多可以接受三个put消息
# q.put("information one ")
# q.put("information two")
# print( "两个消息后 %s" %q.full())      # q.full()队列未满返回False
# a = q.put("information three")
# print("三个消息后 %s" %q.full())       # q.full()队列满后返回True
# try:
#     q.put("information four",True,2)
# except:
#     # 返回当前队列包含的消息数量
#     print("消息队列已满，现有的消息有(%d)条" %q.qsize())
# try:
#     q.put_nowait("information four")
# except:
#     print("消息队列已满，现有的消息有(%d)条" %q.qsize())
# if not q.full():   # 判断消息队列是否为空
#     print(q.put_nowait("information four"))
# # 读取消息时，先判断队列是否为空，再读取
# if not q.empty():
#     for a in range(q.qsize()):
#         print(q.get_nowait())
#

# Queue实列
import multiprocessing
import random
import time

def write(q):
    for value in ['A','B','C']:
        print("子线程1value=%s" %value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print("子线程2value=%s" %value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    q = multiprocessing.Queue()
    qw = multiprocessing.Process(target=write,args=(q,))
    qw.start()
    qw.join()
    qr = multiprocessing.Process(target=read,args=(q,))
    qr.start()
    qr.join()


#
# import multiprocessing
# import os,time,random
# def worker(mg):
#     t_start = time.time()
#     print("%s开始执行，进程号为%d" %(mg,os.getpid()))
#     time.sleep(random.random()*2)
#     t_stop = time.time()
#     print(mg,"执行完毕，耗时间为%.2f" %(t_stop-t_start))
# if __name__ == '__main__':
#     po = multiprocessing.Pool(3)
#     for a in range(0,10):
#         po.apply_async(worker,(a,))
#     print("----------start-------------")
#     po.close()
#     po.join() # 主线程阻塞必须等待子线程退出，必须在close（）或者terminate后使用
#     print("--------end----------")


#
# import multiprocessing
# import time,os
# def reader(q):
#     print("reader启动进程号（%s），父进程启动（%s）" %(os.getpid(),os.getppid()))
#     for a in range(q.qsize()):
#         print("reader从Queue中获取到消息%s:" %q.get(True))
# def writer(q):
#     print("writer启动(%s),父进程启动（%s）" %(os.getpid(),os.getppid()))
#     for a in "guolin":
#         q.put(a)
#
# if __name__ == '__main__':
#     print("(%s)--- stsrt---" %os.getpid())
#     q = multiprocessing.Manager().Queue()
#     po = multiprocessing.Pool()
#     po.apply_async(writer,(q,))
#     time.sleep(1)
#     po.apply_async(reader,(q,))
#     po.close()
#     po.join()
#     print("(%d)---end---- " %os.getpid())
#



# class MyList(object):
#     def __init__(self):
#         self.container = []
#     def add(self, item):
#         self.container.append(item)
#
# mylist = MyList()
# mylist.add(1)
# mylist.add(2)
# mylist.add(3)
# for num in mylist:
#    print(num)
# from typing import Iterable
#
#
# class my_list(object):
#     def __init__(self):
#         self.counter = []
#     def add(self,item):
#         self.counter.append(item)
#     def __iter__(self):
#         pass
# mylist = my_list()
# mylist.add(1)
# print(isinstance(mylist,Iterable))

#
# #迭代器Iterator
# class my_list(object):
#     def __init__(self):
#         self.item = []
#     def add(self,val):
#         self.item.append(val)
#     def __iter__(self):
#         iterator = my_iterator(self)
#         return iterator
#
#
# class my_iterator(object):
#     def __init__(self,mylist):
#         self.mylist = mylist
#         self.current = 0
#
#     def __next__(self):
#         if self.current < len(self.mylist.item):
#             items = self.mylist.item[self.current]
#             self.current += 1
#             return items
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
#
# if __name__ == '__main__':
#     mylist = my_list()
#     mylist.add(1)
#     mylist.add(2)
#     mylist.add(3)
#     for num in mylist:
#         print(num)
#
#
#
