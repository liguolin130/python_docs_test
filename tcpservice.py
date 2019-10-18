# #tcp 客户端
# from socket import*
# # 1.创建套接字
# tcp_client_socket = socket(AF_INET,SOCK_STREAM)
# # 2.发送目的信息
# server_ip = input("请输入要发送的ip：")
# server_port = int(input("请输入要发送的port："))
# tcp_client_socket.bind(("",server_port))
# # 3.连接服务器
# tcp_client_socket.connect((server_ip,server_port))
# # 4.要发送的数据
# send_data = input("请输入要发送的数据:")
# tcp_client_socket.send(send_data.encode('gbk'))
# # 5.接收最大的数据
# reciver_data = tcp_client_socket.recv(1024)
# print("接收到的数据为：%s" %reciver_data.decode('gbk'))
# tcp_client_socket.close()
#
#


# # 服务器
# from socket import*
# import sys
# def get_file_content(file_name):
#     # 获取文件内容
#     try:
#         with open(file_name,"rb") as a:
#             content = a.read()
#         return content
#     except:
#         print("没有下载文件&s" %file_name)
#
# def main():
#     if len(sys.argv) != 2:
#         print("请按照一下方式运行：python3 xxx.py  7890")
#     else:
#         pot = int(sys.argv[1])
#
#     tcp_server_socket = socket(AF_INET,SOCK_STREAM)
#     local_information = ("",8080)
#     tcp_server_socket.bind(local_information)
#     # 将主动套接字变为被动套接字
#     tcp_server_socket.listen(128)
#     while True:
#         # 等待客户端链接，即为这个客户端链接文件
#         client_socket,clientAddr = tcp_server_socket.accept()
#         receive_data = tcp_server_socket.recv(1024)
#         file_name = receive_data.decode("utf-8")
#         print("对方请求下载的文件名：%s" %file_name)
#         file_content = get_file_content(file_name)
#         if file_content:
#             client_socket.send(file_content)
#         client_socket.close()
#     tcp_server_socket.close()
#
# if __name__ == '__main__':
#     main()
#
#
#





# # tcp服务端
# from socket import *
# # 1.创建套接字
# tcp_service_socket = socket(AF_INET, SOCK_STREAM)
# # 2.本地信息
# local_information = ('', 5201)
# # 3.绑定端口
# tcp_service_socket.bind(local_information)
# # 4.使用socket创建的套接字默认是主动的，使用listen将其变为被动的，就可以接收别人的链接
# tcp_service_socket.listen(128)
# # 5.如果有新的客户端来链接服务器，那么就有一个新的套接字专门为客户端服务
# client_socket, clientAddr = tcp_service_socket.accept()
# # 6.接收对方发送来的数据
# reciver_data = client_socket.recv(1024)
# print("接收到的数据：%s" % reciver_data.decode('gbk'))
# # 7.发送一些数据到客户端
# client_socket.send("22;lk;;lk".encode('gbk'))
# client_socket.close()



# 文件下载器客户端
from socket import*
def main():
    tcp_client_socket = socket(AF_INET,SOCK_STREAM)
    servers_ip = input("请输入服务器地址：")
    servers_port = int(input("请输入服务器端口："))
    # 3.链接服务器
    tcp_client_socket.connect((servers_ip,servers_port))

    # 发送文件下载请求
    file_name = input("请输入要下载的文件名:")
    tcp_client_socket.send(file_name.encode("utf-8"))

    # 接收对方发送过来的数据
    receive_data = tcp_client_socket.recv(1024)
    print("接收到的数据为：",receive_data.decode('gbk'))

    # 如果接收到了数据再创建文件
    if receive_data:
        with open("[接收]"+file_name,"wb") as a:
            a.write(receive_data)
    tcp_client_socket.close()

if __name__ == '__main__':
    main()