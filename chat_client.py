import socket
import time
import sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
port = 1234

print("This is your IP address: "+ip)
server_host = input("Enter friend's IP address: ")
name = input("Enter friend's name: ")

socket_server.connect((server_host,port))
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name + " has joined...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name,":",message)
    message = input("Me: ")
    socket_server.send(message.encode())