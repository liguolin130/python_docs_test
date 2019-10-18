

import urllib.request # 抓取网页
import re
import time
import threading
import multiprocessing
import gevent
from gevent import monkey
# monkey.patch_all()
import requests

url = 'https://www.douyu.com/g_yz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
          }

def downloca_img(url_addr, title_name):
    img_contents = urllib.request.urlopen(url_addr).read()
    with open('/home/lgl/桌面/file' + title_name + '.jpg', 'wb') as file:
        file.write(img_contents)
        print('%s以完成下载' % title_name)

# 普通方式(8)
def re_url_list(url_data, title):
    print("普通方法下载图片！")
    # 用k标识下标号,enumerate同时列出数据下标和数据
    for k, url_list in enumerate(url_data):
        print("第(%d)张：" %k)
        downloca_img(url_list, title[k])

# 多线程(7)
def img_thread(ret,title):
    print("多线程下载图片！")
    for a,img_url in enumerate(ret):
        print("第(%d)张：" %a)
        t1 = threading.Thread(target=downloca_img, args=(img_url, title[a]))
        t1.start()
        t1.join()

# 多进程(106)
def img_process(ret, title):
    print("多进程下载图片！")
    for a,img_url in enumerate(ret):
        print("第(%d)张："%a)
        p1 = multiprocessing.Process(target=downloca_img,args=(img_url,title[a]))
        p1.start()
        p1.join()

# 进程池
def img_pool(ret, title):
    print("进程池下载图片！")
    po1 = multiprocessing.Pool(12)
    for a, img_url in enumerate(ret):
        po1.apply_async(downloca_img,(img_url,title[a]))
    po1.close()
    po1.join()
# 协程
def downloca_use_spawn(ret, title):
    print("--------------------协程下载图片---------------------！")
    for a, ret_list in enumerate(ret):
        print("第(%d)张：" % a)
        g1 = gevent.joinall([gevent.spawn(downloca_img, ret_list,title[a])])
        g1.join()

def main():
    opener = requests.get(url, headers=headers)
    read_contents = opener.content.decode()
    # print("333<<<<<<<%s>>>>3333" %read_contents)

    # 使用正则匹配出网页源码里需要抓取到的ret
    ret = re.findall(r'"rs16":"(.*?)/dy1', read_contents)
    # print( "正则ret=====%s==正则ret" %ret)

    # 使用正则匹配出网页源码里需要抓取到的title
    title = re.findall(r'"nn":"(.*?)","od',read_contents)
    # print("正则title==%s==title"%title)

    star = time.time()
    # 1.普通方式
    # re_url_list(ret, title)

    # 2.多线程
    # img_thread(ret, title)

    # 3.多进程
    # img_process(ret,title)

    # 4.进程池
    # img_pool(ret,title)

    # 5.协程
    downloca_use_spawn(ret,title)

    end = time.time()
    print('----------共用时:%d----------' % (end - star))

if __name__ == '__main__':
    main()
