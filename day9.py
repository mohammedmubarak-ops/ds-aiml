# import numpy as np
# a = np.array([1, 2, 3, 4, 5])
# print(a)

# import numpy
# print("hello")

# import numpy
# n = numpy.arange(11)
# print(type(n))
# print(n)
# print(n[0])


#---EXAMPLE---
# import numpy
# n = numpy.arange(12)
# d = n.reshape(3,4)    #3->rows and 4->columns
# print(d)


#---EXAMPLE 3D---
# import numpy
# n = numpy.arange(24).reshape(2,3,4)  #2->number of matrices, 3->rows and 4->columns
# print(n)


#---EXAMPLE SPLIT---
# import numpy
# n = numpy.arange(12).reshape(4,3)
# print(n)
# print(n[0:4:,2])  #first row and second column
# print(n[0:4:,0:3])  #first row and second column


#---EXAMPLE SPLIT 4,7---
import numpy
n = numpy.arange(12).reshape(4,3)
print(n)
print(n[1:3,1])
