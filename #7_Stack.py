"""
Stack Implementation using list in python is not recommended b/c of allocaton of new memory when new index added 
but also the copying of existing elements.

*Recommended approch to implement stack is by using "collection.deque".

Collection.deque:- deque(Double ended Queue)
            Generalization of stack & queue and are implemented using doubly LinkedList.
"""

from collections import deque

# obj = deque()
# print(dir(obj))  # Show all the methods

class Stack:
    def __init__(self):
        self.stk = deque()   # Stack created using deque
    
    
    def push(self, val):    # Push(Insert) Value in Stack
        self.stk.append(val)
        print("Value Added Sucessfully in Stack")


    def pop(self):          # Pop(Remove) value from Stack
        if self.is_Empty():
            print("Stack is Empty")
        else:
            pop_val = self.stk.pop()
            print("Value Removed Sucessfully from Stack")
            return pop_val  
 
    
    def peek(self):          # Print Top(Last Entered value) of Stack
        if self.is_Empty():
            print("Stack is Empty")
        else:
            return self.stk[-1]
 
    
    def is_Empty(self):      # Check if Stack is empty / not 
        return len(self.stk) == 0
 
    
    def size(self):          # Return Size of Stack
        return len(self.stk)
    

s = Stack()
s.push(5)
s.push(12)
s.push(37)
s.push(55)

print(f"Size of Stack is: {s.size()}") # Return size of Stack

s.pop() # Pop the value

print(f"Size of Stack is: {s.size()}") 

print(f"Top of Stack is: {s.peek()}") # Return Top(Last Entered value) of Stack

s.pop()
s.pop()
s.pop()

print(f"Size of Stack is: {s.size()}")

print(f"Top of Stack is: {s.peek()}")






    
