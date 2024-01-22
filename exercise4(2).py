#!/usr/bin/env python
# coding: utf-8

# # Exercise 4

# #### Problem 1
# 
# Given variables `p1s1` and `p1s2` of string type, create a string that contains `p1s1` repeated three times and then `p1s2` repeated three times, with a single space separating the two portions.

# In[6]:


import re


problem1 = p1s1*3 + ' ' + p1s2*3


# #### Problem 2
# 
# Create a string with every special character (that is a value of the `str` type) occuring at least once.

# In[2]:


problem2 = ('\'', '\"', '\\', '\t', '\n', '\r')


# #### Problem 3
# 
# Given the string `p3s`, create a `float` using its value.

# In[ ]:


problem3 = float(p3s)


# #### Problem 4
# 
# Query the user to input their favourite integer, perform and type conversion to an `int`, and assign to `problem4`.

# In[5]:


# your code

problem4 = int(input('Whats\'s your favorite integer?'))


# #### Problem 5
# 
# Query the user to input any line of text and assign the number of characters of that line to `problem5`.

# In[ ]:


# your code

problem5 = len(input('Write anything.'))


# #### Problem 6
# 
# Given boolean variables `p6a` and `p6b`, assign the result of the logical expression "p6a is not true and p6b is" to `problem6`.

# In[ ]:


problem6 = (p6a != True) and (p6b == True)


# #### Problem 7
# 
# Given integer variables `p7a`, `p7b`, and `p7c` assign the result of the expression "p7a is greater than p7b and less than p7c" to `problem7`.

# In[6]:


problem7 = p7a > p7b and p7a < p7c


# #### Problem 8
# 
# Create a function that, given three strings, returns a string that is the product of concatenating the input strings in lexographical order.

# In[ ]:


def problem8(s1, s2, s3):
    strToSort = s1 + ' ' + s2 + ' ' + s3
    sortedStr = sorted(strToSort.split())
    return(sortedStr[0] + sortedStr[1] + sortedStr[2])


# #### Problem 9
# 
# Create a function that accepts a temperature value in degrees Celsius as an argument and returns `True` if the value is below the freezing point of water or above its boiling point, `False` otherwise.

# In[ ]:


def problem9(tempC):
    if tempC < 0 :
        return True
    elif tempC > 100 :
        return True
    else : 
        return False 


# #### Problem 10
# 
# Create a function that accepts a single argument and returns `True` if that argument has type `int`, `False` otherwise.

# In[ ]:


def problem10(arg):
    if type(arg) == int :
        return True
    else :
        return False