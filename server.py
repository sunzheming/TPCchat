import socket
import threading
import datetime


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    name = sock.recv(1024)
    sock.send('Welcome, %s' %name)
    while True:
        t = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        msg = sock.recv(1024)
        if msg == 'exit' or not msg:
            break
        sock.send(t + '||' + name + ':' + msg)
        print t + '||' + name + ':' + msg
    sock.close()
    print 'Connection from %s:%s closed.' % addr

host = socket.gethostname()
port = 12349
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:

    sock, addr = s.accept()
    
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()