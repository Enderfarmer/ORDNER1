import tkinter as tk
fenster = tk.Tk()
user_input_variable = tk.StringVar()
eingabe = tk.Entry(master=fenster, font=('Arial'),textvariable=user_input_variable)
# Set window size
fenster.geometry("300x200")

def farbfüllung():
    user_input = user_input_variable.get()
    # This one is used to make sus things with the window itself, without the Label
    fenster.configure(background=user_input)


button = tk.Button(master=fenster, command=farbfüllung, text='Farbe anzeigen',fg='white',bg='black')

button.pack(side='bottom')
eingabe.pack(side='bottom')
fenster.mainloop()