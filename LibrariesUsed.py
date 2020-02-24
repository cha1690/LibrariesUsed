import tkinter
from tkinter import *
import backend
window = tkinter.Tk()

l1 = tkinter.Label(window, text="Name").grid(row=0, column=0)

l2 = tkinter.Label(window, text="ProjectUsed").grid(row=0, column=2)

l3 = tkinter.Label(window, text="Description").grid(row=1, column=0)

title_text = StringVar()
e1 = tkinter.Entry(window, textvariable=title_text).grid(row=0, column=1)

project_used_text = StringVar()
e2 = tkinter.Entry(window, textvariable=project_used_text).grid(row=0, column=3)

description_text = StringVar()
e3 = tkinter.Entry(window, textvariable=description_text).grid(row=1, column=1)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = tkinter.Button(window, text="View all", fg="black", bg="grey", width=8, command=backend.view_all).grid(row=2, column=3)

b2 = tkinter.Button(window, text="Search Entry", fg="black", bg="grey", width=8).grid(row=3, column=3)

b3 = tkinter.Button(window, text="Add Entry", fg="black", bg="grey", width=8).grid(row=4, column=3)

b4 = tkinter.Button(window, text="Update", fg="black", bg="grey", width=8).grid(row=5, column=3)

b5 = tkinter.Button(window, text="Delete", fg="black", bg="grey", width=8).grid(row=6, column=3)

b6 = tkinter.Button(window, text="Close", fg="black", bg="grey", width=8).grid(row=7, column=3)

window.mainloop()
