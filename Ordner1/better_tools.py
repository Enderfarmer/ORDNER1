import random,time
from collections import namedtuple
class dictionary:
    def __init__(self):
        self.newdict = {}
    def plus(self,key,value):
        self.newdict[key]=value
class liste:
    def __init__(self)->list:
        self.liste_object = []
    def anhängen(self,object):
        self.liste_object.append(object)
            
