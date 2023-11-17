import tkinter as tk
fenster = tk.Tk()
eingabe = tk.Entry(master=fenster, font=('Arial'))
# Set window size
fenster.geometry("300x200")

def farbfüllung():
    k = eingabe.get()
    # This one is used to make sus things with the window itself, without the Label
    fenster.configure(background=k)


button = tk.Button(master=fenster, command=farbfüllung, text='Farbe anzeigen',fg='white',bg='black')

button.pack(side='bottom')
eingabe.pack(side='bottom')
fenster.mainloop()