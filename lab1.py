import numpy as np
a=np.array(34)
print("0-D array",a)
arr= np.array([23,15,78])
print("Array",arr)
arr1=np.array([[34,67,78],[23,65,90]])
print("2-D array\n",arr1)
arr2=np.array([[12,45,39,47],[36,43,82,23],[72,93,41,37]])
print("2-D array\n",arr2)
print(np.__version__)
print(type(arr1))
arr3=np.array([[[23,45,67],[346,673,980]],[[67,34,56],[52,12,678]]])
print("3-D array\n",arr3)
print(a.ndim)
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
b=np.array([34,56,78],ndmin=5)
print(a)
print("No of dimensions:",b.ndim)
print("Accessing elements",arr[0])
print("Accessing elements and adding them",arr[0]+arr[2])
print("2-D array accessing",arr1[1,2])
print("3-D array accessing",arr3[1,1,1])
print("2-D negative indexing",arr2[2,-4])
print("3-D negative indexing",arr3[1,1,-2])