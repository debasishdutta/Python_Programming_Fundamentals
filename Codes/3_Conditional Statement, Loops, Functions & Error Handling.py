""" ############################################################################## """
""" ########################### CONDITIONAL STATEMENTS ########################### """
""" ############################################################################## """

num = float(input("Enter a number: "))

""" Generic If Else Block """
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

""" Nested If Else Block """
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

""" Single Line Statement """
print("Positive Number") if num>0 else print("Zero") if num==0 else print("Negetive Number")

""" ############################################################################## """
""" #################################### LOOPS ################################### """
""" ############################################################################## """

"""" While Loops """
error = 1000.0
while(error>1):
    error=error/4
    if (error < 10):
        break
    else:
        print(error)

""" For Loops """
for x in range (10,20):
    if (x == 15): 
        break
    if (x % 5 == 0) : 
        continue
    print(x)

""" Looping Over Dictionary """
world = { "afghanistan":30.55,"albania":2.77,"algeria":39.21 }
for key, value in world.items() :
    print(key + ":" + str(value))

""" Looping Over 2D Array """
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in np.nditer(meas):
    print(val)

""" Looping Over Data Frame """
import pandas as pd
import os
home_dir = "C:/Users/debas/Downloads/Python Code Library/Numpy, Pandas, Matplotlib, Bokeh/Datasets"
os.chdir(home_dir)
brics = pd.read_csv("3_Brics.csv", index_col = 0)
for lab, val in brics.iterrows():
    print(lab + ": " + val["capital"])
    
""" Map: It iterates over each element of a Pandas Series and apply a function"""
brics['area'].map(lambda x: x/10)

""" Apply: applied both to series and dataframes where function can be applied """ 
""" both series and individual elements based on the type of function provided """
brics[['area','population']].apply(sum,axis=0)

""" ApplyMap: Apply a function to each element of dataframe """
brics.iloc[,:1].applymap(len)

""" ############################################################################## """
""" ########################### USER DEFINED FUNCTIONS ########################### """
""" ############################################################################## """

""" Variable Scoping """
def f():
    """ Local Variable: Scope: Within A Defined Function """
    x = 42              
    def g():
        """ Non Local Variable: Scope: Not Local Not Global But Only Within Nested Method """
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    g()
    print("After calling g: " + str(x))

""" Glbal Variable: Scope: Entire Script """   
x = 44  
f()
print("x in main: " + str(x))

""" Single Argument Function """
def square(value):
    new_value = value ** 2
    print(new_value)
 
square(4)

""" Multiple Argument Function """
def raise_to_power(value, power):
    new_value = value ** power
    return new_value

raise_to_power(4,3)

""" Multiple Argument Function With Default Value """
def raise_to_power(value, power=2):
    new_value = value ** power
    return new_value

raise_to_power(4)

""" Flexible Frguments Function """
def sum_all_numbers(*args):
    sum_all = 0
    for num in args:
        sum_all +=num
    return(sum_all)

sum_all_numbers(1,2,3,4,5)
sum_all_numbers(1,2,3)

def print_all(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)
print_all(name="Debasish", job="Analyst")
print_all(name="Debasish", job="Analyst", grade="CC2")

""" Function Returning Multiple Values """
def raise_both(value1, value2):
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple

print(raise_both(4,2))

""" Nested Function """
def array_modulus(x1, x2, x3):
    def inner(x):
        return x % 2
    return (inner(x1), inner(x2), inner(x3))
print(array_modulus(10,11,12))

""" Lamda Function & Map """
""" map() Applies The Function To ALL Elements In The Sequence """
nums = [1,2,3,4,5]
pows = [1,2,3,4,5]
square_all = map(lambda x,y: x ** y, nums,pows)

""" ############################################################################## """
""" ################################ ASSERT STATEMENT ############################ """
""" ############################################################################## """

""" Python’s assert statement is a debugging aid that tests a condition. If the condition """
""" is true, it does nothing and your program just continues to execute. But if the assert """
""" condition evaluates to false, it raises an AssertionError exception with an optional """
""" error message """

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert (0 <= price <= product['price']), "Incorrect Discount"
    return price

shoes = {'name': 'Fancy Shoes', 'price': 14900}
apply_discount(shoes, 0.25)
apply_discount(shoes, 2)
apply_discount(shoes, -0.3)

""" ############################################################################## """
""" ######################## ERROR & EXCEPTION HANDLING ########################## """
""" ############################################################################## """

""" ValueError:	Raised when a function gets argument of correct type but improper value """
""" ZeroDivisionError:	Raised when second operand of division or modulo operation is zero """
""" TypeError: Raised when a function or operation is applied to an object of incorrect type """
""" StopIteration: Raised by next() function to indicate an iterator has no further item """
""" OverflowError: Raised when result of an arithmetic operation is too large to be represented """
""" NameError:	Raised when a variable is not found in local or global scope """
""" MemoryError: Raised when an operation runs out of memory """
""" IndexError: Raised when index of a sequence is out of range """
""" KeyError: Raised when a key is not found in a dictionary """
""" RuntimeError: Raised when an error does not fall under any other category """
def square(num, power, div):
    if(num==0 or power<=0):
        raise ValueError("Power Can Not Be Zero Or Negetive And Number Can Not Be Zero")
    if (isinstance(num, str) or isinstance(power, str) or isinstance(div, str)):
        raise TypeError("Only Int & Float Are Allowed")
    try:
        return((num**power)/div)
    except ZeroDivisionError:
        print("Can Not Divide By Zero")