class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class Doublelinkedlist:
    def __init__(self):
        self.head=None  
#insert functions
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

    def insertatapos(self,pos,data):
        #1. add at 0th position
        if pos==0:
            self.insertatbeg(data)
            return
        #2. add at any other position
        count=0
        cur=self.head
        while cur is not None and count<pos-1:
            cur=cur.next
            count+=1
        if cur is None:
            print("unable to insert at the given position as out of range")
            return
        temp=cur.next
        new=Node(data,cur,cur.next)
        cur.next=new
        if temp is not None:
            temp.prev=new


#print or iteration
    def itra(self):
        cur=self.head
        if cur is None:
            print("lsit is empty")
            return
        while cur is not None:
            print(cur.data)
            cur=cur.next

#count
    def count(self):
        count=0
        cur=self.head
        while cur is not None:
            cur=cur.next
            count+=1
        return count

l=Doublelinkedlist()
# l.insertatbeg(10)
# l.insertatbeg(20)
# l.insertatbeg(30)
# l.itra()
# print("\n")
l.insertatend(5)
l.insertatend(4)
l.insertatend(3)
# l.itra()
# print("\n")
# l.insertatapos(0,200)
# l.itra()

l.insertatapos(1,200)
l.insertatapos(4,300)
l.itra()
print(f"there are total {l.count()} nodes in the list")