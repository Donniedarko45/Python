import numpy as np
a = np.array([[10,2,3],[4,5,6],[7,8,9]])
print("Sorting along the columns:")
print(np.sort(a))
print("Sorting along the rows:")
print(np.sort(a, 0))
data_type = np.dtype([('name', 'S10'),('marks',int)])
arr = np.array([('Mukesh',200),('John',251)],dtype = data_type)
print("Sorting data ordered by name")
print(np.sort(arr,order = 'name'))


