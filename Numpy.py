# Numpy
import numpy as np

# Numpy is a python library for numerical computation built for handling large arrays and matrices efficiently
# Numpy arrays are homogeneous, meaning all the elements must be the same type

#=====================================================================================================================
# SECTION 1 : Different ways to create Numpy Arrays

# using list or tuples
list1 = [100,101,102,103,104,105]
nparr = np.array(list1)
print("Simple numpy array : ", nparr)

zeros_array = np.zeros((3,3), dtype=int) # An numpy array filled with 0
ones_array = np.ones((3,3), dtype = int) # a numpy array filled with 1
constant = np.full((4,4),10) # numpy array filled with the specified value
range_array = np.arange(2,20,2) # 1D numpy array of given range and steps
linespace = np.linspace(0,1,5)

print("Zero Array : ", zeros_array)
print("Ones Array : ", ones_array)
print("constant Array : ", constant)
print("Arange array : ",range_array)
print("linspace array : ", linespace)

random_rand = np.random.rand(3,3) # random values sampled from a uniformed distribution over [0,1)
random_randn = np.random.randn(3,3) # random values sampled from a standard normal distribution
random_randint = np.random.randint(1,20,size=(3,3)) # random integers from the given range
print("Rand array : ", random_rand)
print("Randn array : ", random_randn)
print("Randint array : ", random_randint)

#===================================================================================================================================
# SECTION 2 : NUMPY ARRAY INDEXING

# Array Indexing refers to the method of accessing specific elements or subsets of data within an array
arr = np.array([10,20,30,40,50,60,70,80,90])
print(arr[0])
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1,1])
cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],

                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(cube[1, 2, 0])

# Slicing elements
print(arr[1:4])
print(arr[0:8:2])

# Boolean indexing
print(arr[arr>30])

#=========================================================================================================================
# SECTION 3 : RESHAPE AND RESIZE NUMPY ARRAY
# Reshaping refers to modifying the dimensions of an existing array without changing its data
# reshape() function is used for this purpose

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr = arr.reshape(4,3) # 2D array
arrs = arr.reshape(2,2,3) # Transforms it into 2 blocks. Each containing 2X3 Matrix
print(arrs)
r = arr.reshape(4,-1) # we use -1 when dimension is unknown.
# Numpy calculates that missing dimension automatically
print(r)

# resize() function is used to change the size of an existing numpy array.
# Reshape changes only the view/shpae of an array without changing its data size
# resize changes the actual array size either truncating data or repeating elements if needed

arr = np.array([1,2,3,4,5,6])
arr.resize(2,4)
print(arr)

#=================================================================================================================================
# SECTION 4 : STACKING AND SPLITTING ARRAYS
# stack() is used to join multiple arrays.
# Unlike concatenate it joins arrays along a new axis.
# To join 2 arrays they must have same shape and dimensions

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
c = np.stack((a,b), axis=0)
print(c)
d = np.stack((a,b),axis=1)
print(d)

x=np.array([[1,2,3],
            [4,5,6]])

y=np.array([[7,8,9],
            [10,11,12]])
xy = np.stack((x,y), axis=0)
print(xy)
yx= np.stack((x,y), axis=1)
print(yx) # Outputs a 3d array where 1st dimension has 1st rows and 2nd dimension has 2nd rows

# We can split numpy arrays horizontally, vertically, or even diagonally
# split(), hsplit(), vsplit() are functions for dividing arrays along various axes and dimensions
arr = np.array([1,2,3,4,5,6,7,8,9])
arrs = np.array_split(arr,3)
print(arrs)

# np.split() is a function that divides an array into equal parts along a specified axis
# The output shows the original array and the two resulting sub arrays each containing 3 elements
result = np.split(arr,3) # splits into 3 equal parts
print(result)
arr = array = np.array([[3, 2, 1], [8, 9, 7], [4, 6, 5]])
result = np.split(arr,3,axis=1)
print(result)

# vsplit() : vertical splitting / row wise divides an array along the vertical axis axis=0
matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9],
                            [10, 11, 12]])
result = np.vsplit(matrix,2)
print(result)

# hsplit() horizontal splitting / column wise divides an array along the horizontal axis axis = 1
arrays = np.array([[1, 2, 3, 4],
                           [5, 6, 7, 8],
                           [9, 10, 11, 12]])
result = np.hsplit(arrays, 2)
print(result)

