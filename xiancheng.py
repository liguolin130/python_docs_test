# ,,,
# from time import sleep
# def sing():
#     for a in range(4):
#         print("be singing %d" %a)
#         sleep(1)
# def dance():
#     for a in range(4):
#         print("be danceing %d" %a)
#         sleep(1)
# if __name__ == '__main__':
#     sing()
#     dance()
#
#
# # 单线程
# from time import  sleep
# def sayhello():
#     print("hello everyone")
#     sleep(1)
# if __name__ == '__main__':
#     for a in range(4):
#         sayhello()

# # 多线程使用thread
# import threading
# from time import sleep
# def sayhello():
#     print("hello ")
#     sleep(1)
# if __name__ == '__main__':
#     for a in range(5):     #使用多线程并发处理
#         b = threading.Thread(target=sayhello)
#         b.start() # 启动线程让线程开始执行
#
#
#
# # 主线程会等待所有的子线程结束后才会结束
# import threading
# import time
# def sing():
#     for a in range(3):
#         print(" to singing %d" %a)
#         time.sleep(1)
# def dance():
#     for a in range(3):
#         print("to danceing %d" %a)
#         time.sleep(1)
# if __name__ == '__main__' :
#     print("开始 %s" %time.ctime())
#     b1 = threading.Thread(target=sing)
#     b2 = threading.Thread(target=dance)
#     b1.start()
#     b2.start()
#     time.sleep(2)
#     print("结束 %s" %time.ctime())
#     # 查看线程数量
#     while True:
#         length = len(threading.enumerate())
#         print("正在运行的线程有%d个" %length)
#         if length <=1:
#             break
#         time.sleep(1)
#
#
# # 线程执行代码封装方法
# import threading
# import time
# class my_thread(threading.Thread):
#    def run(self):
#         for a in range(3):
#            time.sleep(1)
#             mg = "this is "+self.name + ' @ '+str(a)       # name属性保存的是当前的线程
#             print(mg)
# def test():
#     for b in range(5):
#         result = my_thread()
#         result.start()
#         time.sleep(1)
# if __name__ == '__main__':
#     test()
#     time.sleep(4)
#
#
# # 列表当作参数添加到线程中
# import threading
# import time
# nums = [10,20,25]
# def demo1(num):
#     num.append(30)
#     print("in demo1= %s" %num)
# def demo2(num):
#     time.sleep(1)
#     print("in demo2= %s" %num)
# result1 = threading.Thread(target=demo1,args=(nums,))
# result1.start()
# result2 = threading.Thread(target=demo2,args=(nums,))
# result2.start()
#
#
# # 线程t1和t2对全局变量进行加一运算,加10次 最终的结果是20
# import threading
# import time
# g_num = 0
# def demo1(num):
#     global g_num
#     for a in range(num):
#         g_num += 1
#     print("t1加后的值 %d" %g_num)
#
# def demo2(num):
#     global  g_num
#     for a in range(num):
#         g_num += 1
#     print("t2加 %d" %g_num)
#
# print("没有创建线程之前 %d" %g_num)
#
# t1 = threading.Thread(target=demo1,args=(1000000,))
# t1.start()
#
# t2 = threading.Thread(target=demo2,args=(1000000,))
# t2.start()
#
# while len(threading.enumerate()) !=1 :
#     time.sleep(1)
# print("最终的结果是 %d" %g_num)
# # ps:多个线程对quantities变量进行操作时会出现资源抢占问题
#
#
# # 创建互斥锁完成两个线程对一个全局变量的修改
# import threading
# import time
# g_num = 0
# def demo1(num):
#     global  g_num
#     for a in range(num):
#         the_mutex.acquire()
#         g_num += 1
#         the_mutex.release()
#     print("t1 changge %d" %g_num)
# def demo2(num):
#     global g_num
#     for a in range(num):
#         the_mutex.acquire()
#         g_num += 1
#         the_mutex.release()
#     print("t2 change %d" %g_num)
#
# the_mutex = threading.Lock()# 创建一个互斥锁,默认是未上锁的状态
#
#
# t1 = threading.Thread(target=demo1,args=(10000000,))
# t1.start()
#
# t2 = threading.Thread(target=demo2,args=(10000000,))
# t2.start()
# while len(threading.enumerate()) != 1:
#     time.sleep(1)
# print("最终结果=%d" %g_num)
#
#
# # 死锁
# import threading
# import time
# class my_thread1(threading.Thread):
#     def run(self):
#         mutexA.acquire()
#         print(self.name+" acquireA" )
#         time.sleep(1)
#
#         mutexB.acquire()
#         print(self.name+" acquireB")
#         mutexB.release()
#         mutexA.release()
# class my_thread2(threading.Thread):
#     def run(self):
#         mutexB.acquire()
#         print(self.name+" acquireA")
#         time.sleep(1)
#
#         mutexA.acquire()
#         print(self.name+ " acquireB")
#         mutexA.acquire()
#         mutexB.release()
# mutexA = threading.Lock()
# mutexB = threading.Lock()
#
# # 银行家算法是从当前状态出发，逐个按安全序列检查各客户谁能完成其工作，
# # 然后假定其完成工作且归还全部贷款，再进而检查下一个能完成工作的客户，......
# # 。如果所有客户都能完成工作，则找到一个安全序列，银行家才是安全的。
# # 1.此时已经进入了死锁状态，程序设计时要尽量避免银行家算法，添加超时时间等
#
# if __name__ == '__main__':
#     result1 = my_thread1()
#     result1.start()
#     time.sleep(1)
#     result2 = my_thread2()
#     result2.start()
# ,,,
