#客户端
import socket

s=socket.socket()

host=socket.gethostname()
port=12345

s.connect((host,port))
print("已连接到服务器"+host)

info=""
while info!="exit":
    send_data=input("发送:")
    s.send(send_data.encode())

    if send_data=="exit":
        break

    info=s.recv(1024).decode()
    print("接收:"+info)

s.close()
