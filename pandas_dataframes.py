import pandas as pd 

#Metod types: loc, iloc, at, iat

grades_dict = {'Wally':[87,96,70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100,81,82], 'Bob': [83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

"""
print(grades['Eva'])

print(greades.Sam)

#using the loc and iloc methods
print(grades.iloc[1])
"""


#For consecutive rows
print(grades.loc['Test1':'Test2'])

print(grades.iloc[0:2])


#For non-consecutive rows, use a comma
print(grades.loc[['Test1','Test3']])

print(grades.iloc[[0,3]])


#View only Eva's and Katie's grades for test1 and test2
print(grades.loc[:'Test2', ['Eva', 'Katie']])

#View only Sam's and Bob's grades for test1 and test2
print(grades.loc[['Test1', 'Test3'], 'Sam':'Bob'])


#Boolean indexing
#Select everyone with an A grade
grades_A = grades[grades >= 90]
print(grades_A)

#Create a datafrom for everyone with a B grade
grades_B = grades[(grades >= 80) & (grades < 90)]
print(grades_B)

#Create a dataframe for everyone with an A or B grade
grades_A_or_B = [(grades >= 90) | (grades >= 80)]
print(grades_A_or_B)

pd.set_option('precision',2)
print(grades.describe())