""" ###################################################################################### """
""" #################################### PYTHON LISTS #################################### """
""" ###################################################################################### """

""" List is mutuable, heterogenous, zero based indexed one dimensional data container """
sample_list = ['Debasish Dutta', 'Kolkata', 32, 'B-Tech MBA', 11.9]

""" Accessing Values In Lists """
print(sample_list[0])                               """ First element of the list """
print(sample_list[1])                               """ Second element of the list """
print(sample_list[-1])                              """ Last element of the list """
print(sample_list[-4])                              """ Fourth last element of the list """
print(sample_list[1:4])                             """ Start index is inclusive, end index is exclusive """
print(sample_list[3:])                              """ Fourth element from begining onwards """
print(sample_list[:3])                              """ First three elements of the list """
print(sample_list[-3:])                             """ Last three elements """
print(sample_list[:-3])                             """ All elements excluding last three elements """
print(sample_list[::2])                             """ Every second elements in the list """
print(sample_list[::-2])                            """ Every other element starting from end to index 0 """
print(sample_list[2::2])                            """ Every other element starting from index 2 to end """
print(sample_list[2::-2])                           """ Every other element starting from index 2 to start """


""" Storing Multi Dimensional Data In A List """
list1 = [['Debasish Dutta', 'Kolkata', 32, 'B-Tech MBA', 11.9],
         ['Debraj Patra', 'Bangalore',30, 'M Sc', 13]]
list1[1][2]

""" Basic List Operations """
type(sample_list)                                   """ Type of the data container """
str(sample_list)                                    """ Prints the list, returns string """
len(sample_list)                                    """ No of elements in list """
sample_list.reverse()                               """ Reverses a list but returns nothing """
sample_list.sort()                                  """ Sorts a homogenous list but returns nothing """
sample_list.append('Data Scientist')                """ Only one element can be appended """
sample_list.append(['Python', 'Machine Learning'])  """ Appending a list within a list """
sample_list.pop(-1)                                 """ Remove single item based on index """
sample_list.extend(['Python', 'Machine Learning'])  """ Appending multiple items in a list """
sample_list.insert(4,"Accenture")                   """ Inserting an element at a specific position """
sample_list.remove('Kolkata')                       """ Remove the first occurance of a given value """
sample_list.count("Python")                         """ Returns count of the element """
sample_list.index("Debasish Dutta")                 """ Returns the first occurance position """
print(10.6 in sample_list)                          """ List searching, True/False will be returned """
print('New Delhi' not in sample_list)               """ List searching, True/False will be returned """

""" Python List assignment is pointer based assignment """
x = ["a", "b", "c"]
y = x                                               """ y points to x """
y[1] = "z"
print(x)                                            """ ["a", "z", "c"] """
print(y)                                            """ ["a", "z", "c"] """

x = ["a", "b", "c"]
y = x[:]                                            """ Copy of x is created """
y[1] = "z"
print(x)                                            """ ["a", "b", "c"] """
print(y)                                            """ ["a", "z", "c"] """

""" ###################################################################################### """
""" #################################### PYTHON TUPLE #################################### """
""" ###################################################################################### """

""" Tuple is immutuable, heterogenous, zero based indexed one dimensional data container"""
sample_tuple = ('Debasish Dutta', 'New Delhi', 31, 10.6, 'Accenture')
sample_tuple = 'Debasish Dutta', 'New Delhi', 31, 10.6, 'Accenture'

""" Storing Multi Dimensional Data In A Tuple """
tuple1 = (('Debasish Dutta', 'Kolkata', 32, 'B-Tech MBA', 11.9),
         ('Debraj Patra', 'Bangalore',30, 'M Sc', 13))
tuple1[1][2]

""" Python Tuples are acccessed in the same manner as Python Lists are accessed  """

""" As Tuple is immutable; Count and  Index is the only method available for Tuple """
str(sample_tuple)                                  """ Prints the tuple, returns string """
len(sample_tuple)                                  """ No of elements in tuple """
type(sample_tuple)                                 """ Type of the data container """
sample_tuple.count("Kolkata")                      """ Returns count of the element """
sample_tuple.index(32)                             """ Returns the first occurance position """

""" ###################################################################################### """
""" ################################## PYTHON DICTIONARY ################################# """
""" ###################################################################################### """

""" Dictinary is unordered key-value pair or associative array where key is immutable """
""" but value is mutabale. Keys must be unique. If duplicate keys are found then the """
""" last key-value element is taken automatically """
sample_dict = {'Age': 7, 'Class': 'First', 'Name': 'Zara'}
sample_dict = {'Age': [7,8], 'Class': ['First','Second'], 'Name': ['Zara','Sara']}

""" Accessing Dictionary """
list(sample_dict.keys())                           """ Returns list of dictionary keys """
list(sample_dict.values())                         """ Returns list of dictionary values """
list(sample_dict.items())                          """ Returns dictionary's key-value tuple pairs """
list(sample_dict.items())[0][1]                    """ Returns dictionary's value for a key """

""" Storing Multi Dimensional Data In A Dictionary """
dict1 = {'Age': [7,8], 'Class': ['First','Second'], 'Name': ['Zara','Sara']}
list(dict1.items())[0][1][0]

""" Basic Dictionary Operations """
str(sample_dict)                                   """ Prints the dictionary, returns string """
len(sample_dict)                                   """ No of elements in dictionary """
type(sample_dict)                                  """ Type of the data container """
sample_dict['Age'] = 12                            """ Updating an existing key value """
sample_dict['Gender'] = "Female"                   """ Adding new key in existing dictionary """
sample_dict.setdefault('School', None)             """ Default value is set to a missing key """
{}.fromkeys(sample_dict.keys(), None)              """ Initialialize a dict from an existing dict """
'Name' in sample_dict                              """ Searching the keys """
'Salary' not in sample_dict                        """ Searching the keys """
sample_dict.pop('Gender',None)                     """ Remove key and value is returned """
del sample_dict['Name']                            """ Remove key but returns nothing """
sample_dict.clear()                                """ Makes a dictionary empty with no key-value pair """
del sample_dict                                    """ Delete entire dictionary """