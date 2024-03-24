
import socket
import subprocess


host = ''
port = 5000

server = server.socket()

server.bind((host, port))

print("Start")
"""
def login():
    print("Start")
    server.listen(1)
    
    client = server.accept()
    clientAddress = server.accept()
"""
server.setTimeout(60)
server.listen(1)    
client = server.accept()
clientAddress = server.accept()

print(client.recv(1024))
#thisCommand = server.recv(4096)
#command.decode()


    
    
    
    



