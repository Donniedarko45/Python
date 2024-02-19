n=5
t=()
for i in range(0,5):
    e=int(input("enter elements: "))
    t=t+(e,)
print(t)

#for sum
sum=0
for i in t:
    sum+=i
print(sum)    