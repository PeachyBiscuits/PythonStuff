#!/usr/bin/env python
# coding: utf-8

# # Exercise 8

# In[3]:


# Execute this code block to import the NumPy library
import numpy


# #### Problem 1
# 
# Create an `ndarray` object with data-type `float`, shape (2,3,4), and all values initialized to `5`.

# In[91]:


problem1 = numpy.full((2,3,4), 5).astype(float)


# #### Problem 2
# 
# Develop a function `problem2(array1, array2)` with returns `True` if binary arithmetic operations (+, -, \*, etc) may be applied to the arrays `array1` and `array2`, `False` otherwise.

# In[141]:


def problem2(array1, array2):
    try:
        numpy.broadcast(array1, array2)
        return True
    except ValueError:
        return False


# #### Problem 3
# 
# Develop a function `problem3(array1, array2)` that returns the shape of the result of applying binary arithmetic operations (+, -, \*, etc) to the arrays `array1` and `array2` or `None` if doing so would result in a semantic error.

# In[87]:


def problem3(array1, array2):
    if array1.shape[-1] == array2.shape[-1]:
        array3 = array1 + array2
        return array3.shape
    else:
        return None


# #### Problem 4
# 
# Given an array `p4arr`, create a new array whose values correspond to applying the natural logarithm to each of the values in `p4arr`.

# In[42]:


problem4 = numpy.log(p4arr)


# #### Problem 5
# 
# Create an `ndarray` with values ranging from 5 to 50 in increments of 5.

# In[44]:


problem5 = numpy.arange(5,51,5)


# #### Problem 6
# 
# Create an `ndarray` with values ranging from 5 to 50 in increments of 5 in a way different from the previous problem.

# In[ ]:


problem6 = numpy.array([5,10,15,20,25,30,35,40,45,50])


# #### Problem 7
# 
# Develop a function `problem7(array1)` which returns a tuple `(min, max, mean)` of the minimum, maximum, and mean values in the array.

# In[128]:


def problem7(array1):
    TupleVal = (array1.min(), array1.max(), numpy.mean(array1))
    return TupleVal


# #### Problem 8
# 
# Given an array of integers `p8arr`, determine the number of values in the array greater than 5 **without** using loops.

# In[46]:


problem8 = numpy.sum(p8arr > 5)


# In[ ]:




