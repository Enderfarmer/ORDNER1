from tkinter import Tk,Label,Radiobutton,Entry,StringVar,Button
from time import sleep
fenster = Tk(screenName='Planetenabfragen')
my_string_var = StringVar()
label = Label(master=fenster,text='Gib die Planeten nach der Reihenfolge ein.',)
planets=['Merkur','Venus','Erde','Mars','Jupiter','Saturn','Uranus','Neptun']
user_input_variable = StringVar()
fenster.geometry('400x300')
label2 = Label(master=fenster,)
def colour_change():
    while True:
        fenster.after(ms=250,func=button.config(fg=colours[0]))
        colours2.append(colours[0])
        del colours[0]
        if colours == []:
            colours.append(colours2[0])
def planeten_abfragen()->None:
    user_input= user_input_variable.get()
    if planets != []:
        if user_input == planets[0]:
            label2.config(text='Richtig! Mach weiter!')
            del planets[0]
            user_input_variable.set('')
        elif user_input!= planets[0]:
            label2.config(text=f'{user_input} ist falsch oder {user_input} ist noch nicht dran.')
            user_input_variable.set('')
        else:
            pass
    elif planets == []:
        label.config(text='Sehr gut!')
        label2.config(text='')
        sleep(3)
        fenster.destroy
colours = ['red','orange','yellow','green','blue','purple']
colours2 = []
mystringvar = StringVar()
radiobutton = Radiobutton(master=fenster,text='Farben wechseln',command=colour_change,variable=mystringvar)
button = Button(master=fenster,text='Bestätigen',command=planeten_abfragen,bg='black',fg='white')
llabell=Label(master=fenster,text='                                ')
lllabelll=Label(master=fenster,text='                               ')
entry = Entry(master=fenster,textvariable=user_input_variable,font=('Arial',20))
label.pack(side='top')
label2.pack(side='top')
button.pack(side='bottom')
lllabelll.pack(side='right')
llabell.pack(side='left')
entry.pack(side='bottom')
radiobutton.pack(side='left')
fenster.mainloop()
