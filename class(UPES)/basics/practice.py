"""l1=()
l2=()
n1=int(input("total no of element in tupple 1: "))
n2=int(input("total no of element in tupple 2: "))
for i in range(0,n1):
    k=int(input("enter elements: "))
    l1=l1+(k,)
print("enter elements in tuple2: ")    
for i in range(0,n2):
    m=int(input("enter elements: "))
    l1=l1+(m,)
s=()
s=l1+l2
print(s)
pos=()
for i in s:
    if i>0:
        pos=pos+(i,)
print(pos)
neg=()
for i in s:
    if i<0:
        neg=neg+(i,)
print(neg)"""


le=(10,-40,30,40,-78)
le1=tuple([x for x in le if x>0])
print(le1)
        
