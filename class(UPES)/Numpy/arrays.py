import numpy
list1=[1,2,3,4]
array1=numpy.array(list1)
print("Array:",array1)

# 2D arrays

list2=[[10,20],[30,40]]
array2=numpy.array(list2)
print("2D array: \n",array2)

"""
• Array size can not be changed
• Array can contain elements of homogeneous type only
• Array support vectorized operations
"""

#vectorised operation=>Vectorized operations in NumPy refer to the capability of NumPy arrays to perform arithmetic and mathematical operations on entire arrays, rather than on individual elements. This means that when you perform an operation (like addition, multiplication, etc.) between two NumPy arrays, the operation is applied element-wise.

# ways to create numpy arrays:-
"""
 Using empty()
• Numpy.empty(shape,[dtype=<datatype>,])
example:->a2=np.empty([3,2],dtype=int)
"""