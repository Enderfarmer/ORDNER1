import random as rm 
sonderzeichen = {'.',',',':','-','!','<','>','+','*',';',}
def passwort_generieren(zeichen_anzahl:int,sonderzeichen_auch = True,):
    sonderzeichen2 = []
    if sonderzeichen_auch:
     if zeichen_anzahl % 2 == 0:
      for _ in range(zeichen_anzahl/2):
            sonderzeichen2.append(rm.choice(sonderzeichen))
    elif not zeichen_anzahl % 2 == 0:
       for _ in range(zeichen_anzahl-1):
            sonderzeichen2.append(rm.choice(sonderzeichen))

print(passwort_generieren(zeichen_anzahl=5))