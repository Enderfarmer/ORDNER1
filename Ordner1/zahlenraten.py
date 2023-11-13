from random import randint
from tkinter import *
from _thread import start_new_thread
from time import sleep
fenster = Tk(screenName='  Zahlenraten  ')
label = Label(master=fenster,text='',fg ='purple',bg='black')
f = StringVar()
fenster.geometry('300x300')
def null_einhundert():
 x = Entry(master=fenster2, font=('Arial',30))
 if not x == '':
  sleep(9)
  
  fenster.destroy
  fenster2 = Tk(screenName='  Zahlenraten  ')
  label2 = Label(master=fenster2)
  rand = randint(0,100)
  while True:
     
     s = int(x.get())
     if s < rand:
        label2.config(text='Zu klein!', font=('Arial', 30))
     elif s > rand:
        label2.config(text='Zu groß!', font=('Arial', 30))
     else:
        label2.config(text='Herzlichen Glückwunsch! Sie haben die Zahl erraten!', font=('Arial', 30))
        break 
def null_zehn():
   fenster.destroy
   fenster3 = Tk(screenName='  Zahlenraten  ')
   rand = randint(0,10)
   x = Entry(master=fenster3, font=('Arial',30))
   while True:
     s = int(x.get())
     if s < rand:
        label.config(text='Zu klein!')
     elif s > rand:
        label.config(text='Zu groß!')
     else:
        label.config(text='Herzlichen Glückwunsch! Sie haben die Zahl erraten!')
        break 
def null_zehn2():
   start_new_thread(null_zehn,())
def null_hundert2():
   start_new_thread(null_einhundert,())
hndrt = Radiobutton(master=fenster,command=null_hundert2)
zn = Radiobutton(master=fenster,command=null_zehn2)
label.pack()
zn.pack()
hndrt.pack()
fenster.mainloop()
 