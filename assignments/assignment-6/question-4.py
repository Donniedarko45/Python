'''Create a dictionary of n persons where key is name and value is city.
a) Display all names
b) Display all city names
c) Display student name and city of all students. 
d) Count number of students in each city'''


d={}
n=int(input("enter total number of students: "))
# key->name  . value->city
for i in range(n):
    name=input('enter name of a person: ')
    city_names=input('enter name of a city: ')
    d.update({name:city_names})
for i in d.keys():
    print("name of all persons: ",i)
for i in d.values():
    print("city names: ",i)
for i in d.items():
    print("students name along with there city name: ",i)    
count=[0,0] 
""" for number of students in each city let count =0 for both city and students"""
