
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
        
    def delatapos(self,pos):
        count=0
        cur=self.head
        if pos==0:
            self.delatbeg()
            return

        while cur is not None and count<pos-1:
            count+=1
            cur=cur.next   

        if cur is None:
            print(f"no valid pos to del")
            return

        right=cur.next
        right=right.next
        cur.next=right

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


#search an element in the linked list
    def search(self, data):
        cur=self.head
        if cur==None:
            print(f"no element in the linked list t search")
            return
        count=0
        while cur is not None:
            if data==cur.data:
                print(f"the element found in the given linked list at the position",count)
               
                return
            cur=cur.next
            count=count+1
        if cur==None:
            print(f"element not found")


l=Linkedlist()
# l.insertatbeg(10)
# l.insertatbeg(20)
# l.insertatbeg(30)
# l.itra()
# #the above code insert at beg (one before other)
# l.insertatend(3)
# l.insertatend(2)
# l.insertatend(1)
# l.itra()
# #the above code inserts at the end (add after given ones)
# print("\n")
# l.insertatapos(4,5)
# l.itra()
# print(f"the total nodes are",l.count())
# #remove at beg
# l.delatbeg()
# l.itra()

# l.delatbeg()
# l.itra()
# print(f"the total nodes are",l.count())
# l.delatend()
# l.itra()
# print(f"the total nodes are",l.count())
# l.delatapos(0)
# l.itra()
# print(f"the total nodes are",l.count())

# l.insertatbeg(0)
# l.insertatbeg(1)
# l.insertatbeg(2)
# l.insertatbeg(3)
# l.insertatbeg(4)
l.insertatend(0)
l.insertatend(1)
l.insertatend(2)
l.insertatend(3)
l.insertatend(4)
l.insertatend(5)
l.insertatend(6)
l.itra()
print("\n")
l.itra()
# l.delatapos(4)
# l.itra()
l.search(3)
l.itra()