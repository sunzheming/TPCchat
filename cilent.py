import socket


host = socket.gethostname()
port = 12349
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

name = raw_input('Your name:')
s.send(name)
print s.recv(1024)
while True:
    msg = raw_input('type something here and type Enter to sent:')
    if msg == 'exit' or not msg:
        break
    s.send(msg)
    print s.recv(1024)
s.send('exit')
s.close()





