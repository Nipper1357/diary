import tkinter as tk
import datetime as dt
from tkinter import messagebox
import sys

flag = False
path=str(dt.date.today()) + ".txt"

def SaveValue(event):
	global flag
	flag = True
	result = text.get("1.0", "end -1c")
	#print(flag)
	#print(result)
	
	with open(path, mode="w") as f:
		f.write(result)

def callback():
	if flag:
		root.destroy()
	elif messagebox.askokcancel("note","quit without saving?"):
		root.destroy()

def openning():
	try:
		with open(path, mode="r") as f:
			return(f.read())
	except FileNotFoundError as e:
		return("")
	
root = tk.Tk()
root.title("dialy "+str(dt.date.today()))
root.protocol("WM_DELETE_WINDOW", callback)
root.bind("<Control-s>", SaveValue)

text = tk.Text(root)
text.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
text.insert("1.0", openning())

button = tk.Button(text=u"Save")
button.bind("<Button-1>", SaveValue)
button.grid(sticky=(tk.S, tk.E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()