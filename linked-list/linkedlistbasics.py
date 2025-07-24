
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
        
class Linkedlist:
    def __init__(self):
        self.head=None

    def insertatbeg(self,data):
        k=Node(data,self.head)
        self.head=k

    def insertatend(self,data):
        k=Node(data,None)

        if self.head is None :
            self.head=k
            return
        current=self.head
        while current.next is not None:
            current=current.next
        
        current.next=k

    
    def itra(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

    def insertatapos(self,data,pos):
        if pos==0:
            self.insertatbeg(data)
            return
        count=0
        current=self.head
        while current is not None and count < pos-1:
            current = current.next
            count += 1

        if current is None:
            print(f"unable to insert as position is not in range")
            return

        k=Node(data,current.next)
        current.next=k

l=Linkedlist()
l.insertatbeg(10)
l.insertatbeg(20)
l.insertatbeg(30)
l.itra()
#the above code insert at beg (one before other)
l.insertatend(3)
l.insertatend(2)
l.insertatend(1)
l.itra()
#the above code inserts at the end (add after given ones)
print("\n")
l.insertatapos(4,88)
l.itra()