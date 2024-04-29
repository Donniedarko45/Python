s1={'red','yellow','orange','blue'}
s2={'violet','blue','purple'}
print(s1.add("green"))
print(s1.discard("blue"))
print(s2.remove("violet"))
print(s2.update("green","brown","black"))
print(s1.pop())
print(s1.union(s2))
#bitwise operations...
print(s1|s2) #union
print(s1&s2) #common element
print(s2.difference(s1)) #from s2 remove element of s1  which is also present in s2  we can also write s2-s1
print(s1.issubset(s2))  #kya s1 subset hai s2 ka

