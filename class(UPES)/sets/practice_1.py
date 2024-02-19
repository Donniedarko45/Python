s1=set()
s2=set()
a=int(input("enter how many fruits do you want to add in set1: "))
b=int(input("enter how many fruits do you want to add in set2: "))
for i in range(a):
    e=input("enter elements in set1: ")
    s1.add(e)
for i in range(b):
    f=input("enter elements in set2: ")
    s2.add(f)
t=set()
t=s1&s2
print("Fruits which are in both sets s1 and s2 {}".format(t))
t=s1-s2
print("Fruits only in s1 but not in s2 {}".format(t))
t=len(s1|s2)
print("all fruits from s1 and s2 {}".format(t))
