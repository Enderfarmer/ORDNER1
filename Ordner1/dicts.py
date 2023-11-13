riddles = {'1': 'String1', '2': 'String2', '3':'String3'}
x = input('Rätsel: ')
for k, v in riddles.items():
    if k == x:
        print(v)
