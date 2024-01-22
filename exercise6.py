#!/usr/bin/env python
# coding: utf-8

# # Exercise 6

# #### Problem 1
# 
# (True/False) The class object `str` has a method `capitalize()` which may be called explicitly as follows,
# 
# ```python
# string = "my string"
# 
# str.capitalize(string)
# ```

# In[ ]:


problem1 = True # True or False


# #### Problem 2
# 
# Given a string `p2s`, assign to `problem2` a new string resulting from first capitalizing the first letter and then swapping the case of all the characters in `p2s` using a single statement through chaining method calls.

# In[ ]:


problem2 = str.swapcase(p2s[0].upper() + p2s[1:])



# #### Problem 3
# 
# Given the string `p3s`, assign to `problem3` the sub-string resulting from concatenating every other (that is, each alternate: first, third, ...) character in `p3s` (starting with the first).

# In[ ]:


problem3 = p3s[::2]

# #### Problem 4
# 
# Given the list `p4l`, assign to `problem4` the last item of the list.

# In[ ]:


problem4 = p4l[-1]


# #### Problem 5
# 
# Given the list `p5l` of numeric objects, assign `problem5` a new list with items (in order): the minimum value, the maximum value, and the average value in `p5l`.

# In[ ]:


problem5 = [min(p5l), max(p5l), sum(p5l)/len(p5l)]


# #### Problem 6
# 
# Develop a function `problem6(list1, list2)` that concatenates two copies of `list1` with three copies of `list2`.

# In[ ]:


def problem6(list1, list2):  
    list3 = 2*list1 + 3*list2
    return list3
    


# #### Problem 7
# 
# Develop a function `problem7(lists)` that finds the first and last string (lexicographic order) in a list of strings `lists` and returns a new list with these items (in order).

# In[ ]:


def problem7(lists): 
    lists.sort()
    newList = [lists[0], lists[-1]]
    return newList


# #### Problem 8
# 
# Given lists `p8l1` and `p8l2` along with an object `p8i`, assign to `problem8` the value `True` if `p8i` is an item in both lists, otherwise `False`.

# In[ ]:


problem8 = (p8i in p8l1) and (p8i in p8l2)
