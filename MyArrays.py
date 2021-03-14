# REPL in command prompt opens Python's interactive mode
# If numpy module not found, run program in terminal
# Click empty space, then Run python file in terminal

import numpy as np
import random

"""

integers = np.array([1, 2, 3])

#print(type(integers))
#print(integers)

# LIST COMPREHENSION
integers = np.array([x for x in range(2, 21, 2)])
#print(integers)

# make sure to include overall [] for entire list
integers = np.array([[1, 2, 3], [4, 5, 6]])
#print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
#print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape
d = integers.size

print()

for row in integers:
    print(row)
    for col in row:
        print(col, end=' ')

#for i in integers.flat:
    #print(i)


#EXERCISE: create a 2 dim array of 5 ints using random
integers = np.array([[1, 2, 3], [4, 5, 6]])

a = np.array([[random.randint(1,10) for x in range(5)], 
                [random.randint(1,10) for x in range(5)]])

#Using np random module (much easier); array of 2 rows, 5 cols
b = np.array(np.random.randint(1,10,size=(2,5)))

print(a)
print()
print(b)

c = np.zeros(5)
d = np.ones(5)
e = np.ones((2,4),dtype=int)
f = np.full((3,5),13)
g = np.arange(5)
h = np.arange(5,10)
i = np.arange(10,1,-2)

print()

print(np.linspace(0.0, 1.0, num=5)) #Evenly spaced float range

print("\n\n")
#Reshape method can change dimension
array1 = np.arange(1,21)

#Both arrays have to have the same number of elements
array2 = array1.reshape(4,5)

print(array1)
print(array2)

"""

array3 = np.arange(1,100001).reshape(4,25000)
print(array3)

array4 = np.arange(1,100001).reshape(100,1000)
print(array4)

print("\n\n")

numbers = np.arange(1,6)
numbers += 10
print(numbers)

#Broadcasting = operations with arrays of different sizes

#Next line is same as: numbers * [2,2,2,2,2]
print(numbers * 2)

print(numbers ** 3)

#numbers is unchanged by the arithmetic operations
print(numbers)

#Multiplying integer arrays with floating pt arrays
#   result is a floating pt
numbers2 = np.linspace(1.1,5.5,5)
print(numbers * numbers2)



#Comparing arrays; both have to have some number of elements
print(numbers>=13)
print(numbers2 < numbers)
print(numbers == numbers2)
