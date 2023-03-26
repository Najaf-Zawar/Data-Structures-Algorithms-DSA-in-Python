"""
Queue Implementation using list in python is not recommended b/c of allocaton of new memory when new index added 
but also the copying of existing elements.

*Recommended approch to implement Queue is by using "collection.deque".

Collection.deque:- deque(Double ended Queue)
            Generalization of stack & queue and are implemented using doubly LinkedList.
"""

from collections import deque

class Queue:
    def __init__(self):
        self.que = deque()   # Stack created using deque
    
    
    def enqueue(self, val):    # Push(Insert) Value in Stack
        self.que.appendleft(val)
        print("Value Added Sucessfully in Queue")


    def dequeue(self):          # Pop(Remove) value from Stack
        if self.is_Empty():
            print("Queue is Empty")
        else:
            pop_val = self.que.pop()
            print("Value Removed Sucessfully from Queue")
            return pop_val  
 
    
    def peek(self):          # Print Top(Last Entered value) of Stack
        if self.is_Empty():
            print("Queue is Empty")
        else:
            return self.que[-1]
 
    
    def is_Empty(self):      # Check if Stack is empty / not 
        return len(self.que) == 0
 
    
    def size(self):          # Return Size of Stack
        return len(self.que)
    

q = Queue()
q.enqueue(5)
q.enqueue(12)
q.enqueue(37)
q.enqueue(55)

print()
print(f"Size of Queue is: {q.size()}") # Return size of Stack

q.dequeue() # Pop the value

print(q)
print(f"Size of Queue is: {q.size()}") 

print(f"Top of Queue is: {q.peek()}") # Return Top(Last Entered value) of Stack

q.dequeue()
q.dequeue()
q.dequeue()

print(f"Size of Queue is: {q.size()}")

print(f"Top of Queue is: {q.peek()}")