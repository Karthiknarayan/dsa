class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class Doublelinkedlist:
    def __init__(self):
        self.head=None
    
    def insertatbeg(self,data):
        new=Node(data,self.head,None)
        if self.head is not None:
            self.head.prev=new
        self.head=new
    
    def insertatend(self,data):
        new=Node(data,None,None)
        if self.head is None:
            self.head=new
            return
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=new
        new.prev=cur

    def itra(self):
        cur=self.head
        if self.head is None:
            print("List is empty")
            return
        while cur is not None:
            print(cur.data)
            cur=cur.next

l=Doublelinkedlist()
l.insertatbeg(10)
l.insertatbeg(20)
l.insertatbeg(30)
l.itra()
