

def duplicate(l):
    for i in l:
        for j in i:
            if l[i]==l[j]:
                l[i]=l[i+1]
                l=l.append(i)
            else:
                l=l.append(i)   
    return 
l=[1,5,5,8,4,7]
duplicate(l)

print(l)            




