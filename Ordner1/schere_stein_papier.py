from tkinter import Tk,Label,Radiobutton,Button,StringVar,Entry
from random import choice
variants_of_game_ = {1,2,3}# Shears Paper Stone
variant_of_game = choice(variants_of_game_)
fenster = Tk()
my_string_var = StringVar()
def stein():
    label = Label(master=fenster)
    q = True|False|'Unentschieden'
    if variant_of_game is 2:
        label.config(text='Paper')
        q = False
    elif variant_of_game is 1:
        q = True
        label.config(text='Shears')
def papier():
    pass
def schere():
    pass


    