import socket

password = "aXsl1ms9203mdujs"

host = socket.gethostname() # Enter IP address of target machine here
port = 6000

client = socket.socket()
client.connect((host, port))

client.send(password.encode())

command = input("Enter command: ")

while command.lower().strip() != 'exit':
    client.send(command.encode())
    response = client.recv(1024).decode()
    print(response)
    command = input("Enter command: ")

client.close()
