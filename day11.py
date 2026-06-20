#---------------flatten---------------   ---> create copy then work
import numpy as np
# #example 2d
# arr  = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.flatten()
#up_arr[0] = 100 
# print(up_arr)
# print(arr)


# #example 3d
# arr1 = np.arange(24).reshape(3,2,4)
# print(arr1)
# up_arr1 = arr1.flatten()
# print(up_arr1)



#---------------ravel---------------    ---> work on original array
#2d
# arr = np.arange(14).reshape(7,2)
# print(arr)
# up_arr = arr.ravel()
# print(up_arr)

#3d
# arr1 = np.arange(24).reshape(3,2,4)
# print(arr1)
# up_arr1 = arr1.ravel()
# print(up_arr1)





#-------------------TRANSPOSE-------------------
# arr = np.arange(12).reshape(3,4)
# print(arr)
# up_arr = arr.T
# print(up_arr)

#3d eg
# arr1 = np.arange(24).reshape(3,2,4)
# print(arr1)
# up_arr1 = arr1.T
# print(up_arr1)





#-------------------SLICING-------------------
# arr = np.arange(11)   #1d
# print(arr)
# up_arr = arr[:3]
# print(up_arr)


# arr1 = np.arange(16).reshape(8,2)   #2d
# print(arr1)
# up_arr1 = arr1[:,-1]
# print(up_arr1)


# arr2 = np.arange(24).reshape(3,4,2)   #3d
# print(list(arr2))
# print(arr2[[0,1],[0,1],[0,5]])





#-------------------WHILE LOOP-------------------
# arr = np.arange(12)      #1d
# i = 0
# while i < len(arr):
#     print(arr[i], end=" ")
#     i += 1


# arr1 = np.arange(12).reshape(3,4)     #2d
# i = 0
# while i < len(arr1):        
#     j = 0
#     while j < len(arr1[i]):  
#         print(arr1[i][j], end=" ")
#         j += 1
#     print()
#     print("\n")
#     i += 1




#-------------------FOR LOOOP-------------------
arr = np.arange(12)
for i in range(len(arr)):
    print(arr[i],end=" ")
print("\n")