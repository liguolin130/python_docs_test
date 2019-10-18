# 文件夹copy器
import time
import random
import multiprocessing
import os

def copy_file(queue,copy_file_name,former_file_name,new_file_name):
    f_read = open(former_file_name+"/"+copy_file_name,"rb")
    f_write = open(new_file_name+"/"+copy_file_name,"wb")
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()

    queue.put(copy_file_name)  # 发送已经拷贝完的文件

def main():
    # 1. 获取要复制的文件
    former_file_name = input("请输入要复制的文件夹:")
    # 整理目标文件
    new_file_name = former_file_name + "[副本]"
    try:
        os.mkdir(new_file_name)
    except:
        pass # 如果文件存在则创建失败
    file_names = os.listdir(former_file_name)   # 获取文件夹中所有的文件名
    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool()
    for copy_file_name in file_names:
        # 加入进程池
        pool.apply_async(args=(queue,copy_file_name,former_file_name,new_file_name))
    # 主进程显示进度
    pool.close()
    all_file_num = len(file_names)
    while True:
        copy_file_name = queue.get
        if copy_file_name in file_names:
                file_names.remove(copy_file_name)

        copy_rate = (all_file_num-len(file_names))*100/all_file_num
        print("\r%.2f...(%s)" %(copy_rate,copy_file_name)+ ""*50,end="")
        if copy_rate >= 100:
            break
        print()

if __name__ == '__main__':
    main()