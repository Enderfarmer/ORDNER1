from random import randint
from _thread import start_new_thread
from tkinter import Tk, Label, Entry, Button, StringVar, Radiobutton  # The import with * is bad therefore import modules explicitely
from time import sleep
# The fenster properties
fenster = Tk()
fenster.title("  Zahlenraten  ")
fenster.geometry("400x200")


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
        labell.config(text="Zahl ist nicht correct!")

    user_input_variable.set("")


my_string_var.set("Geben Sie die Zahl ein")
numbers_entry = Entry(master=fenster,textvariable=user_input_variable, font=("Arial", 30))
submit_button = Button(fenster, text="Einreichen", command=random_value_game)
label = Label(fenster, textvariable=my_string_var, fg="#F0E", bg="black")
numbers_entry.place(x=150,y=300,width=10, height=30)

label.pack()
labell.pack()
numbers_entry.pack()
submit_button.pack()

# performing an infinite loop
# for the window to display
fenster.mainloop()


