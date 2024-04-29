s1={'red','yellow','orange','blue'}
s2={'violet','blue','purple'}
s1.add("green")
s1.discard("blue")
s2.remove("violet")
s2.update("green","brown","black")
s1.pop()
s1.union(s2)
#bitwise operations...
s1|s2 #union
s1&s2 #common element
s2.difference(s1) #from s2 remove element of s1  which is also present in s2  we can also write s2-s1
s1.issubset(s2)  #kya s1 subset hai s2 ka

