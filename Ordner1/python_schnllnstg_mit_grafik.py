import re
import tkinter



fenster = tkinter.Tk(screenName='  Python 3 Schnelleinstieg  ')
eingabe = tkinter.Entry(master=fenster,font=('Arial', 25))

label = tkinter.Label(master=fenster,font='Arial')
class dictionarry:
    def __init__(self)->dict:
        self.newdict = {}
    def löschenn(self,key_to_delete):
           del self[eingabe.get()]
    def plus(self):
        eingabe2= tkinter.Entry(master=fenster,font=('Arial', 25))
        self[eingabe.get()]=eingabe2.get()
    def lesen(self):
         label = tkinter.Label(master=fenster, font=('Arial'),text=self)
ö = tkinter.StringVar()
addd = tkinter.Radiobutton(master=fenster,text=' neu ',command=dictionarry.__init__(),variable=ö)
löschen = tkinter.Radiobutton(master=fenster,text=' löschen ',command=dictionarry.__init__(),variable=ö)