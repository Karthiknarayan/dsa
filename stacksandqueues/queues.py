from collections import deque

a=deque()
#queue follows fifo

a.append(1)
a.append(2)
a.append(3)
#1----2------3
print(a)

a.pop()
#1---2
print(a)

#removes first person
a.popleft()
print(a)