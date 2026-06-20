import numpy as np
# #list 1d
# l = [1,2,3]
# print(l)

# #array 1d
# arr = np.array([1,2,3])
# print(arr)

# #list 2d
# l = [[1,2,3],[4,5,6]]
# print(l)
# print(l[0])  #first row
# print(l[0][0])  #first row and first element

# #array 2d
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0])  #first row
# print(arr[0][0])  #first row and first element


# #replace arr&list value 4 with 100
# l[1][0] = 100
# arr[1,0]= 100
# print(l)
# print(arr)



#------------LIST VS NUMPY ARRAY------------
# #list
# l = [1,2,3]
# lm = l*2
# print(lm)  #it will repeat the list

# #numpy array
# arr = np.array([l])
# arrM = arr*2
# print(arrM)  #it will multiply the array with 2


#comparison-->
# #list
# import time 
# start = time.time()
# l = [i*2 for i in range(1000000)]
# print("list output:", time.time() - start)

# #array
# start = time.time()
# arr = np.array(1000000)*2
# print("array output:", time.time() - start)



# time taken by list and array
# import time
# # List timing
# start = time.time()
# l = [i * 2 for i in range(1000000)]
# end = time.time()
# print("Time taken by list:", end - start)
 
# # NumPy array timing
# start = time.time()
# a = np.array(1000000) * 2 
# end = time.time()
# print("Time taken by array:", end - start)






#ZEROES -->
# arr = np.zeros(5)   #1d array
# print(arr)

# arr2 = np.zeros((3,4))   #2d array
# print(arr2)



#ONES -->
# arr = np.ones(5)   #1d array
# print(arr)

# arr2 = np.ones((3,4))   #2d array
# print(arr2)


# question zeros -> 2d arr -> 10 
# arr = np.zeros((2,3))+10
# print(arr)
# question ones -> 2d arr -> 5
# arr1 = np.ones((2,3))+5
# print(arr1)



# FULL FOR 1D
# arr = np.full((3),5)
# print(arr)

#FULL FOR 2D
# arr1 = np.full((2,3),5)
# print(arr1)




# #question help of zeros -> 2d -> 6
# arr = np.zeros((2,3))+6
# print(arr)

# #question help of full -> 2d
# arr1 = np.full((3,4),1)
# print(arr1)




#random for 1d
# arr = np.random.random(5)
# print(arr)

#random for 2d
# arr1 = np.random.random((2,3))
# print(arr1)




#arange for 1d
# arr = np.arange(5)
# print(arr)

#arange for 2d
# arr1 = np.arange((0,10,2))
# print(arr1)







# VECTOR 1D LIST
# l = [1,2,3]
# print(l)

#VECTOR 1D ARRAY
# arr = np.array(l)
# print(arr)

#MATRIX 2D LIST
# l = [[1,2,3],[4,5,6]]
# print(l)

#MATRIX 2D ARRAY
# arr = np.random.randint(1,10 , size=(2,3))
# print (arr)

#TENSOR 3D LIST
# l = [[[1,2],[3,4],[5,6],[7,8]]]
# print(l)

#TENSOR 3D ARRAY






#ARRAY PROPERTIES:-
                  #1. shape
                  #2. dimension
                  #3. size
                  #4. dtype

arr = np.arange(12).reshape(3,4)  #3*4=12
print("shape: ",np.shape(arr))
print("dimension: ",np.ndim(arr))
print("size: ",np.size(arr))
print("dtype: ",arr.dtype)