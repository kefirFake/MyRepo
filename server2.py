# -*- coding: utf-8 -*-
import socket, string
 
def do_something(x):
	lst = map(None, x);
	lst.reverse();
	return string.join(lst, "")
 
HOST = ""                 # localhost
PORT = 3333
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
while 1:
	print "Listen port 3333"
	srv.listen(1)             
	sock, addr = srv.accept()
	while 1:
		pal = sock.recv(1024)
		if not pal: 
			break
		print "Recived from %s:%s:" % addr, pal
		lap = do_something(pal)
		print "Sended %s:%s:" % addr, pal
		sock.send(pal)
	sock.close()
