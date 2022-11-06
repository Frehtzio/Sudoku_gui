class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
        


a = Node("A")

b = Node("B")

c = Node("C")

d = Node("D")

z = Node("Z")
a.next = b
b.next = c
c.next = d
d.next = z

uno = Node(1)
dos = Node(2)
uno.next = dos

def zipper_lists(head_1, head_2):
    tail = head_1
    current1 = head_1.next
    current2 = head_2
    count = 0
    while current1 and current2:
        if count % 2 == 0:
            head_1.next = current2
            current2 = current2.next
            head_1 = head_1.next
          
        else:
            
            head_1.next = current1
            current1 = current1.next
            head_1 = head_1.next

        count +=1 
    if current1 != None:
        
        head_1.next = current1
    if current2 != None:
        head_1.next = current2
        
    
    return tail


        
    

def d(head):
    if head == None:
        return 
    print(head.val)
    d(head.next)
    
    
s = zipper_lists(a,uno)
print(d(s))