# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:33:24 2023

@author: Chetan surashe
"""
from numpy import array
#create array
l=[1,2,3]
print(type(l))
a=array(l)
#display array
print(a)
#display array shape
print(a.shape) #gives ans in row*cols
#display array data type
print(a.dtype)  #o/p--> float64
          #print(type(a))-->     <class 'numpy.ndarray'>
#create empty array
from numpy import empty
a=empty([3,3])
print(a)

#create zero array
from numpy import zeros
a=zeros([3,5])
print(a)

#create one array
from numpy import ones
a=ones([5])
print(a)

#create array with vstack
#vertical array is getting printed
from numpy import array
from numpy import vstack
#create first array
a1=array([1,2,3])
print(a1)

#create second array
a2=array([4,5,6])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)
############################

#create array with hstack
#horizontal stack(array)
from numpy import array
from numpy import hstack
a1=array([1,2,3])
print(a1)

#create second array
a2=array([4,5,6])
print(a2)
#horizontal stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)
##########################

#one dimensional list to array
#create one dimensionaal array
from numpy import array
#list of data 
data=[11,22,33,44,55]
type(data)
#array of data 
data=array(data)
print (data)
print(type(data))
################################
#two dimensional list --> lists to array
#create two dimensional array
from numpy import array
#list of data
data=[[11,22],[33,44],[55,66]]
#array of data
data=array(data)
print(data)
print(type(data))
