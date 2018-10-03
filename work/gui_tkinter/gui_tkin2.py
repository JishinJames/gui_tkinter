from Tkinter import *
import os
import subprocess

master = Tk()


master.title("STARCCM+")
def callback():
    print("called the callback!")
path_to=""

 

# create a menu
menu = Menu(master)
master.config(menu=menu)

helpmenu = Menu(menu)
menu.add_cascade(label="About", command=callback)

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
] #etc

variable = StringVar()
variable.set(OPTIONS[0]) # default value
#layer = PhotoImage(file ="C:\Users\JISJAME\Downloads\Benzlogo4.gif")

w= Label(master, text='Select the version',fg="black",bg="white",font='italic').grid()
w = OptionMenu(master,variable, *OPTIONS)
w.config(relief=RIDGE,width=20, bg='white')
w.grid(pady=100,padx=100)
w.rowconfigure(0,weight=1)
w.columnconfigure(0,weight=1)


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
    "13.02.011"):
        path_to=" /share/starccm/" + version+"/star/bin/starccm+"
    if version in ("6.05.021","7.01.071"):
        path_to=" share/starccm/"+version+"_new_tim/star/bin/starccm+"
    if version in ("10.04.008","10.04.009","11.04.010","11.06.010-r8","11.06.011","12.02.004","12.02.010","12.04.010","12.04.010_CTs","13.04.010"):
        path_to=" share/starccm/"+version+"/STAR-CCM+"+version+"/star/bin/starccm+"
    if version in ("12.04.010_TIG"):
        path_to=" share/starccm/12.04.010_TIG_SOLID/STAR-CCM+12.04.010/star/bin/starccm+"
        
    print ("value is:" + path_to)
     
def var_states():
    subprocess.call(["cd", "/"])
    subprocess.call(["sh", path_to])

#Button(master, text='RUN', command=ok).grid(row=2,column=0 ,sticky=W, padx=100,pady=40)
#Button(master, text='QUIT', command=master.destroy).grid(row=2, column=1,sticky=W, padx=100,pady=40)
toolbar = Frame(master, cursor='hand2', relief=SUNKEN, bd=2)
toolbar.grid(pady=0,padx=0,sticky=(N,W,E,S))
#toolbar.pack(side=BOTTOM, fill=X)
Button(toolbar, text='Quit',  command=master.destroy,bg="green" ).pack(side=RIGHT)
Button(toolbar, text='Run', command=ok,bg="green").pack(side=LEFT)


master.mainloop()
toolbar.mainloop()