### In this HashMap Implementation I am handing collision through chaining method ###
class HashMap:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]
    
#################### Hash Function ####################
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # ord gives us Ascii value of character 
        return h % self.max

################# Function to Add Item in HashMap ######################        
    def __setitem__(self,key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] =  (key,val)  
                found = True
                break
        if not found:
                self.arr[h].append((key,val)) 

################# Function to Retrieve/Get Item from HashMap ######################   
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

################# Function to Delete Item from HashMap ######################      
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


h = HashMap()

h["march 5"] = 10  # Adding key,val pair
h["march 6"] = 12
h["march 17"] = 14

print(h["march 6"])
print(h["march 17"])

del h["march 17"]     # Deleting

print(h["march 17"])  # Print after deleting



