"""
In this impementation of HashMap (Dictionary) I am saving the "age" of man as value & using the man "name" as a Key.
No Collision handling
"""
class HashMap:
    def __init__(self):
        self.max = 100     # Size of list
        self.arr = [None for i in range(self.max)] # Using List Comprehension
        
#################### Hash Function ####################
    def get_hash(self, key):  
        h = 0
        for char in key:
            h += ord(char)    # ord gives us Ascii value of character
        return h % self.max
    
################# Function to Add Item in HashMap ######################
    def add_item(self, key, val):       # Using this Func we can add item using "h.additem(key, val)"
        h = self.get_hash(key)
        self.arr[h] = val
    
    def __setitem__(self, key, val):    # Using built-in operator(__setitem__) now we can add item using "h[key] = val"
        h = self.get_hash(key)
        self.arr[h] = val
           
################# Function to Retrieve/Get Item from HashMap ######################
    def get_item(self, key):        # Using this Func we can get item using "h.get_item(key)"
        h = self.get_hash(key)
        return self.arr[h]
    
    def __getitem__(self, key):     # Using built-in operator(__getitem__) now we can get item using "h[key]"
        h = self.get_hash(key)
        return self.arr[h]

################# Function to Delete Item from HashMap ######################
    def del_item(self, key):        # Using this Func we can delete item using "h.del_item(key)"
        h = self.get_hash(key)
        self.arr[h] = None
    
    def __delitem__(self, key):     # Using built-in operator(__delitem__) now we can delete item using "del h[key]"
        h = self.get_hash(key)
        self.arr[h] = None  

h = HashMap()

###### Adding item #########

h.add_item("Ali", 5)     # Adding using add_item Function

h["Najaf"] = 22           # Adding using __setitem__ 

###### Getting/Retrieving item #########

print(h.get_item("Ali"))   # Retrieving using get_item Function

print(h["Najaf"])          # Retrieving using __getitem__

###### Deleting item #########

h.del_item("Ali")          # Deleting using get_item Function

del h["Najaf"]             # Deleting using __delitem__

###### After Deleting #########
print("After Deleting")

print(h["Ali"])
print(h["Najaf"])

