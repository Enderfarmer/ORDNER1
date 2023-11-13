import re
import wörter, tkinter


seiten = wörter.dictionary() # here dictionary.__init__() is called
#print(f"seiten {seiten.neudict}")

#non_default_dict = {"first": 1 , "second": 2}


#non_default_seiten = wörter.dictionary(default_dict=non_default_dict) # here dictionary.__init__() is called
#print(f"seiten {non_default_seiten.neudict}")

#x = 1 
# this 'f' is a fstring with a empty place that can be filled with something
#blablabla = f'60 Minutes = {x} hour.'
#blablabla.format(x)
#print(blablabla)
ümenu = '''
(h)inzufügen
(l)öschen
(le)sen
(e)nde
'''
while True: 
    print(ümenu)
    s = input('Methode: ')
    if s in'hH':
       try:
        seiten.plus(input('Nummer: '), input('Inhalt: '))
       except:
        print('Leider nicht gelungen.')
    elif s in 'lL':
       seiten.löschen(input('Welche Seite löschen? '))
    elif s in 'Le' or 'le' or'LE'or'lE':
       print(seiten[input('Seite: ')])
    elif s == 'eE':
        print('Bis bald!')
        break