# web静态服务器-1-显示固定的页面
#
# import socket
# def handle_client(client_socket):
#     "为一个客户端进行服务"
#     reciver_data = client_socket.recv(1024).decode("utf-8")
#     request_header_lines = reciver_data.splitlines()
#     for line in request_header_lines:
#         print(line)
#     # 组织相应的头信息
#     response_headers = "HTTP/1.1 200 OK \r\n"  # 200表示找到这个资源
#     response_headers += "/r/k"                 #用一个空的行进行与body隔开
#     # 组织内容
#     response_body = "HELLO GUOLIN"
#
#     response = response_headers + response_body
#     client_socket.send(response.encode("utf-8"))
#     client_socket.close()
#
# def main():
#     # 创建套接字
#     server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 设置当前服务器先close，即服务器端四次挥手之后能立即释放资源释放资源，
#     #这样就可以保证在下次运行时，可以立即绑定7788端口
#     server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#     server_socket.bind(("",7788))
#     server_socket.listen(128)
#     client_socket,client_adder = server_socket.accept()
#     handle_client(client_socket)
#
# if __name__ == '__main__':
#     main()

#
# import socket
# import re
#
#
# def handle_client(client_socket):
#     "为一个客户端进行服务"
#     recv_data = client_socket.recv(1024).decode('utf-8', errors="ignore")
#     request_header_lines = recv_data.splitlines()
#     for line in request_header_lines:
#         print(line)
#
#     http_request_line = request_header_lines[0]
#     get_file_name = re.match("[^/]+(/[^ ]*)", http_request_line).group(1)
#     print("file name is ===>%s" % get_file_name)  # for test
#
#     # 如果没有指定访问哪个页面。例如index.html
#     # GET / HTTP/1.1
#     if get_file_name == "/":
#         get_file_name = DOCUMENTS_ROOT + "/index.html"
#     else:
#         get_file_name = DOCUMENTS_ROOT + get_file_name
#
#     print("file name is ===2>%s" % get_file_name) #for test
#
#     try:
#         f = open(get_file_name, "rb")
#     except IOError:
#         # 404表示没有这个页面
#         response_headers = "HTTP/1.1 404 not found\r\n"
#         response_headers += "\r\n"
#         response_body = "====sorry ,file not found===="
#     else:
#         response_headers = "HTTP/1.1 200 OK\r\n"
#         response_headers += "\r\n"
#         response_body = f.read()
#         f.close()
#     finally:
#         # 因为头信息在组织的时候，是按照字符串组织的，不能与以二进制打开文件读取的数据合并，因此分开发送
#         # 先发送response的头信息
#         client_socket.send(response_headers.encode('utf-8'))
#         # 再发送body
#         client_socket.send(response_body)
#         client_socket.close()
#
#
# def main():
#     "作为程序的主控制入口"
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind(("", 7788))
#     server_socket.listen(128)
#     while True:
#         client_socket, clien_cAddr = server_socket.accept()
#         handle_client(client_socket)
#
#
# #这里配置服务器
# DOCUMENTS_ROOT = "./html"
#
# if __name__ == "__main__":
#     main()
#

