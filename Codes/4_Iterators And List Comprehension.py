""" ###################################################################################### """
""" ###################################### ITERATORS ##################################### """
""" ###################################################################################### """

""" Iterable is an object like lists, strings, dictionaries, file connections,"""
""" which one can iterate over. It generates an Iterator when passed to iter() """ 
""" method. Iterator is an object, which is used to iterate over an iterable """ 
""" object using next() method """

string_1 = "My Name Is Debasish Dutta"
iterator_1 = iter(string_1)
for i in range(len(string_1)):
    print(next(iterator_1))

string_2 = "My Name Is Debasish Dutta"
iterator_2 = iter(string_2)
print(*iterator_2)                              """ Iterating at once with """

dictionary_1 = {'Name': 'Debasish', 'Company': 'TCS', 'Qualification': 'B Tech MBA'}
for key, value in dictionary_1.items():
    print(key, value)

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
arr = np.array([np_height, np_weight])

for val in np.nditer(arr):              
    print(val)
for val in arr :
    print(val)

""" For Pandas Dataframes iterrows() function can be used """

""" ###################################################################################### """
""" ###################################### ENUMERATE ##################################### """
""" ###################################################################################### """
  
""" Enumerate() method adds a counter to an iterable and returns it in a form of enumerate """ 
""" object. This enumerate object can then be used directly in for loops or be converted into """
""" a list of tuples using list() method."""

avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
for index, value in enumerate(avengers, start=10):
    print(index, value)

""" ###################################################################################### """
""" ######################################### ZIP ######################################## """
""" ###################################################################################### """

"""The purpose of zip is to map the similar index of multiple containers so that they """
""" can be used just using as single entity """

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ] 
marks = [ 40, 50, 60, 70 ] 
mapped = zip(name, roll_no, marks) 
for z1, z2, z3 in list(mapped):
    print("Name:"+z1+";   Roll No:"+str(z2)+";   Marks:"+str(z3))

""" ###################################################################################### """
""" ################################# LIST COMPREHENSION ################################# """
""" ###################################################################################### """

"""  List Comprehension allows us to create a list using for loop with lesser code """

""" Condition on Iterable """
print([num ** 2 for num in range(10) if num % 2 == 0])  """ [0, 4, 16, 36, 64] """

""" Condition on Output Expression """
print([num**2 if num%2==0 else 0 for num in range(10)]) """ [0, 0, 4, 0, 16, 0, 36, 0, 64, 0] """

""" Dictionary Creation With List Comprehension """
pos_neg = {'Negetive Value of '+str(num):-num for num in range(1,11)}

""" ###################################################################################### """
""" ################################### GENERATORS ####################################### """
""" ###################################################################################### """

""" Generators are similar to list comprehensions, but it  doesn’t construct """
""" list object rather generator generates the next element in demand which """
""" reduces the memory consumption """

from sys import getsizeof 
comp = [i for i in range(10*10000)] 
gen = (i for i in range(10*10000)) 
print("List Comprehension = ", getsizeof(comp)) 
print("Generator = ", getsizeof(gen))