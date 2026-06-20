#----------------------SORT----------------------
import numpy as np
# arr = np.array([10,40,30,60,90,7,5])   #1d
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)

# arr1 = np.array([[10,40,30],[60,90,7]])   #2d
# print(arr1)
# arr1_s = np.sort(arr1, axis=0)  #
# print(arr1_s)  #default sort --> row wise 


#example of 2d
# by default sorting -> ascending -> descending
# arr = np.array([10,40,30,60,90,7,5])
# print(arr)
# arr_s = np.sort(arr)
# print(arr_s)
# arr_sd = np.sort(arr)[::-1]   #descending
# print(arr_sd)





#----------------------FILTER----------------------
# arr = np.array([10,20,40,6,3,4,2])
# print(arr)
# arr_f = arr[arr < 40]
# print(arr_f)



#----------------------FANCY INDEXING----------------------
# arr = np.array([10,20,3,4,90,100])
# print(arr)
# arr_f = arr[[0,2]]  #0 index value, 2 indx value


#----------------------NP.WHERE----------------------
# arr = np.array([10,3,4,80,30,40,9])
# print(arr)
# arr_w = np.where(arr>40,"True","false")   #conition: true : false
# print(arr_w)

#example
# arr1 = np.array([10,3,4,80,30,40,9])
# print(arr1)
# arr_w = np.where(arr>40,arr+2,arr-2)    #conition: true : false
# print(arr_w)






#----------------------CONCATENATE----------------------
# arr1 = np.array([10,20,30])    #1d
# arr2 = np.array([1,2,3])
# arr1_arr2 = np.concatenate((arr1,arr2))
# print(arr1_arr2)
# print(arr1+arr2)


# arr3 = np.array([[10,20,30],[40,50,60]])   #2d
# arr4 = np.array([[1,2,3],[4,5,6]])
# arr3_arr4 = np.concatenate((arr3,arr4), axis=0)
# print(arr3_arr4)





#STATISTICAL FXNS -->
# 1.np.sum(a) -> Sum of all elements
# 2.np.mean(a) -> Average = Sum of elements / Number of elements
# 3.np.median(a) -> Middle value after sorting
# 4.np.min(a) -> Smallest value in array
# 5.np.max(a) -> Largest value in array
# 6.np.var(a) mean,difference,square,average | (sum = ddof) -> divide by array length
# 7.np.std(a) -> Standard Deviation = √Variance -> Measures spread of data
# 8.np.prod(a) -> Multiplication of all elements
# 9.np.cumsum(a) -> Cumulative (running) sum
# 10.np.cumprod(a) -> Cumulative (running) product
# 11.np.argmin(a) -> Index position of minimum value
# 12.np.argmax(a) -> Index position of maximum value
# 13.np.abs(a) -> Converts negative values to positive -> Absolute value (distance from zero)
# 14.np.unique(a) -> Returns unique values only -> Removes duplicates
# 15.np.percentile(a, 50) -> Finds percentage-based value -> 50th percentile = Median
# 16.np.quantile(a, 0.5) -> Similar to percentile -> 0.5 = 50%
# 17.np.ptp(a) -> Range = Max - Min
# 18.np.any(a) -> True if at least one value is True




# arr = np.array([10,20,30,40,50])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.median(arr))
# print(np.min(arr))
# print(np.max(arr))


arr=np.array([1, 2]) / 0 
print(arr)