s=set()
n=int(input('enter how many elements do you want to add in set: '))
for i in range(n):
    a=int(input('enter elements: '))
    s.add(a*a*a)    
print(s)
