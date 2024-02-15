from tkinter import Tk, Frame, Label, Button
from tkinter.ttk import Progressbar, Style
import time
import Assistant
import subprocess

def new_win():
    Assistant.new_win()

def bar():
    subprocess.Popen(['python3', 'Assistant.py'])

w = Tk()
w.geometry("427x250")
w.title("Virtual Assistant - NEEL")

a = '#0174BE'

s = Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')

progress = Progressbar(w, style="red.Horizontal.TProgressbar", orient='horizontal', length=500, mode='determinate')
progress.place(x=-10, y=235)
Frame(w, width=427, height=250, bg=a).place(x=0, y=0)



b1 = Button(w, width=10, height=1, text='Get Started', command=bar, border=0, fg=a, bg='blue')
b1.place(x=170, y=200)


l1 = Label(w, text='NEEL', fg='white', bg=a)
l1.config(font=('Calibri (Body)', 25, 'bold'))
l1.place(x=80, y=80)

l2 = Label(w, text='.AI', fg='white', bg=a)
l2.config(font=('Calibri (Body)', 25,'bold'))
l2.place(x=145, y=80)

l3 = Label(w, text='Virtual Assistant', fg='white', bg=a)
l3.config(font=('Calibri (Body)', 13))
l3.place(x=80, y=110)

w.mainloop()
