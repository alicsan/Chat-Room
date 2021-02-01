import socket
import time
import sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 1234



new_socket.bind((str(s_ip), port))
print("Binding successful!")
print("This is your IP:", s_ip)

name=input("Enter name:")
new_socket.listen(1)

conn,add = new_socket.accept()
print("Recieved connection from", add[0])
print("Conection Established. Connected from: ",add[0])

client = (conn.recv(1024)).decode()
print(client + "has connected.")
conn.send(name.enconde())

while True:
    message = input('Me: ')
    conn.send(message.enconde())
    message = conn.recv(1024)
    message = message.decode()
    print(client + ":" + message) 



