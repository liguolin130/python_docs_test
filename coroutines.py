
# 创建生成器的方法一
# builder = (a**2 for a in range(0,5))
# print(builder)
# # 1>next()方法调用
# print(next(builder))
# print(next(builder))
# # 方法二for调用
# for a in builder:
#     print("for循环下=%d" %a)




# 实现简单协程Coroutine
# import time
# def demo1():
#     while True:
#         print("demo1")
#         #yield
#         time.sleep(1)
# def demo2():
#     while True:
#         print("demo2")
#         yield
#         time.sleep(1)
# def main():
#     d1 = demo1()
#     d2 = demo2()
#     counter = 0
#     while counter < 4:
#         next(d1)
#         next(d2)
#         counter += 1
#
# if __name__ == '__main__':
#     main()

# greenlet 对多任务进行封装，从而使得任务切换变得更加简单
# import time
# from greenlet import greenlet
#
#
# def demo1():
#     while True:
#         print("---demo1----")
#         d2.switch()
#         time.sleep(1)
#
# def demo2():
#     while True:
#         print("----demo2-----")
#         d1.switch()
#         time.sleep(1)
# d1 = greenlet(demo1)
# d2 = greenlet(demo2)
#
# # d1.switch()

# # gevent 的自动切换任务,三个greenlet是一次性运行的
# import gevent
# def demo(b):
#     for a in range(b):
#         print("greenlet=%s" %gevent.getcurrent(),a)
# d1 = gevent.spawn(demo,3)
# d2 = gevent.spawn(demo,4)
# d3 = gevent.spawn(demo,5)
# d1.join()
# d2.join()
# d3.join()

# gevent切换执行,模拟一个耗时操作
# import gevent
# def demo(num):
#     for a in range(num):
#         print("greenlet=%s" %gevent.getcurrent(),a)
#         gevent.sleep(1)
# d1 = gevent.spawn(demo,2)
# d2 = gevent.spawn(demo,3)
# d3 =gevent.spawn(demo,4)
# d1.join()
# d2.join()
# d3.join()

# 给程序打补丁
# import time
#
# import gevent
# import random
#
#
# from gevent import monkey
#
# monkey.patch_all()
# def demo(num):
#     for a in range(10):
#         print(num,a)
#         time.sleep(random.random())
# gevent.joinall([
#                 gevent.spawn(demo,"greentel1"),
#                 gevent.spawn(demo,"greental2")
#               ])

# 并发下载器（并发下载原理）
from gevent import monkey
import gevent
import urllib.request

#有IO才做时需要这一句
monkey.patch_all()

def my_downLoad(file_name, url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as f:
        f.write(data)

    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(my_downLoad, "1.mp4", 'http://oo52bgdsl.bkt.clouddn.com/05day-08-%E3%80%90%E7%90%86%E8%A7%A3%E3%80%91%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E6%80%BB%E7%BB%93%EF%BC%88%E4%B8%80%EF%BC%89.mp4'),
        gevent.spawn(my_downLoad, "2.mp4", 'http://oo52bgdsl.bkt.clouddn.com/05day-03-%E3%80%90%E6%8E%8C%E6%8F%A1%E3%80%91%E6%97%A0%E5%8F%82%E6%95%B0%E6%97%A0%E8%BF%94%E5%9B%9E%E5%80%BC%E5%87%BD%E6%95%B0%E7%9A%84%E5%AE%9A%E4%B9%89%E3%80%81%E8%B0%83%E7%94%A8%28%E4%B8%8B%29.mp4'),
])