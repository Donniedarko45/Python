"""
• Series
• 1-D array of data and associated array of data labels (index).
• Dataframes
• 2-D data structure with labels which can store heterogeneous data
"""
# creating series objects

import pandas
hello=pandas.Series([1,2,3])
marsh=pandas.Series([10,20,30],index=[2,5,8])
print(marsh)
print(hello)
a=pandas.Series({"jan":31,"Feb":28,"March":30})
print(a)
ser=pandas.Series({1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"})
print(ser[2:4])
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

var=pandas.DataFrame(mydataset)
print(var)

