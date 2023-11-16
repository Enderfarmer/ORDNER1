#
# Author: Artem Kort
# Date: 09.11.2023
#
from random import randint
from tkinter import Tk, Label, Entry, Button, StringVar  # The import with * is bad therefore import modules explicitely
from time import sleep

# The fenster properties
fenster = Tk()
fenster.title("  Zahlenraten  ")
fenster.geometry("300x300")


user_input_variable = StringVar()
my_string_var = StringVar()
max_random_value = 100


def random_value_game() -> None:
    """Checks that entered value  equal to random."""

    user_input = user_input_variable.get()
    random_value = randint(0, max_random_value)
    print(f"user_input {user_input}, random_value {random_value}")

    if user_input.isnumeric():
        user_number = int(user_input)
        if user_number < random_value:
            my_string_var.set(f"Zu klein!")
        elif user_number > random_value:
            my_string_var.set(f"Zu groß!")
        else:
            my_string_var.set("Herzlichen Glückwunsch! Sie haben die Zahl erraten!")
    else:
        my_string_var.set("Zahl ist nicht correct!")

    user_input_variable.set("")


my_string_var.set("Geben Sie Ihre Nummer ein")
numbers_entry = Entry(fenster, textvariable=user_input_variable, font=("Arial", 30))
submit_button = Button(fenster, text="Einreichen", command=random_value_game)
label = Label(fenster, textvariable=my_string_var, fg="purple", bg="gray")


label.pack()
numbers_entry.pack()
submit_button.pack()

# performing an infinite loop
# for the window to display
fenster.mainloop()
