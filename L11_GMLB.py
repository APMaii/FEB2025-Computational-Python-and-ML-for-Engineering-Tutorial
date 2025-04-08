
"""
In The Name of GOD


Created on Sun Mar 30 17:53:45 2025

@author: Ali Pilehvar Meibody

----L11----------


function ---> output=name(input)

import lib as mokhafaf

mokhafaf.function(input,....)


---> math --> riaziat --> GMLB_L10.py
----> datetime

--> Numpy




-----Variables-----
---> int , float, complex
---> str 
---> Boolean

---> Iterables --> multiple variables
List,set,tuple, dictionary ,......


List---> 2 disadvantage ---> 
1---> Fast --> Python , memory 
2----> 1D



--> Numpy --> numpy array (araye, matrix, matrices)

Fast (60X ) ---> C , C++
1D,2D,3D,........






"""

import numpy as np

#--->array

#----> array 

#np.array([])

#-------0D-------
a1=np.array(12)

a1.ndim #0
a1.size #1
a1.shape # ()

#-----1D-----
#list --> a1=[10,20,30,40]
a1=np.array([10,20,30,40,50,60])

#string, boolean, .... adad

a1.ndim #1
a1.shape # (6,)
a1.size #6

a1[1] #20

a1[1:4] #array([20, 30, 40])


a1[1]=200

print(a1) #[ 10 200  30  40  50  60]



#-----2D-----------
#dovodi--> jkadval


#radif, sotoon
  
a1=np.array( [ [10,20,30] , [40,50,60]   ] )
#2 ta radif
#3 ta sotoon
a1.ndim #2
a1.size #5
a1.shape # (2, 3)

#dastresi--> a1[2] 
#indexe radif, indexe sotone
#a1[indexe radif , indexe sotoon]

a1[0,2] #30

a1[0,2]=400

print(a1)
'''
[[ 10  20 400]
 [ 40  50  60]]
'''



#_-------3D-------

#kodom jadval, kodom radfif kodom sotoon

a3=np.array([ [[1,2,3],[4,5,6]    ] , [ [7,8,9],[10,11,12]  ]  , [ [13,14,15],[16,17,18]  ]      ])

a3[1,1,2] #12\
    
a3[1,1,2]=400  

print(a3)
'''
[[[  1   2   3]
  [  4   5   6]]

 [[  7   8   9]
  [ 10  11 400]]

 [[ 13  14  15]
  [ 16  17  18]]]

'''


#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
#------OTHER ASSIGNMENT--------
#-------------------------------
#-------------------------------
#-------------------------------

#arange
zarf=np.arange(0,20,2)
#array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

#aazinja b bad man zarf nmizrm ama yademon bashe bayad
#zarf bzrim zakhire konim

#In ravesh ha bjaye innke benevism np.array b kar mire


np.arange(0,100)
'''
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])

'''

#asahih


#ashari ---> az 0 ta 20 ro 10 ghesmat kon

np.linspace(0, 20,10)
'''
array([ 0.        ,  2.22222222,  4.44444444,  6.66666667,  8.88888889,
       11.11111111, 13.33333333, 15.55555556, 17.77777778, 20.        ])

'''


#_--------------
#adadi begid
#hame ro 0 mikone
#hame ro 1 mikone
#hamaro full mio

#shape


#(4,) --> 1D --> tedad element 
#[1,2,3,4]

#(4,2)  --> 4 ta radif , 2 ta sotoon


np.zeros(10)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])


np.zeros((4,2))

'''
array([[0., 0.],
       [0., 0.],
       [0., 0.],
       [0., 0.]])
'''

#4 ta RADIFFFFFFF
#2 TA SOTOOON

zarf=np.zeros((4,2))

zarf.ndim
zarf.size
zarf.shape # (4, 2)


np.empty(10)
#array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])


np.ones(10)
#array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

np.ones((2,8))
'''
array([[1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1.]])

'''

#aval shape , ba chi fullesh kone

np.full(10,4)

# array([4, 4, 4, 4, 4, 4, 4, 4, 4, 4])

