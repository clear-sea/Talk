#服务器
import socket

host=socket.gethostname()
port=12345

s=socket.socket()
s.bind((host,port))
s.listen(1)

sock,address=s.accept()
print("与客户端"+host+"连接已建立")

info=sock.recv(1024).decode()

while info!="exit":
    if info:
        print("接收:"+info)
    send_data=input("发送:")
    sock.send(send_data.encode())

    if send_data=="exit":
        break

    info=sock.recv(1024).decode()

sock.close()
s.close()