def simpl_intrest(p,r,t):
    si=p*r*t/100
    return si
t=int(input("enter time years: "))
p=int(input("enter principle amount: "))
r=int(input("enter rate: "))
print("simple intrest is:",simpl_intrest(p,r,t))


