n=int(input("enter no. of movies: "))
d={}
for i in range(n):
    year=int(input("enter year: "))
    name=input("enter movie name: ")
    production_cost=int(input("enter cost of production: "))
    collection=float(input("enter total collecn of movie: "))
    director_name=input("enter director name: ")
    v=(year,production_cost,collection,director_name)
    d.update({name:v})

#printing movie name
    
for i in d:
    print("movie name: ",name)
#display name of movies released before 2015    
for i in d:
    if d[i][0]<2015:
        print("movies released before 2015: ",i)
    if (d[i][2]-d[i][1])>0: # printing movies that made a profit. 
        print("movies tht made profit: ",i)
t=input("which director you are looking for: ")        
for i in d:
    if(d[i][3]==t):
      print("director name:",director_name,"name of his movies:",i)
#yearwise movies printing:
"""sorted(d[i][0])      
for i in d:"""
    
