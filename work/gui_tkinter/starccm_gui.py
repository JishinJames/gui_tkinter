from Tkinter import *
import Tkinter as tk
import os
import subprocess
master = tk.Tk()
master.title("Starccm+")
master.resizable(width=False, height=False)
'''
mainframe = Frame(master).grid(column=0,row=2,pady=50,sticky=W)
#mainframe.pack(pady = 100,padx = 100)#with pack it doesn't work in linux
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
    "6.05.021",
    "7.01.071",
    "7.02.008",
    "7.04.011",
    "7.06.009",
    "7.06.009-r8",
    "8.02.008",
    "8.02.011",
    "8.04.006",
    "8.04.007",
    "8.05.065",
    "8.06.005",
    "8.06.005-r8",
    "9.04.009",
    "9.06.002",
    "9.06.009",
    "9.06.009-r8",
    "9.06.010",
    "10.02.010",
    "10.02.010-r8",
    "10.02.012",
    "10.02.012-r8",
    "10.04.008",
    "10.04.009",
    "10.06.009",
    "10.06.009-r8",
    "10.06.010_cts",
    "11.02.009",
    "11.02.010_cts",
    "11.02.010_cts_v2",
    "11.02.010_cts_v3",
    "11.04.010",
    "11.04.012",
    "11.04.012-r8",
    "11.06.010",
    "11.06.010-r8",
    "12.02.004",
    "12.02.010",
    "12.02.011",
    "12.02.011-r8",
    "12.04.010",
    "12.04.010_CTs",
    "12.04.010_TIG",
    "12.04.011" ,
    "12.06.010",
    "13.02.011",
    "13.02.011-r8",
    "13.04.010"
] 

variable = StringVar(master)
variable.set(OPTIONS[0]) # default val

w = Label(master, text='Select the version',fg="white",bg="black",font='italic').grid(pady=(85,30))
#w.pack(side=TOP)
w = OptionMenu(master, variable, *OPTIONS)
w.config(relief=RIDGE,width=20,bg='white')
w.grid(pady=10)

def ok():
    version=variable.get()
    if version in ("7.02.008",
    "7.04.011",
    "7.06.009",
    "7.06.009-r8",
    "8.02.008",
    "8.02.011",
    "8.04.006",
    "8.04.007",
    "8.05.065",
    "8.06.005",
    "8.06.005-r8",
    "9.04.009",
    "9.06.002",
    "9.06.009",
    "9.06.009-r8",
    "9.06.010",
    "10.02.010",
    "10.02.010-r8",
    "10.02.012",
    "10.02.012-r8",
    "10.06.009-r8",
    "10.06.010_cts",
    "11.02.009",
    "11.02.010_cts",
    "11.02.010_cts_v2",
    "11.02.010_cts_v3",
    "11.04.012",
    "11.04.012-r8",
    "11.06.010",
    "12.02.011",
    "12.02.011-r8",
    "12.04.011" ,
    "12.06.010",
    "13.02.011",
    "13.02.011-r8"):
        path_to="/share/starccm/" + version+"/star/bin/starccm+"
    if version in ("6.05.021","7.01.071"):
        path_to="/share/starccm/"+version+"_new_tim/star/bin/starccm+"
    if version in ("10.04.008","10.04.009","11.04.010","11.06.010-r8","11.06.011","12.02.004","12.02.010","12.04.010","12.04.010_CTs","13.04.010"):
        path_to="/share/starccm/"+version+"/STAR-CCM+"+version+"/star/bin/starccm+"
    if version in ("12.04.010_TIG"):
        path_to="/share/starccm/12.04.010_TIG_SOLID/STAR-CCM+12.04.010/star/bin/starccm+"
        
    #print ("value is:" + path_to)
     

    subprocess.call(["cd", "/"])
    subprocess.call(["sh", path_to])

toolbar = Frame(master, cursor='hand2', relief=SUNKEN)
toolbar.grid(pady=30)
#toolbar.grid(pady=50,padx=196,sticky=(N,W,E,S))
Button(toolbar, text='Run', command=ok,bg="white").pack()

master.mainloop()
toolbar.mainloop()
