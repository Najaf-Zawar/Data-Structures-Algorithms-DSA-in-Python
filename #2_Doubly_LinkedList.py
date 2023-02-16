############################## Class Node ###################################


class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

############################ Class LinkList #################################


class Doubly_LinkedList:
    def __init__(self):
        self.head = None


############################## Function to Insert Node at begining #######################################


    def insert_at_begining(self, data):
        if self.head is None:  
            node = Node(None, data, self.head)
            self.head = node
        else:
            node = Node(None, data, self.head)
            self.head.prev = node
            self.head = node

############################## Function to Insert Node at End #######################################

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(None, data, None)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
                
            node = Node(itr, data, None)
            itr.next = node
            
            
############################ Function to Calculate Length of LinkedList ###################################
    def get_len(self):
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count    
            
            

################################ Function to Insert Node at Given Index(Indexing starts from 0)################################
    def insert_at_index(self, data, index):
        if index < 0 or index > self.get_len():
            print("Enter valid Index")
        else:
            itr = self.head
            if index == 0:                          # If 1st Node
                self.insert_at_begining(data)
                print(f"Node Inserted Sucessfully at Index {index}")
            elif index == self.get_len():           # If last Node
                 self.insert_at_end(data)
                 print(f"Node Inserted Sucessfully at Index {index}")
            else:
                count = 0
                while itr:
                    if count == index-1:            # If new Node Insert anywhere in between two Nodes
                        node = Node (itr, data, itr.next)
                        itr.next = node  
                        if node.next:
                            node.next.prev = node
                            itr.next = node
                            print(f"Node Inserted Sucessfully at Index {index}")
                            break  
                    itr = itr.next
                    count += 1    
                    
                    
################################ Function to Insert Node at Given Index(Indexing starts from 0) ################################
    def remove_at_index(self,index):
        if self.head is None:
            print("LinkedList is Empty")                    # If LinkedList is Empty
        elif index >= 0 or index < self.get_len():
            itr = self.head
            if index == 0:                                  # If we Remove 1st Node of LinkedList
                self.head = self.head.next
                self.head.prev = None
                print("Node Removed Sucessfully from the Start")
            elif index == self.get_len()-1:                 # If we Remove last Node of LinkedList
                while itr.next:
                    itr = itr.next
                itr = itr.prev
                itr.next = None
                print("Node Removed Sucessfully from the End")
            else:
                count = 0
                while itr:
                    if count == index:                     # If we Remove Node in anywhere from the center of LinkedList
                        itr.prev.next = itr.next
                        itr.next.prev = itr.prev
                        print(f"Node Removed Sucessfully from {index} Index") 
                        break
                    count += 1
                    itr = itr.next        
        else:
            print("Invalid Index")           
######################### Function to Print LinkList ##################################

    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.data) + "-->"
                itr = itr.next
            print(llstr)


######################## Main Function ###################################
if __name__ == "__main__":
    
    L = Doubly_LinkedList()
    # L.insert_at_begining(52)
    # L.insert_at_begining(32)
    # L.insert_at_end(55)
    # L.insert_at_end(76)
    
    L.insert_at_index(4, 0)
    L.insert_at_index(5, 1)
    L.insert_at_index(7, 2)
    L.insert_at_index(8, 2)
    L.insert_at_index(22, 3)
    
    
    L.print()
    size = L.get_len()
    print(f"Size of LinkedList is: {size}")
    
    L.remove_at_index(0)
    L.print()
    size = L.get_len()
    print(f"Size of LinkedList is: {size}")
    
    L.remove_at_index(3)
    L.print()
    size = L.get_len()
    print(f"Size of LinkedList is: {size}")
    
    L.remove_at_index(1)
    L.print()
    size = L.get_len()
    print(f"Size of LinkedList is: {size}")
    
    
    
