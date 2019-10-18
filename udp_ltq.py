# from socket import*
# udp_socket = socket(AF_INET,SOCK_DGRAM)
#
# port1 = int(input("请输入要绑定的端口:"))
# udp_socket.bind(('',port1))
# port2 = int(input("请输入要发送的端口:"))
# # local = ('',8080)
# # udp_socket.bind(local)
# dest_adder = ('127.0.0.1',8080)
#
# # 从键盘获取数据
# send_data =input("请输入要发送的数据：")
# # 发送数据到指定电脑上
# udp_socket.sendto(send_data.encode('gbk'),dest_adder)
# # 等待接收对方发送的数据
# recv_data = udp_socket.recvfrom(1024)
# # recv_data[0] 是对方的数据
# print(recv_data[0].decode('gbk'))
# # recv_data[1]事ip和端口
# print(recv_data[1])
# # 关闭套接字
# udp_socket.close()
#





import socket
import time
import threading

def keyboard_send(udp_socket):
    while True:
        data = input("请输入要发送的数据:")
        dest_ip = input("请输入要发送的ip:")
        dest_port = int(input("请输入要发送的端口:"))
        udp_socket.sendto(data.encode("utf-8"),(dest_ip,dest_port))

def reciver_data(udp_socket):
    while True:
        reciver_data = udp_socket.recvfrom(1024)
        reciver_ip = reciver_data[1]
        reciver_data = reciver_data[0].decode("utf-8")
        print("----%s:%s---" %(str(reciver_ip),reciver_data))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7788))
    d1 = threading.Thread(target=reciver_data,args=(udp_socket,))
    d1.start()
    keyboard_send(udp_socket)

if __name__ == '__main__':
    main()


