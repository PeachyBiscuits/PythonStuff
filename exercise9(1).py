#!/usr/bin/env python
# coding: utf-8

# # Exercise 9

# In[2]:


# Execute this code block to import the NumPy library
import numpy


# #### Problem 1
# 
# Using `NumPy`'s linear algebra module, develop a function `problem1(A,b)` that returns `True` if the linear equation system $\mathbf{Ax} = \mathbf{b}$ has a unique solution and `False` otherwise.

# In[276]:


def problem1(A,b):
    if A.shape[0] == b.shape[0]:
        C = numpy.append(A,b,axis = 1)
        if numpy.linalg.matrix_rank(A) == b.shape[0] and numpy.linalg.matrix_rank(A) == numpy.linalg.matrix_rank(C):
            return True
    return False


# #### Problem 2
# 
# Using `NumPy`'s linear algebra module and your solution to Problem 1, develop a function `problem2(A,b,method)` that returns the elapsed time (seconds) required to solve the linear equation system $\mathbf{Ax} = \mathbf{b}$ using (i) Gaussian Elimination if `method = "ge"` (`linalg.solve()`) or (ii) the inverse ($\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$) method if `method = "inv"`. If the linear equation system does not have a unique solution or is not solvable, return `None`.

# In[204]:


import time

def problem2(A,b,method):
    check = problem1(A,b)
    if check == True:
        if method == "ge":
            ts = time.time()
            x = numpy.linalg.solve(A,b)
            return (time.time() - ts)
        elif method == "inv":
            ts = time.time()
            x = numpy.linalg.inv(A)*b
            return (time.time() - ts)
    return None


# #### Problem 3
# 
# Use the `NumPy` functions `polyfit()`, `random.random()`, and your solution to Problem 2 to develop a function `problem3(n_array, method)` that returns a `array` of the coefficients of the best-fit polynomial $t(n)$ for the runtime of Gaussian elimination or the inverse matrix method depending on the value of `method` (`"ge"` or `"inv"`). The runtime should be fit to a third order polynomial:
# 
# $t(n) = a_0 + a_1 n + a_2 n^2 + a_3 n^3$
# 
# where $t(n)$ is the runtime of the method for solving a linear system of size $n$. The input argument `n_array` specifies the dimensions of the linear systems that should be used as a sample set to measure runtimes which are then used to determine a best-fit. The best fit $t(n)$ provides us with an approximation of the runtime versus linear system size for the specified method (`"ge"` or `"inv"`).
# 
# The `random.random()` function should be used to generate the linear equation systems of different dimensions (specified by `n_array`) which, in turn, will be used to create timing data points $(n, t)$ for fitting to the polynomial.

# In[275]:


def problem3(n_array, method):
    x_values = []
    y_values = []
    for i in range(50): 
        x = numpy.random.randint(n_array[0], n_array[1])
        A = numpy.random.random((x, x))
        b = numpy.random.random((x, 1))
        y = problem2(A,b,method)
        if y != None:
            x_values.append(x)
            y_values.append(y)
    t = numpy.polyfit(x_values, y_values, 3)
    return t


# In[ ]:





# In[ ]:




