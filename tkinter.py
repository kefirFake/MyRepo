# -*- coding: utf-8 -*-
from Tkinter import *

def add(x):
	print raw.get()
	raw.delete(0, END)
	
def smiley(event):
     cv = Canvas(height=30,width=30)
     cv.create_oval(1,1,29,29,fill="yellow")
     cv.create_oval(9,10,12,12)
     cv.create_oval(19,10,22,12)
     cv.create_polygon(9,20,15,24,22,20)
     text.window_create(CURRENT,window=cv)

root = Tk()
root.title("Чат-хуят")

text = Text(root, state=DISABLED)
tx.bind('<Button-1>',smiley)
text.pack()

raw = Entry(root, width=70)
raw.bind('<Key-Return>', add)
raw.pack()

root.mainloop()
