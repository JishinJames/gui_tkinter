# coding : utf9
from Tkinter import *
import Tkinter as tk
import os
import subprocess
import random
import time

subprocess.call(["sh", "ansa.sh"])

#os.system("test \"$?BASH_VERSION\" = \"0\" || eval \'setenv() { export \"$1=$2\"; }\'")
#os.system("setenv ANSA_SRV \"srtia004.in623.corpintra.net\"")

master = tk.Tk()
master.title("ANSA")

master.resizable(width=False, height=False)

'''
mainframe = Frame(master).grid(column=0,row=2,pady=50,sticky=W)
mainframe.pack(pady = 100,padx = 100)#with pack it doesn't work in linux
'''


path_to=""

''' create a menu'''
menu = Menu(master)
master.config(menu=menu)#bg="#aceda1")
master.columnconfigure(0,weight=1)
#master.rowconfigure(0,weight=1)

image = tk.PhotoImage(file="finalbenz.gif")
width = image.width()
height = image.height()
master.geometry("%sx%s"%(width, height))
background_label = tk.Label(master, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
helpmenu = Menu(menu)
menu.add_command(label="Quit", command=master.destroy)
#helpmenu.add_command(label="About...", command=callback)


OPTIONS = [
	"14.0.2",
	"14.0.3",
	"14.1.0",
	"14.1.1",
	"15.0.0",
	"15.0.1",
	"15.1.1",
	"15.1.2",
	"15.2.0",
	"15.2.4",
	"15.3.3",
	"16.0.0",
	"16.0.3",
	"16.1.0",
	"16.2.0",
	"16.2.1",
	"16.2.3",
	"16.2.4",
	"17.0.1",
	"17.0.2",
	"17.0.4",
	"17.1.1",
	"17.1.3",
	"18.1.0",
	"18.1.1"
]

variable = StringVar(master)
variable.set(OPTIONS[0]) # default val

w = Label(master, text='Select the version',fg="white",bg="black",font='italic').grid(pady=(85,30))
w = OptionMenu(master, variable, *OPTIONS)
w.config(relief=RIDGE,width=20,bg='white')
w.grid(pady=10)


def ok():
    version=variable.get()
    if version in (
	"14.0.2",
        "14.0.3",
        "14.1.0",
        "14.1.1",
        "15.0.0",
        "15.0.1",
        "15.1.1",
        "15.1.2",
        "15.2.0",
        "15.2.4",
        "15.3.3",
        "16.0.0",
        "16.0.3",
        "16.1.0",
        "16.2.0",
        "16.2.1",
        "16.2.3",
        "16.2.4",
        "17.0.1",
        "17.0.2",
        "17.0.4",
        "17.1.1",
        "17.1.3",
        "18.1.0",
        "18.1.1"
	"14.0.3",
        "14.1.0",
        "14.1.1",
        "15.0.0",
        "15.0.1",
        "15.1.1",
        "15.1.2"):
	path_to="/share/beta_cae_systems/"+version+"/ansa_v"+version+"/ansa64.sh"
	#print ("value is:" + path_to)

    #os.system("test \"$?BASH_VERSION\" = \"0\" || eval \'setenv() { export \"$1=$2\"; }\'")
    #os.system("setenv ANSA_SRV \"srtia004.in623.corpintra.net\"")
    os.system("cd /")
    #subprocess.call(["cd", "/"])
    if version in (
	"14.0.2"):
	subprocess.call([path_to])
    else:	
	subprocess.call(["sh", path_to])

toolbar = Frame(master, cursor='hand2', relief=SUNKEN)
toolbar.grid(pady=30)
#toolbar.grid(pady=50,padx=196,sticky=(N,W,E,S)
Button(toolbar, text='Run', command=ok,bg="white").pack()

master.mainloop()
toolbar.mainloop()

