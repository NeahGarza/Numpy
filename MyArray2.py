import numpy as np
import random

grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81,82]])

#Each row represents a student
#Each col represents a test grade
a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
print(g)

h = grades.mean(axis=1)
print(h)

numbers = np.array([1,4,9,16,25,36])

sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1,7) * 10

add = np.add(numbers, numbers2)

print(add)

multiply = np.multiply(numbers2, 5)

print(multiply)

#Let's reshape numbers2 into a 2 by 3 array, then multiply its value by a 
# one-dimensional array of three elements:
numbers3 = numbers2.reshape(2,3)
numbers4 = np.array([2,4,6])
multiply2 = np.multiply(numbers3, numbers4)
print(multiply2)

"""This works because numbers4 has the same length as each row of numbers3,
so NumPy can apply the multiply operation by treating numbers4 as if it were the
following array:

array([[2,4,6],
[2,4,6]])"""

#Indexing and slicing
grades = np.array([[87,96,70], [100,87,90], [94,77,90], [100,81,82]])

a = grades[0,1]
print(a)
#96

b = grades[1]
#array([100,87,90])

#To select multiple sequential rows use slice
#notation (remember upper limit is not included)
firsttwo = grades[0:2]
#array ([87, 96, 70], 
#       [100,87,90])

#all rows and only first column
c = grades[:2,0]
print(c)

#You can select consecutive columsn using a slice:
d = grades[:,1:3]
"""array([[96,70]
[87,90]
[77,90]
[81,82]]) """

#Or specific columns using a list of column indices:
e = grades[:,[0,2]]
"""array([[87,70]
[100,90]
[94,90]
[100,82]]) """


"""Use NumPy random number generation to create an array of twelve random grades
in the range of 60 through 100, then reshape result into a 3 by 4 array.
Calculate the average of all the grades, the averages of the grades for each test,
and the averages of the grades for each student."""

grades = np.random.randint(60,101,12).reshape(3,4)

print(grades.mean())
print(grades.mean(axis=0))
print(grades.mean(axis=1))

#Shallow copies (view)
#The array method view returns a new array object with a view of the original array

numbers = np.arange(1,6)
#array([1, 2, 3, 4, 5])

numbers2 = numbers.view()
#array([1, 2, 3, 4, 5])

numbers[1] *= 10

print(numbers2)
#array([1, 20, 3, 4, 5])

#Similarly, changing a value in the view also changes that value in the original array:
numbers2[1] /= 10

print(numbers)

#Slice values
#Slices also create views. Let's make numbers2 a slice that views only the first
#   three elements of numbers:
numbers2 = numbers[0:3]

#To verify it is a view, let's modify an element in the original array and see
#   the view array
numbers[1] *= 20

print(numbers2)
# array([1, 40, 3])

#Deep copies (copy)
#The array method copy returns a new array object with a deep 
#   copy of the original array
numbers = np.arange(1,6)
numbers2 = numbers.copy()

#To prove that numbers2 has a separate copy of the data in numbers, let's modify an
#   element in numbers, then display both arrays:

numbers[1] *= 10

print(numbers)
# array([1, 20, 3, 4, 5])

print(numbers2)
# array([1, 2, 3, 4, 5])

"""The array methods reshape and resize both enable you to change the array's dimensions
Method reshape returns a view (shallow copy) of the original array with the
new dimensions. It doesn't modify the original array: """

grades = np.array([[87, 96, 70], [100, 87, 90]])

a = grades.reshape(1,6)
print(a)
print(grades)
# array([[87, 96, 70, 100, 87, 90]])

b = grades.resize(1,6)
print(grades)

#Method flatten deep copies the original array's data:
flattened = grades.flatten()

#Alternatively, Method ravel produces a view (Shallow Copy) of the original array,
#   which shares the grades array's data:
raveled = grades.ravel()

#confirm that they share the same data
raveled[0] = 100
raveled[5] = 99

#Since it is a view and they share the same data, we can look at grades to see
#   that the 6th element has been updated
print(grades)

#You can quickly transpose an array's rows and columns - that is "flip" 
# the array, so the rows become the columns and the columns become rows
# The T attributes returns a transposed view (shallow copy) of the array

transposed = grades.T
print(transposed)

#You can combine arrays by adding more columns or more rows - known as
#   horizontal stacking and vertical stacking

#H STACK
#Let's assume grades2 represents three additional exam grades for the
#   two students in the grades array
grades = np.array([[87, 96, 70], [100, 87, 90]])
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

#We can combine grades and grades2 with NumPy's hstack
h_grades = np.hstack((grades, grades2))

#new array
print(h_grades)

#old array is not affected
print(grades)

#V STACK

#Let's assume that grades2 represents two more students' grades on three exams
v_grades = np.vstack((grades, grades2))
print(v_grades)

