class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class Doublelinkedlist:
    def __init__(self):
        self.head=None  

    def insertatbeg(self,data):
        new=Node(data,None,self.head)
        if self.head is not None:
            self.head.prev=new
        self.head=new

    def insertatend(self,data):
        new=Node(data,None,None)
        cur=self.head
        if self.head is None:
            self.head=new
            return
        while cur.next is not None:
            cur=cur.next
        #here i have reached the last position and i need to append new node
        cur.next=new
        new.prev=cur

    def itra(self):
        cur=self.head
        if cur is None:
            print("lsit is empty")
            return
        while cur is not None:
            print(cur.data)
            cur=cur.next

l=Doublelinkedlist()
l.insertatbeg(10)
l.insertatbeg(20)
l.insertatbeg(30)
l.itra()
print("\n")
l.insertatend(5)
l.insertatend(4)
l.insertatend(3)
l.itra()