np.full( (4,2) ,3.14   )
'''
array([[3.14, 3.14],
       [3.14, 3.14],
       [3.14, 3.14],
       [3.14, 3.14]])
'''
#tedad migire

#2 bodi --> martix mroabne

#3 X 3

np.eye(3)
'''
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
'''


np.eye(4)
'''
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])

'''

#vataro 1 fgjht mzr

np.diag([1,2,3])
'''
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
'''

np.diag([10,20,30,40])
'''
array([[10,  0,  0,  0],
       [ 0, 20,  0,  0],
       [ 0,  0, 30,  0],
       [ 0,  0,  0, 40]])
'''

#-----> save koni numpy array 

#IDE 

#np.save(file, arr)
a1=np.load('random_matrix.npy')


#---------------------------------
#---------RANDOM NUMBERS----------
#--------------------------

#yek adade random beyne 0 va 1
#1D --> 10 ta elemnt dashte bashe
#har element y adade random beyne 0 va 1 bashe

#===============float random between 0 and 1 ========

np.random.random(10)
'''
array([0.48814505, 0.67794194, 0.46145483, 0.4100598 , 0.10564777,
       0.31265719, 0.14322925, 0.96145286, 0.52090944, 0.0199149 ])
'''

np.random.random((2,4))
#2 ta radiuf, 4 ta sotoonn 
#az 0 ta 1 
'''
array([[0.6876889 , 0.6836344 , 0.88757185, 0.53467167],
       [0.36730633, 0.13328727, 0.20937025, 0.15859439]])
'''


#===============Integer random between two boundary ========
#az 0 ta 10 boro adade sahih vardar

#(adade aval, adade dovom , shape)
np.random.randint(0,10,10)
# array([0, 9, 4, 6, 2, 4, 1, 9, 3, 0])

np.random.randint(0,10,(2,1))
'''
array([[8],
       [7]])
'''




#-------Float radnom between two boudnary------
#--- a ta b --> random bvardar


#tamame adasd ha beyen 10 ta 80 --> 
#10.1 , 10.8 , 11, 11.3 shanse barabar daran baraye entkehab shdon

#uniform distribution
#(aval,dovom , shape)
np.random.uniform(0,10,5)
# array([3.4806908 , 4.58217792, 7.21409665, 2.18030593, 8.59648123])


#----normal, gaussian

#---> yek adadi oon vasat kh ehtemal dare oon adado entkehab kone

#az 0 ta 10 --> 5 bishtar nazdik b 5 bere vardare

#normal ---> mean ---> oon adad vasatie chi bashe
#sigma---> 

np.random.normal(5,2,10)
'''
array([ 5.28445672,  3.97313484,  3.76093464,  7.06018887,  3.85016409,
        3.61048531,  2.51881837, -1.3431838 ,  5.07191635,  4.54158363])

'''

#( mean , enheraf az meyar , shape)

np.random.normal(5,2,(2,4))
'''
array([[3.40864979, 4.20629652, 6.89303948, 3.37088691],
       [9.42409915, 6.53156828, 7.35088028, 3.43936462]])
'''


#-------------------ARRAY ro darim-----
#Function mikhaym k bahashon betonim kar konim-----

a=np.arange(0,10)

a=np.random.normal(10,1,(4,6))

print(a)
'''
[[10.53097005 10.11698644  9.97461633 11.15592138  8.97697398 11.22074576]
 [10.76289721  9.31903534  9.2522473   8.83764697 11.21034521  9.5243948 ]
 [10.68667969 10.74081979  8.50661117  9.38791068  9.44339527 10.10501444]
 [ 9.53784524 10.2639371  10.41086787  8.9056589   8.90558763  9.76211804]]
'''
a.size
a.ndim
a.shape

a.dtype # dtype('float64')

a.astype('')


b='salam'
b.upper()


#koli tabeye tdkahelie numpyu ro dare k
#behemon ejaze mide tagirat ro emal jmonim


a.astype(int)
'''
array([[10, 10,  9, 11,  8, 11],
       [10,  9,  9,  8, 11,  9],
       [10, 10,  8,  9,  9, 10],
       [ 9, 10, 10,  8,  8,  9]])
'''

#a ro taghir nnmide

