############################## Class Node ###################################


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
############################ Class LinkList #################################

class LinkedList:
    def __init__(self):
        self.head = None


############################## Function to Insert Node at begining #######################################

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


###################################### Function to Insert Node at End ###################################

    def insert_at_end(self, data):                      
        if self.head is None:
            node = Node(data, None)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(data, None)
            itr.next = node


############################ Function to Calculate Length of LinkedList ###################################

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count
    
    
################################ Function to Insert Node at Given Index ################################

    def insert_at_index(self, data, index):
        if index > 0 or index <= self.get_len():
            if self.head is None:                 # If 1st Node / LinkedList is Empty
                self.insert_at_begining(data)

            elif index-1 == self.get_len():       # If last Node
                self.insert_at_end(data)

            elif index < self.get_len():          # If new Node Insert anywhere in between two Nodes
                count = 1
                itr = self.head
                while count < index - 1:
                    itr = itr.next
                    count += 1
                node = Node(data, itr.next)
                itr.next = node

################################ Function to Remove Node at Given Index ################################

    def remove_at_index(self, index):
        if self.head is None:                            # If LinkedList is Empty
            print("LinkedList is Empty")                           
        elif index >= 0 and index<= self.get_len():   
            itr = self.head
            
            if index == 0:                               # If we Remove 1st Node of LinkedList
                self.head = self.head.next
                print("Node Removed Sucessfully from the Start")
            else:
                count = 0
                while itr: 
                    if count == index -1:
                        if itr.next.next is None:        # If we Remove Last Node of LinkedList
                            itr.next = None
                            print("Node Removed Sucessfully from the End")
                            break
                        else:
                            itr.next = itr.next.next     # If we Remove Node in anywhere from the center of LinkedList
                            print(f"Node Removed Sucessfully from {index} Index")
                            break   
                    else:
                        itr = itr.next
                        count += 1
                            
                                       
###################### Function to add node in Sorted(by value) Form ##############################

    def insert_by_value(self, val):
        if self.head is None:                     # If LinnkedList is Empty
            self.insert_at_begining(val)
            
        else:
            itr = self.head
            if itr.data > val:                    # if new Node value > 1st Node Value (Insertion at start)
                self.insert_at_begining(val)
                
            else:
                flag = False
                temp_itr = itr
                while itr.data < val:
                    if itr.next is None:
                        self.insert_at_end(val)   # If new Node Insert at the End
                        flag = True
                        break
                    else:
                        temp_itr = itr
                        itr = itr.next

                if flag is False:
                    node = Node(val, temp_itr.next) # If new Node Insert anywhere in between two Nodes
                    temp_itr.next = node


######################### Function to Print LinkList ##################################

    def print(self):        
        if self.head is None:
            print("Linked list is Empty")
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data)+'-->'
                itr = itr.next
            print(llstr)


######################## Main Function ###################################
if __name__ == "__main__":
    L = LinkedList()
    
    L.remove_at_index(2)           # When our List is Empty
      
    L.insert_at_end(7)
    L.insert_at_end(8)
    L.insert_at_begining(10)
    L.insert_at_begining(2)
    
 
    

    # L.insert_at_index(2,1)
    # L.insert_at_index(3,2)
    # L.insert_at_index(5,3)
    # L.insert_at_index(6,4)
    # L.insert_at_index(4,3)

    # L.insert_by_value(15)
    # L.insert_by_value(19)
    # L.insert_by_value(14)
    # L.insert_by_value(23)
    # L.insert_by_value(2)


########### Display LinkedList ##########################
L.print()

L.remove_at_index(3)

L.print()

L.remove_at_index(1)

L.print()

L.remove_at_index(0)

L.print()

############ SIze of LinkedList #########################
size = L.get_len()
print(f"Size of LinkedList is: {size}")
    
