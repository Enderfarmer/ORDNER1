from random import choice
kandidaten = {'1':'Aaron H.','2':'Aaron R.','3':'Arti','4':'Fahrican','5':'Akram','6':'Lukas V.','7':'Lin','8':'Yuna','9':'Luis','10':'Narrendra'}
for i in range(4):  
    sus = set(kandidaten.keys())
    yell = choice(sus)
    if sus in kandidaten.items():
        print(kandidaten[sus])
        
         
              
