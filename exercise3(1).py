#!/usr/bin/env python
# coding: utf-8

# # Exercise 3

# **IMPORTANT**: Do not confuse the letter `l` and the number `1`, which look similar in a monospace font: `l` is a lowercase L, `1` is the numeral 1. Mixing them up will cause you a lot of grief!
# 
# In this exercise, we introduce problems where you must write functions (Problems 3, 4, 6). In order for function declarations to be syntactically correct, they must contain at least a single indented line of code. The statement `pass` is often used to denote an incomplete function. `pass` does nothing, so please replace it when writing your solution.

# #### Problem 1
# 
# Round `p1a` (float) to the decimal place `p1b` (integer) and assign the resulting value to `problem1`.

# In[ ]:


problem1 = round(p1a, p1b);


# #### Problem 2
# 
# Using built-in functions to assign a complex value with the real component equal to `p2r` and the imaginary component equal to `p2i`.

# In[ ]:


problem2 =complex(p2r, p2i);


# #### Problem 3
# 
# Complete the partial function declaration below.

# In[ ]:


def problem3(m1, n1, m2, n2):
    int = m1, n1, m2, n2;
    product = min(int)*max(int);
    return product;


# #### Problem 4
# 
# Which one of the following scenarios would *not* be an appropriate use of the `None` value:
# 
# a) As the return value for a function that displays text to the screen.
# 
# b) As the input value for the real argument for `complex()` to represent a number with a zero real component.
# 
# c) The result of executing a function with invalid input arguments.

# In[ ]:


problem4 = 'ab';


# #### Problem 5
# 
# Following the function design recipe, define a function that finds the determinant of a square 2x2 matrix given entries `a`, `b`, `c`, `d` in order row-wise.

# In[ ]:


def problem5(a, b, c, d):
    determinant = (a*d)-(b*c);
    return determinant;


# #### Problem 6
# 
# Following the function design recipe, define a function that returns the number of breaks to be taken on a trip of length `h` hours if a break is taken every `t` minutes.

# In[ ]:


def problem6(h, t):
    breaks = h/t
    return breaks
    
    

