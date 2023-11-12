
#We have to do it like this...
class dictionary:
    """Class descrition."""

    def __init__(self, default_dict=None):
        self.neudict = {} if default_dict is None else default_dict



    def plus(self, key2, value2):
        self.neudict[key2] = value2
    def löschen(self, keytodel):
        try:
            del self.neudict[keytodel]
        except:
            print('Unmögliche Operation.')
    def key_print_value_in_dict(self,key):
        s = input('Schlüssel: ')
        for k, v in self.neudict.items():
            if k == s:
                print(v)
 

