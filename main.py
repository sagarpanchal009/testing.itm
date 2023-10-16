from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
top=Tk()
top.title('example textbox')
top.geometry('300x300')
frame1 = Frame(top,background="black")
frame1.pack(expand=True,fill=BOTH)
def callfunction():
    messagebox.showinfo("HELLO PYTHON ","HELLO WORLD")

Btnok=Button(frame1,text="ok",fg="red",bg="yellow",activebackground="blue",height="2",padx="10",command=callfunction)
Btnbye=Button(frame1,text="bye",fg="red",bg="yellow",activebackground="blue",height="2",padx="10",command=callfunction)
Btnwelcome=Button(frame1,text="welcome",fg="red",bg="yellow",activebackground="blue",height="2",padx="10",command=callfunction)
Btnok.pack(side=TOP)
Btnbye.pack(side=LEFT)
Btnwelcome.pack(side=BOTTOM)
top.mainloop()