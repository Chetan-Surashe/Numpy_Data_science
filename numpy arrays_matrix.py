# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:11:56 2023

@author: Chetan Surashe
"""
#index a one dimensional array
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data) #[11 22 33 44 55] printing an array
#index data
print(data[0])
print(data[4])

#index array out of bound
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[5])
#IndexError: index 5 is out of bounds for axis 
#0 with size 5

######################

#negative array indexing
from numpy import array
#define array
data=array([11,22,33,44,55])
#index data
print(data[-1])  #55
print(data[-5])  #11
#negative indexing start from end of array 
#with -1 index while positive indexing start with
#0 by default from starting of array

#########################

#index two dimensional array
from numpy import array
#define array
data=array([[11,22],
            [33,44],
            [55,66]])
#index data
print(data[0,0])  #o/p= 11
###################

#index row of two dimensional array
from numpy import array
#define array
data=array([[11,22],  #0th row
            [33,44],  #1st row
            [55,66]]) #2nd column
print(data[0,])  #0th row and all column
#o/p= [11,22] 
#########################

#slice a one dimensional array
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[1:4])
#in slicing the last specified index is excluded
#o/p-[22 33 44] --> 22 at 1st index and
# 44 at 3rd index 4th index is excluded

###############################

#negative slicing of one dimensional array
from numpy import array
#define data
data=array([11,22,33,44,55])
print(data[-2:])
#as negative indexing start from -1 and from end
#of the array [-2:] last index is not given 
#so it print -2 to -1 i.e. [44 55]

#in this also last index is excluded
#eg. [-5:-2] o/p=[11 22 33] -2 index i.e. 
#44 is excluded

##############################

#split input and output data
from numpy import array
#define array
data=array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#separate data
x,y=data[:,:-1],data[:,-1]
x
y
print(x)
print(y)

#x=[:,:-1]--> first : denotes take element from 
# staring row to ending row & second--> , :-1
# denotes starting from 0th column to last column
#i.e -1 index but it is excluded as it is specified 
# o/p= array([[11, 22], 0th row & 0th and 1st column
#            [44, 55],  1st row & 0th and 1st column
#            [77, 88]]) 2nd row & 0th and 1st column
#here all rows and all columns are printed
# except last 

#y=[:,-1]--> take all rows and only last column
#o/p= array([33, 66, 99])
#here all rows and only taking last column
#so 33 0th row and last column
#   66 1st row and last column
#   99 2nd row and last column


#############################

# broadcast scalar to one dimensional array
#broadcast --> send out/put out
from numpy import array
# define array
a=array([1,2,3])
print(a) #[1 2 3]
#define scalar
b=2
print(b) #2
#broadcast
c=a+b
print(c) #[3 4 5] -->  2 is get added in each 
# digit in 'a' i.e. 2+[1,2,3]

####################################

#vector addition 
#1d array is called vector
#2d array is called matrix 
#more than 3 called Tensor
from numpy import array
#define first vector
a=array([1,2,3])
print(a) #[1 2 3]
#define second vector
b=array([1,2,3])
print(b)  #[1 2 3]
#add vectors
c=a+b
print(c) #[2 4 6]

##############################
#vector substraction
from numpy import array
#define first vector
a=array([1,2,3])
print(a)  #[1 2 3]
#define second vector
b=array([0.5,0.5,0.5])
print(b)  #[0.5 0.5 0.5]
#substract vectors
c=a-b  
print(c) #[0.5 1.5 2.5]

###############################################

#vector L1 norm
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
print(a)  #[1 2 3]
#calculate norm
l1=norm(a,1)
print(l1)

#L1 Norm (Manhattan Norm or Taxicab Norm):
#The L1 norm of a vector is the sum of the
# absolute values of its components.

# Mathematically, it is calculated as:
#||a||1=|a1|+|a2|+....+|an|

#You are using the norm function with
#the ord parameter set to 1, which indicates that
# you want to calculate the L1 norm. The result 
#is stored in the variable l1.
#For the vector a = [1, 2, 3], the L1 norm is
# calculated as: 
#||a||1=|1|+|2|+|3|=1+2+3 = 6  = 6.0

##########################################
#vector L2 norm
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
print(a)   #[1 2 3]
#calculate norm
l2=norm(a)
print(l2) #3.7416573867739413

#L2 Norm (Euclidean Norm):
    
#The L2 norm of a vector is the square root of 
#the sum of the squares of its components.

# Mathematically, it is calculated as:
#||a||2= sq root(1^2+2^2+3^2)=sq root(2+4+9)=
#= sq root(14)=3.7417 (rounding off)

#So, l2 will be equal to the square root of 14,
#which is approximately 3.7417 
#(rounded to four decimal places). 

########################################

#triangular matrices  -->image processing,croping img
from numpy import array
from numpy import tril #triangular lower
from numpy import triu  #triangular upper
M=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(M)
#lower triangular matrix
lower=tril(M)  
print(lower)  #[[1 0 0]
               #[4 5 0]
               #[7 8 9]]
#upper triangular matrix
upper=triu(M)
print(upper)     #[[1 2 3]
                 # [0 5 6]
                 # [0 0 9]]

###################################
#diagonal matrix
#A diagonal matrix is a special type of square
#matrix in which all the elements outside the 
#main diagonal are zero.
from numpy import array
from numpy import diag
#define square matrix
M=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(M)
#extract diagonal vector
d=diag(M)
print(d)  #[1 5 9]
#extracting only diagonal elements

#create diagonal matrix from vector
D=diag(d)
print(D)    #[[1 0 0]
            # [0 5 0]
            # [0 0 9]]

#printing whole diagonal array

#######################################

#identity matrix
from numpy import identity
I=identity(3)
print(I)
 
#########################

#orthogonal matrix
from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
Q=array([
    [1,0],
    [0,-1]])
print(Q)

# inverse equivalence
V=inv(Q)
print(Q.T)
print(V)

#Identity equivalence
I=Q.dot(Q.T)
print(I)
#############################################
