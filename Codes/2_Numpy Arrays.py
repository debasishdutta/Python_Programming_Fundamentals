""" ###################################################################################### """
""" #################################### NUMPY ARRAYS #################################### """
""" ###################################################################################### """

""" Numpy arrays are multi dimensional homogenus data container which consumes less memory """
""" and provides faster processing compared to Python Lists """

import numpy as np
np.__version__  

sample_1darray = np.array([1,2,3,4,5], dtype='float32')
sample_2darray = np.array(([1,2,3,4,5],[6,7,8,9,10]), dtype='int')
""" Permitted Data Types: int8, int16, int32, int64, uint8, uint16, uint32, uint64, float16 """ 
""" float32, float64, complex64, complex128 """

print(np.eye(5))                                  """ Creates 5R X 5C Identical Matrix """
print(np.zeros((3,5),dtype='int'))                """ Creates 3R X 5C array filled with zeros """ 
print(np.ones((3,5),dtype='int'))                 """ Creates 3R X 5C array filled with ones """
print(np.full((3,5),3.14,dtype='float'))          """ Creates 3R X 5C array filled with 3.14 """
print(np.linspace(0,100,10))                      """ 1-D array from evenly spaced values in a range """
print(np.arange(0,100,10))                        """ 1-D array from a defined spaced values in a range """
print(np.arange(0,100,10).reshape(2,5))           """ 2-D array from a defined spaced values in a range """
print(np.arange(0,300,10).reshape(2,5,3))         """ 3-D array from a defined spaced values in a range """
""" Size of initial array should match with size of reshaped array """

""" Inspecting Array Structure """
sample_3darray= np.arange(0,600,10).reshape(3, 4, 5)
type(sample_3darray)                               """ Type of data container """
print(sample_3darray.ndim)                         """ Dimension: 3 """
print(sample_3darray.shape)                        """ Shape: 3 X 4 X 5 """
print(sample_3darray.size)                         """ Size: 60 Elements """
print(sample_3darray.dtype)                        """ Data Type of Each Element: int32 """
print(sample_3darray.itemsize)                     """ Size of Each Elements In Bytes """
print(sample_3darray.nbytes)                       """ Size of of Whole Array In Bytes """
del sample_3darray                                 """ Delete array """

""" Accessing Numpy Arrays """
""" Numpy 1-D Arrays are acccessed in the same manner as Python Lists are accessed  """
x = np.arange(0,75,5).reshape(3,5)
print(x[:,0])                                      """ First column """
print(x[0,:])                                      """ First row """
print(x[3-1,3-1])                                  """ Third row third column """
print(x[:2,:3])                                    """ First two rows and first three columns """
print(x[:,1:3])                                    """ All rows and second & third columns """
print(x[:,::2])                                    """ All rows and every second columns """
print(x[::-1,::-1])                                """ Reversing the array """

""" Numpy Array assignment is also pointer based assignment like Python List """
x2_sub_array_copy = x[:2,:3].copy()
x2_sub_array_copy[0,0]=55                            
print(x2_sub_array_copy)                             
print(x)

""" Some Commonly Used Array Functions & Operations """
x= np.random.randint(0,10,(3,5))

""" Sorting """
print(np.sort(x, axis=None))              """ Sort Along The Flattened Array """
print(np.sort(x,axis=0))                  """ Sort Along Columns """
print(np.sort(x,axis=1))                  """ Sort Along Rows """
print(np.sort(x))                         """ Sort Along The Last Axis, In This Case Row """

print(np.argsort(x, axis=None))           """ Indices of Sorted Flattened Array """
print(np.argsort(x,axis=0))               """ Indices of Sorted Array Along Columns """
print(np.argsort(x,axis=1))               """ Indices of Sorted ArraySort Along Rows """
print(np.argsort(x))                      """ Indices of Sorted Array Along The Last Axis """

""" Aggregating """
print(np.sum(x, axis=None))               """ Sum of The Flattend Array, Other Variant np.nansum """                                        
print(np.sum(x, axis=0))                  """ Column Sum """
print(np.sum(x, axis=1))                  """ Row Sum """

print(np.cumsum(x, axis=None))            """ Cum Sum of Flattend Array Other Variant np.nancumsum """
print(np.cumsum(x, axis=0))               """ Cum Sum of Columns """
print(np.cumsum(x, axis=1))               """ Cum Sum of Rows """

print(np.prod(x, axis=None))              """ Product of The Entire Array, Other Variant np.nanprod """
print(np.prod(x, axis=0))                 """ Column Product """
print(np.prod(x, axis=1))                 """ Row Product """

print(np.cumprod(x, axis=None))           """ Cum Prod of Flattend Array, Other Variant np.nancumprod """
print(np.cumprod(x, axis=0))              """ Cum Prod of Columns """
print(np.cumprod(x, axis=1))              """ Cum Prod of Rows """

print(np.min(x, axis=None))               """ Min of The Flattend Array, Other Variant np.nanmin """
print(np.min(x, axis=0))                  """ Column Min, Ignores NaN """
print(np.min(x, axis=1))                  """ Row Min, Ignores NaN """