#
# import socket
# import re
# import multiprocessing
#
#
# class WSGIServer(object):
#
#     def __init__(self, server_address):
#         # 创建一个tcp套接字
#         self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # 允许立即使用上次绑定的port
#         self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         # 绑定
#         self.listen_socket.bind(server_address)
#         # 变为被动，并制定队列的长度
#         self.listen_socket.listen(128)
#
#     def serve_forever(self):
#         "循环运行web服务器，等待客户端的链接并为客户端服务"
#         while True:
#             # 等待新客户端到来
#             client_socket, client_address = self.listen_socket.accept()
#             print(client_address)  # for test
#             new_process = multiprocessing.Process(target=self.handleRequest, args=(client_socket,))
#             new_process.start()
#
#             # 因为子进程已经复制了父进程的套接字等资源，所以父进程调用close不会将他们对应的这个链接关闭的
#             client_socket.close()
#
#     def handleRequest(self, client_socket):
#         "用一个新的进程，为一个客户端进行服务"
#         recv_data = client_socket.recv(1024).decode('utf-8')
#         print(recv_data)
#         requestHeaderLines = recv_data.splitlines()
#         for line in requestHeaderLines:
#             print(line)
#
#         request_line = requestHeaderLines[0]
#         get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
#         print("file name is ===>%s" % get_file_name) # for test
#
#         if get_file_name == "/":
#             get_file_name = DOCUMENTS_ROOT + "/index.html"
#         else:
#             get_file_name = DOCUMENTS_ROOT + get_file_name
#
#         print("file name is ===2>%s" % get_file_name) # for test
#
#         try:
#             f = open(get_file_name, "rb")
#         except IOError:
#             response_header = "HTTP/1.1 404 not found\r\n"
#             response_header += "\r\n"
#             response_body = "====sorry ,file not found===="
#         else:
#             response_header = "HTTP/1.1 200 OK\r\n"
#             response_header += "\r\n"
#             response_body = f.read()
#             f.close()
#         finally:
#             client_socket.send(response_header.encode('utf-8'))
#             client_socket.send(response_body)
#             client_socket.close()
#
#
# # 设定服务器的端口
# SERVER_ADDR = (HOST, PORT) = "", 8888
# # 设置服务器服务静态资源时的路径
# DOCUMENTS_ROOT = "./html"
#
#
# def main():
#     httpd = WSGIServer(SERVER_ADDR)
#     print("web Server: Serving HTTP on port %d ...\n" % PORT)
#     httpd.serve_forever()
#
# if __name__ == "__main__":
#     main()



# Web静态服务器-4-多线程

#coding=utf-8
# import socket
# import re
# import threading
#
#
# class WSGIServer(object):
#
#     def __init__(self, server_address):
#         # 创建一个tcp套接字
#         self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # 允许立即使用上次绑定的port
#         self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         # 绑定
#         self.listen_socket.bind(server_address)
#         # 变为被动，并制定队列的长度
#         self.listen_socket.listen(128)
#
#     def serve_forever(self):
#         "循环运行web服务器，等待客户端的链接并为客户端服务"
#         while True:
#             # 等待新客户端到来
#             client_socket, client_address = self.listen_socket.accept()
#             print(client_address)
#             new_process = threading.Thread(target=self.handleRequest, args=(client_socket,))
#             new_process.start()
#
#             # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
#             # client_socket.close()
#
#     def handleRequest(self, client_socket):
#         "用一个新的进程，为一个客户端进行服务"
#         recv_data = client_socket.recv(1024).decode('utf-8')
#         print(recv_data)
#         requestHeaderLines = recv_data.splitlines()
#         for line in requestHeaderLines:
#             print(line)
#
#         request_line = requestHeaderLines[0]
#         get_file_name = re.match("[^/]+(/[^ ]*)", request_line).group(1)
#         print("file name is ===>%s" % get_file_name) # for test
#
#         if get_file_name == "/":
#             get_file_name = DOCUMENTS_ROOT + "/index.html"
#         else:
#             get_file_name = DOCUMENTS_ROOT + get_file_name
#
#         print("file name is ===2>%s" % get_file_name) # for test
#
#         try:
#             f = open(get_file_name, "rb")
#         except IOError:
#             response_header = "HTTP/1.1 404 not found\r\n"
#             response_header += "\r\n"
#             response_body = "====sorry ,file not found===="
#         else:
#             response_header = "HTTP/1.1 200 OK\r\n"
#             response_header += "\r\n"
#             response_body = f.read()
#             f.close()
#         finally:
#             client_socket.send(response_header.encode('utf-8'))
#             client_socket.send(response_body)
#             client_socket.close()
#
#
# # 设定服务器的端口
# SERVER_ADDR = (HOST, PORT) = "", 8888
# # 设置服务器服务静态资源时的路径
# DOCUMENTS_ROOT = "./html"
#
#
# def main():
#     httpd = WSGIServer(SERVER_ADDR)
#     print("web Server: Serving HTTP on port %d ...\n" % PORT)
#     httpd.serve_forever()
#
# if __name__ == "__main__":
#     main()