# dsplit() is used for splitting arrays along the thrid axis axis=2 applicable to 3D arrays
original_3d_array = np.arange(24).reshape((2, 3, 4))
result = np.dsplit(original_3d_array, 2)
print(result)

#================================================================================================================================
# SECTION 5 : NUMPY ARRAY BROADCASTING
# Broadcasting allows us to perform arithmetic operations on arrays of different shapes without reshaping
# It automatically adjusts the smaller array to match the larger array's shape by replicating its values along the necessary dimensions
arr = np.array([[1,2,3],[4,5,6]])
print(arr+10)

a = np.array([2, 4, 6])
b = np.array([[1, 3, 5], [7, 9, 11]])
res = a + b
print(res)

fd = np.array([ [0.8, 2.9, 3.9],
                [52.4, 23.6, 36.5],
                [55.2, 31.7, 23.9],
                [14.4, 11.0, 4.9] ])

cpg = np.array([9, 4, 4])
res = fd * cpg
print(res)

#================================================================================================================================
# SECTION 6 : ARITHEMTIC OPERATIONS
# np.add() function to add two arrays
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.add(a, b)
print(res)

# np.subtract() function to subtract each element of second array from the corresponding element in the first array
res = np.subtract(a,b)
print(res)

# np.multiply() function multiplies element wise
res = np.multiply(a,b)
print(res)

#np.divide() function divides each element of first array by corresponding element in the second array
res= np.divide(a,b)
print(res)

# np.power() raises each element in an array to a specified power
res = np.power(a,b)
print(res)

# np.mod() calculates modulus element wise
res= np.mod(a,b)
print(res)

# np.sum() returns the sum of array elements over the specified axis
arr = [1,2,3,4,5]
print(np.sum(arr))
print(np.sum(arr,dtype=np.float32))

arr = [[14, 17, 12, 33, 44],
	[15, 6, 27, 8, 19],
	[23, 2, 54, 1, 4,]]
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

# np.mean() returns the mean of the array along the specified axis
arr = [20, 2, 7, 1, 34]
print(np.mean(arr))
arr = [[14, 17, 12],
       [15,  6, 27],
       [23,  2, 54]]
print(np.mean(arr))
print(np.mean(arr, axis=1)) # column wise mean
print(np.mean(arr, axis=0)) # row wise mean

# np.maximum() returns the maximum element wise
in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 15]
print(np.maximum(in_arr1, in_arr2))
in_arr1 = [np.nan, 0, np.nan]
in_arr2 = [np.nan, np.nan, 0]
print(np.maximum(in_arr1, in_arr2))
in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 15]
print(np.minimum(in_arr1, in_arr2))
in_arr1 = [np.nan, 0, np.nan]
in_arr2 = [np.nan, np.nan, 0]
print(np.minimum(in_arr1, in_arr2))

#=========================================================================================================================
# SECTION 7 : MATRIX MULTIPLICATION AND MANIPULATION

# Element wise addition, subtraction and division
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

print("Addition:\n", np.add(x, y))
print("Subtraction:\n", np.subtract(x, y))
print("Division:\n", np.divide(x, y))

# Element wise multiplication and matrix multiplication
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

print(f'ELement wise multiplication : {np.multiply(x,y)}')
print(f'Matrix multiplication / Dot product : {np.dot(a,b)}')

print(f'Square root of all the elements : {np.sqrt(x)}')
print(f'Sum of all elements : {np.sum(y)}')
print(f'Column wise sum : {np.sum(x,axis=1)}')
print(f'Row wise sum : {np.sum(x,axis=0)}')
print(f'Transpose : {x.T}')

# To find the determinant of the matrix
# Determinant of a square matrix is a special number that helps determine whether the matrix is invertible and how it transforms space
sign, logdet = np.linalg.slogdet(x) # To large matrices
# computes the sign and log of the determinant helps prevent numerical overflow or underflow
res = sign * np.exp(logdet)
print(res)

result = np.linalg.det(x)
print(result)

# To find the inverse of a matrix
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
print(np.linalg.inv(A))

#===================================================================================================================================

# SECTION 8 : RANDOM NUMBER GENERATION AND STATISTICS

# Normal distribution
x = np.random.normal()
y = np.random.normal(size=10)
z = np.random.normal(10,scale=2,size=(3,3))
print(f'Single value normal distribution : {x}')
print(f'Array of normal distribution : {y}')
print(f'Mutlidimensional normal distribution : {z}')
