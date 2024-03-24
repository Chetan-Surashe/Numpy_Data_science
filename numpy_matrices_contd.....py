# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:04:35 2023

@author:Chetan Surashe
"""
from numpy import array
#define matrix
A=array([
    [1,2],
    [3,4],
    [5,6]])
print(A)
#calculate transpose
C=A.T
print(C)
#transpose matrix convert rows into column and 
#vice-versa

###############################

#invert matrix
from numpy import array
from numpy.linalg import inv
#define matrix
A=array([
    [1.0,2.0],
    [3.0,4.0]])
print(A)
B=inv(A)
print(B)
#multiply A and B
I=A.dot(B)
print(I)
#######################################

#sparse matrix
#in sparse matrix string is converted into matrix
#of 1's and 0's
from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix
A=array([
    [1,0,0,1,0,0],
    [0,0,2,0,0,1],
    [0,0,0,2,0,0]])
print(A)
#convert to sparse matrix(CSR method)
S=csr_matrix(A)
print(S)
#reconstruct dense matrix
B=S.todense()
print(B)

########################################
#program to get the numpy version and configuration
import numpy as np
print(np.__version__)
print(np.show_config())

#numpy program to get help with the add function
import numpy as np
print(np.info(np.add))

#numpy program to test whether none of the elements 
#of given array are zero(0)
import numpy as np
x=np.array([1,2,3,4])
print("Original array: ")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))  #print true if 0 is absent
######################################

#numpy program to test if any of the elements of a 
#given array are non zero

import numpy as np
x=np.array([1,0,0,0])
print("Original array: ")
print(x)
print("Test if none of the elements of the said array is non zero:")
print(np.any(x))
##########################################

#numpy program to test a given array element-wise
#for finiteness (not infinity not a number)
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original array: ")
print(a)
print("test a given array element-wise for finiteness: ")
print(np.isfinite(a))

#write a numpy program to test element-wise for 
# NaN of a given array
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print("Original array: ")
print(a)
print("test a given array element-wise for NaN: ")
print(np.isnan(a))
############################################

#write a numpy program to test element-wise for 
#complex numbers,real numbers in a given array.
#Also test if a given number is of a scaler 
#type or not.
import numpy as np
a=np.array([1+1j,1+0j,4.5,3,2,2j])
print("Original array: ")
print(a)
print("Checking for complex number: ")
print(np.iscomplex(a))          
print("Checking for real number: ")
print(np.isreal(a))   
print("Checking for scalar type: ")
print(np.isscalar(3.1)) #it is scalar-->TRUE 
print(np.isscalar([3.1])) #it is vector-->FALSE

##############################################
#numpy program to compute the multiplication 
#of two given matrices
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix: ")
print(p)
print(q)
result=np.outer(p,q)
print("outer product of the said two vectors: ")
print(result)
#######################################

#numpy program to compute the cross product 
#of two given matrices
import numpy as np
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix: ")
print(p)
print(q)
result1=np.cross(p,q)
result2=np.cross(q,p)
print("cross product of the said two vectors(p,q): ")
print(result1)
print("cross product of the said two vectors(q,p): ")
print(result2)