import random as rm 
print('Spiel: Zahlenraten. Bitte geben Sie eine Zahl zwischen 0 und 100 ein.')
while True:
     rand = rm.randint(0,100)
     x = int(input('Zahl: '))
     if x < rand:
        print('Zu klein!')
     elif x > rand:
        print('Zu groß!')
     else:
        print('Herzlichen Glückwunsch! Sie haben die Zahl erraten!')
        break 