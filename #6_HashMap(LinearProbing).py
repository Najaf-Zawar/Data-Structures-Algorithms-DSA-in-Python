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

    def __setitem__(self, key, val): 
        h = self.get_hash(key)
        self.arr[h] = val
           
################# Function to Retrieve/Get Item from HashMap ######################

    def __getitem__(self, key): 
        h = self.get_hash(key)
        return self.arr[h]

################# Function to Delete Item from HashMap ######################

    def __delitem__(self, key): 
        h = self.get_hash(key)
        self.arr[h] = None  