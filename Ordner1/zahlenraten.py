from random import randint
from tkinter import Tk, Label, Entry, Button, StringVar, Radiobutton  # The import with * is bad therefore import modules explicitely
# The fenster properties
fenster = Tk()
fenster.title("  Zahlenraten  ")
fenster.geometry("400x300")
user_input_variable = StringVar()
my_string_var = StringVar()
max_random_value = 100
labell = Label(master=fenster,font=('Arial',30))


def random_value_game() -> None:
    """Checks that entered value  equal to random."""

    user_input = user_input_variable.get()
    random_value = randint(0, max_random_value)
    

    if user_input.isnumeric():
        user_number = int(user_input)
        if user_number < random_value:
            labell.config(text=f"Zu klein!")
        elif user_number > random_value:
           labell.config(text=f"Zu groß!")
        else:
            labell.config(text="Herzlichen Glückwunsch! Sie haben die Zahl erraten!")
    else:
        labell.config(text="Unmöglich")

    user_input_variable.set("")


my_string_var.set("Geben Sie die Zahl ein")
numbers_entry = Entry(master=fenster,textvariable=user_input_variable, font=("Arial", 30))
submit_button = Button(fenster, text="Einreichen", command=random_value_game)
label = Label(fenster, textvariable=my_string_var, fg="#F0E", bg="black")
mystringvar = StringVar()
ll = Label(master=fenster,text='                                          ',)
lll= Label(master=fenster,text='                                          ')
def gelb():
    fenster.configure(bg='#FF0')
    ll.config(fg='#FF0')
    lll.config(fg='#FF0')
    s.config(bg='#FF0',fg='black')
    l.config(bg='#FF0',fg='black')
    b.config(bg='#FF0',fg='black')
s = Radiobutton(master=fenster,bg='black',fg='white', text='Gelber Hintergrund',command=gelb,variable=mystringvar)
def lila():
    fenster.configure(bg='purple')
    ll.config(fg='purple')
    lll.config(fg='purple')
    s.config(bg='purple',fg='black')
    l.config(bg='purple',fg='black')
    b.config(bg='purple',fg='black')
l = Radiobutton(master=fenster,bg='black',fg='white',text='Violetter Hintergrund',command=lila,variable=mystringvar)
def blau():
    ll.config(fg='blue')
    lll.config(fg='blue')
    fenster.configure(bg='blue')
    s.config(bg='blue',fg='black')
    l.config(bg='blue',fg='black')
    b.config(bg='blue',fg='black')
b = Radiobutton(master=fenster,bg='black',fg='white',text='Blauer Hintergrund',command=blau,variable=mystringvar)
fenster.configure(bg='black')
l.place(x=5,y=350)
b.place(x=5,y=320)
s.place(x=255,y=290)
ll.pack(side='left')
lll.pack(side='right')
label.pack()
labell.pack()
l.pack()
b.pack()
s.pack()
submit_button.pack(side="bottom")
numbers_entry.pack(side="bottom")
# performing an infinite loop
# for the window to display
fenster.mainloop()