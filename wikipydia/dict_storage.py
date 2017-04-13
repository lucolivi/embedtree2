### Dict Storage class to be used to load and save dicts
#It saves data in pickle format
#By Lucas V. Oliveira

import pickle

class DictStorage(dict):
    
    def __init__(self, filename):
        self.filename = filename + ".pickle"
        
        dict_list = []
        
        try:
            with open(self.filename, mode='r+b') as pickle_file:
                dict_list = pickle.load(pickle_file)
        except IOError:
            print("Failed to open " + self.filename + ". Created empty dict.")
        finally:
            super().__init__(dict_list)
    
    def save(self):
        with open(self.filename, mode='w+b') as pickle_file:
            pickle.dump(self, pickle_file)
            
  #  def __setitem__(self, key, value):
 #       #Ensure data is string 
 #       super(DictStorage, self).__setitem__(key.lower(), value)

 #   def __getitem__(self, key):
#        #Ensure data is string 
 #       return super(DictStorage, self).__getitem__(key.lower())
    
#    def has_key(self, key):
#        #Ensure data is string 
#        return super(DictStorage, self).has_key(key.lower())

if __name__ == "__main__":
    test1 = DictStorage("ae2")
    print(test1.items())
    print(test1.save())
    test1['LUCAS'] = 128
    print(test1.items())
    print(test1.save())
    print(test1['LUCAS'])
    print(test1['LUCAS'])