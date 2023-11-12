planets = {'Merkur', 'Venus', 'Erde', 'Mars', 'Jupiter',
           'Saturn', 'Uranus', 'Neptun'}

print('Zähle die Planeten unseres Sonnensystems auf!')
while  planets != {}:
    inpt = input('Planet: ')
    if inpt in planets:
        planets = planets - {inpt}
        print('Richtig!')
        
else:
    print('Leider falsch!')
print(planets)