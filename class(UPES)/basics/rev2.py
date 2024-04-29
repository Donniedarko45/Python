n=int(input("enter total no of elements: "))
l=()
for i in range(n):
    el=int(input("enter elements: "))
    l=l+(el,)
t2=()
for i in range(n):
    t2=t2+(l[n-i-1],)
print("reverse tuple: ",t2)    

