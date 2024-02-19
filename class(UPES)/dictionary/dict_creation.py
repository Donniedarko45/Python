n=5
d={4: '10', 5: '11', 6: '12', 7: '13', 8: '14'}
for i in range(n):
    k=int(input("enter key: "))
    v=input("enter value: ")
    d.update({k:v}) # or d[k]=v
print(d)
for i in d:
    # for accessing keys
    print(i) #for accessing value i ki jagah d[i]...
    
