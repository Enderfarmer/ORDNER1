from random import choice
from time import sleep
s = {'s':'j'}
#We have to do it like this...
class dictionary:
    """Class description."""

    def __init__(self, )->dict:
        self.neudict = {} 



    def plus(self, key2, value2):
        try:
            self.neudict[key2] = value2
        except:
            pass
    def löschen(self, keytodel):
        try:
            del self.neudict[keytodel]
        except:
            print('Unmögliche Operation.')
    def key_print_value_in_dict(self,key):
        s = input('Schlüssel: ')
        for k, v in self.neudict.items():
            if k == s:
                return v
    


import tkinter as tk
fenster=tk.Tk()
fenster.geometry('400x300')
label = tk.Label(master=fenster,)
my_string_var = tk.StringVar()
user_input_variable_wort = tk.StringVar()
user_input_variable_übersetzung=tk.StringVar()
user_input_variable_löschen = tk.StringVar()
wörter_hinzu = {}
with open(file='wörter_vocabulary',mode='r')as ö:
    for line in ö:
        line = line.strip()
        zuordnung = line.split(' bedeutet ')
        if len(zuordnung)== 2:
            wörter_hinzu[zuordnung[0]]=zuordnung[1]
def hinzufügen():
    fenster2 = tk.Tk()
    fenster2.geometry('200x100')
    wort_entry = tk.Entry(master=fenster2,textvariable=user_input_variable_wort)
    über_entry = tk.Entry(master=fenster2,textvariable=user_input_variable_übersetzung)
    über = user_input_variable_übersetzung.get()
    wort=user_input_variable_wort.get()
    def hinzu():
        wörter_hinzu[wort]=über
        with open(file='wörter_vocabulary',mode='w')as ö:
         for _ in wörter_hinzu:
            ö.write(f'{_} bedeutet {wörter_hinzu[_]}')
        fenster2.destroy 
    button = tk.Button(master=fenster2,command=hinzu,text='Bestätigen')
    button.pack(side='bottom')
    über_entry.pack(side='bottom')
    wort_entry.pack(side='bottom')
    
    fenster2.mainloop()
def nutzen():
    fenster2 = tk.Tk()
    entry = tk.Entry(master=fenster2)
    wort = entry.get()
    label2 = tk.Label(master=fenster2,text='Geben Sie das Wort ein')
    def benutzen():
        label2.config(text=wörter_hinzu[wort])
    button = tk.Button(master=fenster2,command=benutzen,text='übersetzen')
    entry.pack()
    label2.pack()
    button.pack()
    fenster2.mainloop()
    
nutzen_radiobutton = tk.Radiobutton(master=fenster,command=nutzen,text='Wörterübersetzung')
hinzufügen_radiobutton = tk.Radiobutton(master=fenster,command=hinzufügen,text='Wörter hinzufügen')
hinzufügen_radiobutton.pack()
nutzen_radiobutton.pack()
fenster.mainloop()


