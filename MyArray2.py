import numpy as np

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