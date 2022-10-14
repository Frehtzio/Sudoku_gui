"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

from threading import currentThread
from tkinter.messagebox import NO


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        if position == 1:
            return current
        for i in range(position - 1):
            if not current.next:
                return None
            current = current.next
            
        return current
            
            
        
    
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        new =new_element
        if position == 1:
            new.next = current
            self.head = new
            return self.head
        for i in range(position - 2):
            current = current.next
        new.next = current.next
        current.next = new
        
    


    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head 
        if value == 1:
            self.head = current.next
        for i in range(value - 1):
            current = current.next
        try:
            temp = current.next.next
            current.next = temp
            
        except:
            return None
            
        
        
        

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1) # 1
ll.append(e2)#2
ll.append(e3)#3

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

ll.insert(e4,3)
# Should print 4 now
print( ll.get_position(3).value)



# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)