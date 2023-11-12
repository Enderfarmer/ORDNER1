from random import choice
vocabulary = {}
known = {}
MENÜ = '''
(n)eues Wort
(i)n gelernt hinzufügen
(l)esen
(a)bfragen
(w)egmachen
(e)nde
'''
print(MENÜ)
def hinzufügen(wort,übersetzung):
    vocabulary[wort]=übersetzung
    print('Erfolgreich erfüllt!')


def in_gelernt():
    known=known+{vocabulary}
    vocabulary.clear
    print('Erfolgreich erfüllt!')
def abfragen():
    o = choice(vocabulary.values())|choice(vocabulary.keys)
    print(o)
    eingabe = input('Wort: ')
    if eingabe == vocabulary.values(o):
        print('Sehr gut')
    else:
        print('Falsch!')
def entfernen(a,b):
    del vocabulary[a,b]
    print('Erfolgreich ausgefüllt!')



while True:
    ss=input('Option: ')
    if ss in'nN':
        hinzufügen(input('Vokabel: '),input('Übersetzung: '))
    elif ss in 'Ll':
        print(vocabulary)
    elif ss in 'Aa':
        abfragen
    elif ss in'iI':
        in_gelernt
    elif ss in 'Ww':
        entfernen(input('Schlüssel: '),input('Wert dieses Schlüssels: '))
    elif ss in 'eE':
        print('Bis bald!')  
        break
    
