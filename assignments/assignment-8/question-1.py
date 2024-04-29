"""1. Add few names, one name in each row, in “name.txt file”.
a. Count no of names
b. Count all names starting with vowel
c. Find longest name """

def create_file(filename):
   f=open(filename,"w")
   f.close()

#creating function to entering a name in each row:---

def add_name(filename):
   f=open(filename,"a")
   name1="ram"
   name2="shyam"
   name3="harsh"
   name4="pulkit"
   name5="akshit"
   name6="elephant"
   f.write(name1+"\n"+name2+"\n"+name3+"\n"+name4+"\n"+name5+"\n"+name6)
   f.close()    
   return filename

#creating function that counts number of names..

def no_of_names(filename):
   f=open(filename)
   names=f.readlines()
   return print("number of names in file is: ",len(names))
   
#creating function to find a name with longest character...
def longest_name(filename):
   pass

#creating function to Count all names starting with vowel...
   
def count_name_with_vowels(filename):
   f=open(filename)
   names=f.readlines()
   count=0
   for name in names:
      if name[0] in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
         count+=1
   return print("all names starting with vowel",count)     

create_file("names.txt")
add_name("names.txt") 
f=open("names.txt")
print(f.read())
no_of_names("names.txt") 
count_name_with_vowels("names.txt")  


