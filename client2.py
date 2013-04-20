# -*- coding: utf-8 -*-
import socket
from Tkinter import *

root = Tk()
root.title("Чат-хуят")

textbox = Entry()
textbox.pack()
HOST = "192.168.1.35"                
PORT = 3333            
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
while 1:
	sock.send(raw_input())
	answer = sock.recv(1024)
	print answer

