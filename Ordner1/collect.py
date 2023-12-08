from collections import namedtuple
# The namedtuple is used for named collections where every element has a value definition, it's kind of 'class'
# But there have to be all the names!
# This is UNIQUE!
# Example:
Buch = namedtuple('Buch',['Autor','Beschreibung'])
buch = Buch(Autor='Michael Weigend',Beschreibung='Python Tricks')
# The value can be shown. Like this
print(buch.Autor)