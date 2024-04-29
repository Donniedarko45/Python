
d={}
n=int(input("enter no of elements: "))
for i in range(n):
    k=int(input("enter key: "))
    v=int(input("enter value: "))
    d.update({k:v}) 
print(d)
s=0
for i in d:
    print(d[i])
for i in d.values():
    s=s+i
print(s)    


    
    
