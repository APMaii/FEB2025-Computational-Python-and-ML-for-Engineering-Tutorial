"""
In The Name of GOD

Created on Sun Apr  6 18:06:27 2025

@author: apm

L12


--------Python fundemental ---
-------Libraries------------

Ketabkhone 

import ketabkhone

ketabkhone.function()


import ketabkhone as mokhafaf

mokhafaf.function()



from ketabkhoone import function

function()






--------application----

math ---> riaziat --> math.pi
math.sin()
math.cos()
math.sqrt()


datetime---> .now()



#------------------

Numpy --> array



"""

import numpy as np

a=np.array([1,2,3,4])

#array --> fast > list
# > 1DS

#2D


#array --->> 

#.ndim
#.size
#.shape


#[index]

#[radif,soton]


#koli trab e dakhelesh bood k mitonesim estefade konim


#niazi nist k inaro hefrz konim


#a.mean()
#a.sum()
#a.min()
#a.max()


#a.max(axis)

#a+b ---> matrix 

'''
matplotlib 



pip install matplotlib





'''


import matplotlib.pyplot as plt

#matplotlib.pyplot


#plt

import numpy 
import matplotlib.pyplot 


x=numpy.arange(0,10)
y=numpy.arange(0,100,10)

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,10)
y=np.arange(0,100,10)

plt.plot(x,y)
plt.show()


#--------------
'''


IDE --> SPYDER


--> jupyter notrebook

'''





import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for a professional look
sns.set_palette("deep")

x=np.arange(0,10)
y=np.arange(0,100,10)


# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, s=100)

# Customize the plot
plt.title('Scatter Plot', fontsize=14, pad=15)
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)

# Add grid and customize its appearance
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

x=np.random.normal(5,3,(10000,))
# Create histogram with optimal binning and density plot
sns.histplot(data=x, stat='density', kde=True, 
             color='#2E86C1', alpha=0.9,
             edgecolor='black', linewidth=2)

# Customize the appearance
plt.title('l12 pLOT', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('student scores', fontsize=12, fontweight='bold')
plt.ylabel('Density', fontsize=12, fontweight='bold')

# Customize the grid
plt.grid(True, linestyle='--', alpha=0.3, which='major')
plt.grid(True, linestyle=':', alpha=0.2, which='minor')

# Customize the spines
for spine in plt.gca().spines.values():
    spine.set_linewidth(1.5)

# Add minor ticks
plt.minorticks_on()

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()


#--------------------------------

'''

MATH ---> Riazi
DATETIME --. TIME

NUMPY -----> narray moahsebate sari
matplotlib ---> rasm
seaborn 




scipy
sympy 
moadelat , mshtagh , integral, hal koni
hale tahlili , hale adadi, FEM 


#----------

pandas ---> excel vared konim , pak sazi , kar ba dade

Scikit learn --> SKLEARN --> AI --> focus


Deeplearning --> Intro
'''


#-----------------

'''

scipy

sympy

'''

#yek moadele dari


# 4*X**2 + 3*X + 8 =0


#yek tabe e bsazam k btoone #hal kone
#Moadele daraje do ro 

#ch vorodi ee bgire
#chi khoroji bde???


'''




Input ---> tabe --> output



'''

def hale_moadele(moadele):
    pass
    
    






#hale_moadele(5*x**2+3*x+4)

'''

a*x**2 + b*x + c =0



4x**2 + 3x + 6=0

a=4
b=3
c=6




a,b,c ---> function --> khoroji (x)



'''





import math

def hale_moadele(a,b,c):
    
    delta= b**2 - 4 * a * c
    
    if delta<0:
        return None
    
    elif delta==0:
        r=-b/2*a
        return r
    
    elif delta>0:
        r1=(-b + math.sqrt(delta))/2*a
        r2=(-b - math.sqrt(delta))/2*a
        
        return r1,r2


#5*x**2 + 3*x + 8=0

zarf=hale_moadele(5,3,8)



print(zarf) #None

#5*x**2 + 3*x - 8=0


zarf=hale_moadele(5,3,-8)
print(zarf)
#(25.0, -40.0)

#x**2 - 100 =0 

#x=10


zarf=hale_moadele(1,0,-100)

print(zarf)
#(10.0, -10.0)



# zarib dadfam


'''

scipy --> science python

--> zaribi kar mikone 

hale adadi hast




#------------------------
sympy 


eq=4*x**2 + 3*x -8 

symbol --> 



#-----------------
dar do jalaseye ayand e--> maodelat 

scipy , sympy ---> numerical modeling
hale adadiu, integral, moshtagh ,.....


scipy --> kole focus numerical , coeff (zaribi)
sympy ---> tabe haye dakheelsh , equation symbolic , analytical 



pip install scipy
pip install sympy

'''

import scipy 
import sympy