#Kkhoroji midan

#Oon numoy array taghir nmikone balke
#taghirat roosh emal mishe


#-----------copy , view
arr2=a.view()
arr3=a.copy()


#------filtering-------

A=np.array([10,20,30,40,50])
#np.arange(10,110,10)


row_index=[1,2,3]

A[1:4]
A[[1,2,3]]
A[row_index]

#pa faratar bzri
#esme
mask=[False,True,True,True,True]

A[mask]
# array([20, 30, 40, 50])

mask= (A>10)
A[mask]


A[A>10] #array([20, 30, 40, 50])


A[A==20]


#shart mizari jaye index behet pas mide

#------------khode array kolesho 
#moghayese koni

A=np.array([10,20,30,40,50])


A>5
#array([ True,  True,  True,  True,  True])


A>100
#array([False, False, False, False, False])

A>30
#array([False, False, False,  True,  True])

#==
#!=
#>
#>=
#<
#<=



#_------where --> migarde

A=np.array([10,20,30,40,50])
np.where(A==20) # (array([1]),)

#np.where(shart)

np.where(A>25) # (array([2, 3, 4]),)



#----------------------
#---------------------
#join two arrays-------
#-----------------------

a=np.array([10,20,30,40])
b=np.array([100,200,300,400])

#np---> concatenate

c=np.concatenate([a,b])
print(c)
#[ 10  20  30  40 100 200 300 400]

a=np.array([ [10,20,30],[40,50,60]])

b=np.array( [ [1,2,3],[4,5,6]  ])


np.vstack #vertical
np.hstack #horizontal

np.vstack([a,b])
'''
array([[10, 20, 30],
       [40, 50, 60],
       [ 1,  2,  3],
       [ 4,  5,  6]])

'''
zarf=np.vstack([a,b])

np.hstack([a,b])
'''
array([[10, 20, 30,  1,  2,  3],
       [40, 50, 60,  4,  5,  6]])
'''



#concat() , hstack() , vstack()
#axis ---> 0 , 1 
#radifi, sotooni



#-------------Array calculations--------

x=np.arange(0,10)

print(x)
#[0 1 2 3 4 5 6 7 8 9]

#1D , 2D ,.....


#karhaee k ba adad anajm midadi ro
#biay ba in matrix ha anjuam bdi
#+ - * ,. ba tak take elemnt ha inkaro koni


x+5
#array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])


new_array=x+5

#minevsiamo shoma mitoni khoroji bgiri

x-5

x*2

x**2

# array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])

#/


#comparison
x>10
#array([False, False, False, False, False, False, False, False, False,
#       False])


#+ - * ** / --> javab yek array jadid mide
#k in computation dakhele elemnt elemnt emal shode



#numpy tabe dare haminkar
a=np.array([1,2,3])
b=np.array([5,6,7])
np.add(a,b) #array([ 6,  8, 10])

np.add() #+
np.subtract() #-
np.negative() #-
np.multiply() #*
np.divide() #/
np.power(a,2) #*   array([1, 4, 9])
np.absolute(a) #absolute (gfhadre motlagh ro pas mide)
np.abs(a)


#------> < == !=
np.equal() #==
np.not_equal() #!=
#a==b
np.less()
np.less_equal()
#np.greater()
#np.greater_equal() #<=


#------Tabe haye mosalasati darim
#0 --> 90 

theta=np.linspace(0,np.pi,3)
print(theta) #[0.         1.57079633 3.14159265]

np.sin(theta) # array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])

#vase done done element in kararo njam mide

np.cos(theta)

np.tan(theta)

np.arcsin(theta)

#dakhele done done elemnt kar haro anjam mide

#logarim
#math.log(10)

a=np.array([10,20,30,40,50])
np.log(a) #@ array([2.30258509, 2.99573227, 3.40119738, 3.68887945, 3.91202301])


a=np.random.normal(5,0.1,10)
print(a)
'''
[5.01128395 4.9381221  5.0792782  5.10249124 5.10994037 4.94357307
 4.93070945 5.03763245 4.98761032 5.01425982]
'''


