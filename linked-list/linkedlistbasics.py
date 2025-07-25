
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
        
class Linkedlist:
    def __init__(self):
        self.head=None

#insert
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

#delete
    def delatbeg(self):
        if self.head is None:
            print(f"No elements to delete")
            return
        
        cur=self.head
        cur=cur.next
        self.head=cur
        return
    def delatend(self):
        if self.head is None:
            print(f"No elements to delete")
            return
        cur=self.head
        while cur.next is not None:
            prev=cur
            cur=cur.next
        
        prev.next=None
        return
            

#counts the number of nodes:
    def count(self):
        cur=self.head
        if self.head==None:
            return 0
        
        count=0
        while cur:
            count+=1
            cur=cur.next
        return count
    
#function to print or iterate ove rthe linkedlist
    def itra(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next


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
print(f"the total nodes are",l.count())
#remove at beg
l.delatbeg()
l.itra()

l.delatbeg()
l.itra()
print(f"the total nodes are",l.count())
l.delatend()
l.itra()
print(f"the total nodes are",l.count())
