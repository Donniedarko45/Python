import re
text = "The temperature is 25 degrees Celsius."
matches=re.findall("\d",text)
#print(matches)

text = "This is a sample sentence. "
matches=re.findall("\s",text)
a=len(matches)
print(a)


text = "The temperature is 25 degrees Celsius."
matches=re.findall("\D",text)
print(matches)

text = "The temperature is 25 degrees Celsius."
matches=re.findall("/S",text)
print(matches)