#ger roo b paeen
np.floor(a)
#array([5., 4., 5., 5., 5., 4., 4., 5., 4., 5.])


#roo be bala
np.ceil(a)
#array([6., 5., 6., 6., 6., 5., 5., 6., 5., 6.])





#-----------------------------
#-----Statisticalll----------
a=np.array([10,20,30,40,50])


a.sum() #np.int64(150)

#min
#max

a.min() #10
a.max() #50

a.argmax() #4  idnexe 4


a.mean() #4


'''

np.var()
np.prod()
np.std()
np.min()
np.max()
np.argmax()
np.argmin()
np.mean()
np.median()
np.percentile()

'''


#----- 1D------


#----2D------

a=np.array([ [10,20,30], [40,50,60]])
print(a)
'''
[[10 20 30]
 [40 50 60]]

'''



a.sum() #210
 
a.max() #60
a.min()

#a.mean()
#a.var()


#fght too felan soton, felan radif

#a.min()

a[0,:].min()

#dastresi peyda kon bad min() , max ,....


#too dele tabe ha axis ---> kol


a.min(axis=0) #done done soton
#array([10, 20, 30])

a.min(axis=1)
#rray([10, 40])

a.min() #10

a.sum() #210

#too har soton sum chn mdishe
a.sum(axis=0)
#50, 70, 90

a.sum(axis=1)
#array([ 60, 150])



#2D----> khode tabe ha bsorate khalie
#ham elewmeent haro kenare ham michinan

#ama to gahan naiz dari bgi agha 
#to felan soton , felan radif



#----------------------
#------Iteration in numpy-----

a=[10,20,30,40,50]


for i in a:
    print(i)



a=np.array([10,20,30,40,50,60])

for i in a:
    print(i)
'''
10
20
30
40
50
60
'''



#2D???

#avalin for --> vase har radif


a=np.array([ [10,20,30] , [40,50,60] , [70,80,90]   ])

for i in a:
    print(i)

'''
i= [10 20 30]
i= [40 50 60]
i=[70 80 90]
'''




for i in a:
    for j in i:
        print(j)
        
'''
10
20
30
40
50
60
70
80
90
'''

#------------------------------------

a=np.arange(0,10)

print(a)
#[0 1 2 3 4 5 6 7 8 9]

#1D--->2D

#2D, 3D

#2D-->1D


#----> reshape()

a.ndim #1
a.shape #(100,)


#2d--> 2 ta radif, 5 ta stoon
a.reshape((2,5))
'''
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
'''


a=np.arange(0,10).reshape((2,5))



#2 ta radif, 



a=np.arange(0,96)

#2 ta radif

b=a.reshape((2,-1))

#-1 --> khodet hesabv kon


#---------------------------
b.shape #(2, 48)


b.reshape((-1,))


#----------------------------------
#----------------------------------
'''

Pypi --- > Install, package

github ---> souce code 

google --> search bzni too site aslish
documentation ---->  get started , 

https://numpy.org/doc/stable/user/basics.creation.html




numpy --> har ketabkhone ee pip install
github source, documentation --> khondaneshe




-----------------
datetime
math


numpy ----> array (bejaye list -->mohasebat)

matplotlib ---> rasm hast 


matplotlib.pyplot

pip install matplotlib

black window --> terminal , cmd.exe

enter --> install


'''


import matplotlib.pyplot as plt

#hich errori nadad --> installesh krdi



#source?
#https://github.com/matplotlib/matplotlib


#har tabe ee hast dakhele plt hast

x=[10,20,30,40]
y=[100,200,300,400]

#y ro bar asase x bekesham
plt.plot(x,y)
plt.show()


#in samte rast oon bala bbinesh

#koli taghirat bdm

plt.plot(x,y,'*',ms=20)
plt.show()



'''

SPYDER ---> run koni


---> tasvir dare

spyder AMOOZESH 


jupyter --> spyder, IDE, --> tutorial


'''

x=[10,20,30,40]
y=[100,150,200,250]
plt.plot(x,y)



plt.xlabel('x haye man')
plt.title('nemodoare man')
plt.ylabel('y haye man')
plt.ylim(0,400)
plt.xlim(0,50)

plt.show()











