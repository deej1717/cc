import socket

host = socket.gethostname()
port = 6000

password = "aXsl1ms9203mdujs"

server = socket.socket()
server.bind((host, port))

server.listen(1)
conn, address = server.accept()
guess = conn.recv(1024).decode()

if guess == password:
    while True:
        command = conn.recv(1024).decode()
        if not command:
            break
        print(command)
        #Shell goes here
        response = "Dhruv"
        conn.send(response.encode())

conn.close()