print(np.argmin(x, axis=None))            """ Find Index of Minimum Value of Flattened Array """
print(np.argmin(x, axis=0))               """ Find Index of Column Minimum Value """
print(np.argmin(x, axis=1))               """ Find Index of Row Minimum Value """

print(np.max(x, axis=None))               """ Max of The Flattened Array, Other Variant np.nanmax """
print(np.max(x, axis=0))                  """ Column Max, Ignores NaN """
print(np.max(x, axis=1))                  """ Column Min, Ignores NaN """

print(np.argmax(x, axis=None))            """ Find Index of Maximum Value of Flattened Array """
print(np.argmax(x, axis=0))               """ Find Index of Column Maximum Value """
print(np.argmax(x, axis=1))               """ Find Index of Row Maximum Value """

print(np.mean(x, axis=None))              """ Mean of The Flattened Array, Other Variant np.nanmean """
print(np.mean(x, axis=0))                 """ Column Mean """
print(np.mean(x, axis=1))                 """ Row Mean """

print(np.median(x, axis=None))            """ Median of The Flattened Array, Other Variant np.nanmedian """
print(np.median(x, axis=0))               """ Column Median """
print(np.median(x, axis=1))               """ Row Median """

print(np.std(x, axis=None))               """ Std Dev of The Flattened Array, Other Variant np.nanstd """
print(np.std(x, axis=0))                  """ Column Standard Deviation """
print(np.std(x, axis=1))                  """ Row Standard Deviation """

print(np.var(x, axis=None))               """ Variance of The Entire Array, Other Variant np.nanvar """ 
print(np.var(x, axis=0))                  """ Column Variance """
print(np.var(x, axis=1))                  """ Row Variance """

print(np.percentile(x,75, axis= None))    """ Percentile of The Entire Array, Other Variant np.nanpercentile """
print(np.percentile(x, 75, axis=0))       """ Column Percentile """
print(np.percentile(x, 75, axis=1))       """ Row Percentile """

print(np.all(x==5, axis=None))            """ Evaluate Whether All Elements Are True """
print(np.all(x==5, axis=0))               """ Evaluate Whether All Elements of Columns Are True """
print(np.all(x==5, axis=1))               """ Evaluate Whether All Elements of Rows Are True """

print(np.any(x==5, axis=None))            """ Evaluate Whether Any Elements Are True """
print(np.any(x==5, axis=0))               """ Evaluate Whether Any Elements of Columns Are True """
print(np.any(x==5, axis=1))               """ Evaluate Whether Any Elements of Rows Are True """

print(np.count_nonzero(x<5,axis=None))    """ Non Zero Count of Flattened Array """
print(np.count_nonzero(x<5,axis=0))       """ Column-wise Non Zero Count """
print(np.count_nonzero(x<5,axis=1))       """ Row-wise Non Zero Count """

print(np.sum((x > 0) & (x < 5), axis=None))  """ Count (Boolean Operators: &, |, ~) of Flattened Array """
print(np.sum((x > 0) & (x < 5), axis=0))     """ Column-wise Count (Boolean Operators: &, |, ~) """
print(np.sum((x > 0) & (x < 5), axis=1))     """ Row-wise Count (Boolean Operators: &, |, ~) """
""" All of these functions can be accessed by dot operators also like x.mean(0) means column """
""" mean and x.mean(1) means row mean """

""" Mathmatical Functions, Does Not Have Axis Argument """
print(np.abs(x))
print(np.exp(x))
print(np.exp2([x]))
print(np.power(3,x))
print(np.log(x))
print(np.log2(x))
print(np.log10(x)) 

""" Array Concatenation """
x= np.array([1,2,3,4,5,6]).reshape(2,3)
y= np.array([7,8,9,10,11,12]).reshape(2,3)

print(np.concatenate([x,y],axis=0))       """ Vertical Stack """
print(np.vstack([x,y]))                   """ Vertical Stack """ 
print(np.row_stack([x,y]))                """ Vertical Stack """

print(np.concatenate([x,y],axis=1))       """ Horizontal Stack """
print(np.hstack([x,y]))                   """ Horizontal Stack """
print(np.column_stack([x,y]))             """ Horizontal Stack """

print(np.concatenate([x,y],axis=None))    """ Flattened An Array """

""" Array Splitting """
grid = np.arange(16).reshape(4,4)

upper, lower = np.vsplit(grid, [2])       """ Vertical Splitting """
print(upper)
print(lower)

left,right = np.hsplit(grid,[2])          """ Horizontal Splitting """
print(left)
print(right)

""" Numpy Arrays For Random Number Generation """
np.random.seed(12345)                     """ Seed For Reproducibility """
print(np.random.random((3,5)))            """ Filling A 3R X 5C Array With Uniform Random Dist [0,1) """
print(np.random.randint(0,10,(3,5)))      """ Filling A 3R X 5C Array With Random Integers [0,10) """
print(np.random.normal(0,1,(3,5)))        """ Filling A 3R X 5C Array With Normal Dist Mean=0,Std=1 """