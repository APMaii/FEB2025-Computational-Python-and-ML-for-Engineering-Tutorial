
"""

In The Name of GOD

Created on Wed Apr  9 18:05:38 2025

@author: apm



-------L13-------------
Numerical Modeling


-----Fuynctions, class ----------

-----Libraries------

timedate ---> time.now()
math ---> amale riazi
Numpy ----> np.array()  []  [matrix] -------> amaliat ro sari anjam midad
matplotlib.pyplot --> plot() scatter() pie() bar() hist() 




----------------------------
Numerical------------- 
scipy
sympy



pip install scipy
pip install sympy

nasb mishan


scipy --> science ----> coefficient , zarib -->  focus --> hal haye adadi
sympy --> symbol ---> inaro equation --> moadele minevise





-----------------------------
data preprocessing ---> pandas
sklearn ---> Machine learning




"""


'''

Differentiation 
moshtagh



integral
antegral


scipy
sympy

'''

import scipy
import sympy


#matplotlib.pyplot.plot()
#scipy.integrate.tabe hast
#...



#KHODESHON mokhafaf

#import scipy as sp
#import sympy as sp

#sp.


#---- moshtaggh --------------

import sympy

#symbol
x=sympy.symbols('x') #x---> x variabel, symbol
#sin(x) + e**x
#math
#sympy .sin()  .exp()

f=sympy.sin(x) +  sympy.exp(x) #tabeye man


dfdx = sympy.diff(f,x)

#f'
print(dfdx) #exp(x) + cos(x)




#f''
dfdx2= sympy.diff(f,x,2)
print(dfdx2) #exp(x) - sin(x)


#tooye yek noghte bebinidesh 
#.subs


values=dfdx.subs(x,10) #=cos(10) + exp(10)
print(values)





#moshtagh nesbat b x y 
# z , x , y


x=sympy.symbols('x')
y=sympy.symbols('y')
z=sympy.symbols('z')
#-----
x,y,z=sympy.symbols('x,y,z')
f=sympy.sin(x*y)+ sympy.cos(y*z)

#x , y 

#df/dx df / dy **2

sympy.diff(f,x,1,y,2) #-x*(x*y*cos(x*y) + 2*sin(x*y))





#-----scipy--------
import numpy as np
#scipy ---> yekser tabe bekesham beron
from scipy.misc import derivative 

#symbols 
#be hamin sadegi sin(x) + cos (x)

#scipy --> function khdoet bayad besazi

def f(x):
    f=np.sin(x) + np.exp(x)
    return f


#f(10) # 22025.921773695827

#tabeye f ro moshatghegsho nesbat b x at point x=2 . dx = kh koochi
zarf=derivative(f,2,dx=1e-5)

print(zarf) #6.972909262614734





#===============================
#===============================
#===============================
#---------Integration-----------
#===============================
#===============================
#===============================

x=sympy.symbols('x')
f=sympy.sin(x)

zarf=sympy.integrate(f,x)
print(zarf) #-cos(x)


#limit az felan ja ta delan ja
zarf=sympy.integrate(f,(x,-1,1))
print(zarf) #0

#sympy.oo #infinity
from sympy import oo


zarf=sympy.integrate(f,(x,-oo,oo))
print(zarf) #AccumBounds(-2, 2)






x=sympy.symbols('x')
result=sympy.integrate(sympy.exp(-x),(x,0,sympy.oo))
print(result) #1







#----numerical iuntegration - quadrature
from scipy.integrate import quad, dblquad,tplquad


#---function
def f(x):
    return x

#f(x)=x

x_lower=0
x_upper=1
#2 ta khorji mide
zarf1,zarf2=quad(f,x_lower,x_upper)
print('integral value:',zarf1 , 'absolute error :', zarf2)
#integral value: 0.5 absolute error : 5.551115123125783e-15





x=sympy.symbols('x')
f=x
zarf=sympy.integrate(f,(x,0,1))
print(zarf) #1/2




from scipy.integrate import quad, dblquad,tplquad


#---function
def f(x):
    return x

#f(x)=x
x_lower=0
x_upper=np.inf #Infinity numpy

#2 ta khorji mide
zarf1,zarf2=quad(f,x_lower,x_upper)
print('integral value:',zarf1 , 'absolute error :', zarf2)
#integral value: 0.4999999961769933 absolute error : 5.7336234760563265e-06



#sklearn

#linearregression
#neuralnetwork --> mlp

#import sklearn

#sklearn.linear_model.linearregression
#sklearn.neural_networks.mlp_classifer

#from sklearn.linear_model import LinearRegression
#LinearRegression



#high dimentional integraton


def z(x,y):
    return np.exp(-x**2 - y**2)


x_lower=0
x_upper=10
y_lower=0
y_upper=10

val , abserr = dblquad(z, x_lower, x_upper , lambda x : y_lower , lambda x: y_upper)

print(val, abserr)



#---------------------------------------
#---------------------------------------


'''

Numerical Modeling

hale adadi 

Karborde riaziat dar elm haye digar (shimi , mavad , polymer , .....)

brief , introduction ---------------------------

dar entheaye heat transfer equation ,  mass transfer, rheology ,.....

--> Equation (moadele) --> maodele kh moheme

raftare farayand ro neshon mide, farayadn , vakonesh , padide ,

agar betoonid oon rabtee ro hal konid --> javab haee beresid --->

baraye hal krdne moadelat -->


4*x+ 30 = 40

4*x = 10

x= 2.5 ---> ghelxzat --> 2.5



#---------
x**9 + x**7 + 8*x*2 + 19 =0 

x--> ghelzate motenasebe yek reactor



moadele differential --> kh pichide mishe


kh sade biaym va halesh konim , niaz darim b yekseri trick






------DASTE BANDI KONIM-----------
-------MOADELAT---------------

1-Moadelate jabri --> Algebra 
moadelat khati 4x + 8 = 0 
4*x = -8 ---> x = -8/4 = -2 --> tahlil 
raveshe tahlil analytical


2-sysstem haye moadelate jabri 
x + y = 8
2x + 9y = 10

tahlili hal mishan
ama tedad ziad beshe 100000 --> ina dg nmishe tahlili hal krd


3-non linear -- gheyre khati hastan 
4*x**2 + 3x

x**10  polynomial 
hendesi 
sin(x)* 4x + 9x + 3*x**2 =0


exp , logarithmic


4- sysmtes of non -linear hastan





------differential -------
dy / dx
d z / dx



5- ODE (ordinal differential equation)
dy / dx

6- PDE ( partial )
dy / dx  + dy / dz  + dy / dy


7, 8 ---> system of ODE , PDE

 





--------RAVESH HAYE HAL----------------
----------------------------------------

------Analytical ------- (tahlili)-------
sade bashe
yek format khasi bashe moadele --> analyticla estefadd  miona

4*x + 8 =0 
4*x = -8
x= -2


4*x**2 + 3*x + 20 = 0
a**x*2 + b*x + c
delta --->  tahlili 




-----Graphical --------------
#rasmesh

#sade bashe, shenakhte shode bashe






#system of linear equation
#non - linear equation 
#sysmte of non-linear
#ODE , PDE 




---------- Numerical --------------
#hale adadi ----> in ravesh ha mian va yek trick mizanan


#try error 

#x pressure 
# temeprature 
#kinetic criteria in tehrmodynamic



4*x*3 - 3*X - 10 =0 

tahlili ee vojod ndre
graphical 


4*x**3 = 3 * x + 10

x= 1 ---> 


4 * x **3 = 13

x ** 3 = 13/4 = 3.25


x= 1.1


4*x**3 = 3 * x + 10


4 * x **3 = 13.3

x---> 13.3 / 4 = 3.19 

x= 0.8


4*x**3 = 3 * x + 10




#----->
raveshe tekrar
iteration 

x --> samte rast
ba samte chao holohoshan yeki beshan


yeki mishan --> javabe moadeleye man --> Numerical  ( adadi)


taghribi --> khata 
ama kh jaha bekaremon miad


#----tekrar konam tekrar konam tekra rkonm

#ba dast sakhte
#ama ag yek funciton amn tooye python bnvims
#ba yek hlageye for
#aya nemishe in karo krd???


#-----MATLAB----
#Inja --->



#ma khialemon


ketbakhone mese scipy , sympy -- in tabe haro neevshtyan
yani shoma hata naiz ndrin tabe benevsii kafie
tabe ash ro bgiri va estefade koni




application of AI , python in Engineering


akarbordi estefade konim






#----------------------------------------------
sympy ---> symbols ----> analyticallll --> 
scipy ---> Numerical --> adadi , taghribi



'''


#-------------1 - Linear Algebra Equation-------------------
#----> khati va sade --> halehson konim

#analytical ------

from sympy import * 

#from sympy import symbols, ...

symbols()

#import sympy
#sympy.symbols()



x=symbols('x')
eq=8*x + 4

#sympy.solve()
sol = solve(eq,x)
print(sol) #[-1/2]



#-------

import sympy
x=sympy.symbols('x')
eq= 8*x + 4
sol = sympy.solve(eq,x)
print(sol) #[-1/2]



#-------- sympy.expand(f)------

from sympy import * 

#expand --->
#sympy.e

x=symbols('x')
f=(x+1)*(x+2)*(x+3)
res=expand(f)
print(res) #x**3 + 6*x**2 + 11*x + 6




#hendesi
a=symbols('a')
b=symbols('b')
f=sin(a+b)
res=expand(f,trig=True)
print(res) #sin(a)*cos(b) + sin(b)*cos(a)




#------sympy.simplify-------
x=symbols('x')

simplify(((x+1)*(x+2)*(x+3))) #(x + 1)*(x + 2)*(x + 3)


a=symbols('a')
simplify(sin(a)**2 + cos(a)**2) #1

simplify((cos(x)/sin(x))) #1/tan(x)


#------apart / together
#

f= 1/ ((a+1)*(a+2))
apart(f)
#-1/(a + 2) + 1/(a + 1)


f=-1/(a + 2) + 1/(a + 1)
together(f) #1/((a + 1)*(a + 2))


#-----zigma ----> sum 

n=symbols('n')
Sum(1/n**2,(n,1,10)) #Sum(n**(-2), (n, 1, 10))



Sum(1/n**2,(n,1,10)).evalf() #1.54976773116654


#zigma 1/n**2  n--> 1 , 10 

#1 / 1**2 + 1/2**2 + 1/3**2 ,...



Sum(1/n**2,(n,1,oo)).evalf()  #1.64493406684823

#----lim---
#---limit

#sympy.limit()

limit(sin(x)/x , x, 0) #1




#---sympy.series


series(exp(x),x)
#1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + O(x**6)

series(exp(x),x,1)
#E + E*(x - 1) + E*(x - 1)**2/2 + E*(x - 1)**3/6 + E*(x - 1)**4/24 + E*(x - 1)**5/120 + O((x - 1)**6, (x, 1))

series(exp(x),x,1,10)


#E + E*(x - 1) + E*(x - 1)**2/2 + E*(x - 1)**3/6 + E*(x - 1)**4/24 + E*(x - 1)**5/120 + E*(x - 1)**6/720 + E*(x - 1)**7/5040 + E*(x - 1)**8/40320 + E*(x - 1)**9/362880 + O((x - 1)**10, (x, 1))


series(exp(x),x,0,10)
#1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + x**6/720 + x**7/5040 + x**8/40320 + x**9/362880 + O(x**10)








#------
x=symbols('x')
eq=8*x + 4
#sympy.solve()
sol = solve(eq,x)
print(sol) #[-1/2]







#-------------2 - Non - Linear Algebra Equation-------------------


#------> analytical --> sympy------
#x**2 -5x + 6 =0
#(x-2)(x-3)=0

#x=2 , x=3

#sympy.solve()  --> analythical --> linear, non-linear --> simple


x=symbols('x')
eq=x**2 -5*x +6
sol = solve(eq,x)
print(sol) #[2, 3]



x=symbols('x')
eq=sin(x) - 0.5
sol=solve(eq,x)
print(sol) #[0.523598775598299, 2.61799387799149]


x=symbols('x')
eq=log(x) -10
sol=solve(eq,x)
print(sol) #[exp(10)]



#-----8*x**7 ,... complex-----> numerical
#f(x) =0 --> x

#iteration method --->  g(x) = x  
#wegeshtain method --> speed
#newton method --> moshtagh
#secant method ---> newyon method bedone msohtagh
#bisection --> f(a).f(b) <0 c=a+b/2




#----bisection method-------
from scipy.optimize import bisect

def f(x):
    return x**3 - x - 2


#a,b

root=bisect(f,1,2)

print(root) #1.5213797068045096


r=1.5213797068045096
myfunc=r**3 - r - 2
print(myfunc) #-3.446132268436486e-13 ---> 0




#-----newton-------
from scipy.optimize import newton

def f(x):
    return x**3 - x - 2

#mohstaghesham besazi

def df(x):
    return 3*x**2 -1

root=newton(f,x0=1.5,fprime=df)
print(root) #1.5213797068045676



#--------moshtagh ---------
#secant---------
from scipy.optimize import newton

def f(x):
    return x**3 - x - 2

#moshtagh enemigiri

#bejaye moshtagh, hadse dovom midi
root=newton(f,x0=1.5,x1=2)
print(root)  #1.5213797068044876




#----fixed-point iteration 
#g(x)=x

from scipy.optimize import fixed_point

def f(x):
    return (x+ 2/x)**0.5


root= fixed_point(f,x0=1.5)
print(root) #1.695620769559862






#---analythica-----
x=sympy.symbols('x')
f=x**3 - x - 2
res=sympy.solve(f,x)
print(res)

'''
[(-1/2 - sqrt(3)*I/2)*(sqrt(78)/9 + 1)**(1/3) + 1/(3*(-1/2 - sqrt(3)*I/2)*(sqrt(78)/9 + 1)**(1/3)), 1/(3*(-1/2 + sqrt(3)*I/2)*(sqrt(78)/9 + 1)**(1/3)) + (-1/2 + sqrt(3)*I/2)*(sqrt(78)/9 + 1)**(1/3), 1/(3*(sqrt(78)/9 + 1)**(1/3)) + (sqrt(78)/9 + 1)**(1/3)]

'''

#-------numerical sympy

#nsolve   #----> numerical solving

#solve --> analythical

x=sympy.symbols('x')
f=sympy.Eq(x**3 - x - 2,0)
root=sympy.nsolve(f,x,1.5)
print(root) #1.52137970680457

#az ch methodi estefasde mikone sympy --> dsgahigg
#yek ravehs haee , newton ,bisect , ... gharoghati 




#_--------scipy
from scipy.optimize import root
#mix ......
def f(x):
    return x**3 -x -2

x0=1.5

sol = root(f,x0,method='hybr')
print(sol.x) #[1.52137971]

#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html






'''

Systmes of Linear algebric

systems of Non-linear algebrics



in tabe ha system ha ham javab mide





file python teelrgam 1600 khat kamel oonja tadris --> src



'''


#analyticalll------

x,y = sympy.symbols('x y')
eq1=sympy.Eq(2*x + 3*y,7)
eq2=sympy.Eq(4*x - y , 5)

solution = sympy.solve((eq1,eq2),(x,y))


print(solution)
#{x: 11/7, y: 9/7}


#LUDECOMPOSITION 
#Matrix row reduction 9RREF
#DECMPOSITION
#mATRIX INVERSION

#_---> src





#_-------------------

'''
scipy

coefficient

3x + 2y = 5
1x + 4y = 6

 
zaribe x , y --> majhool
3 2  
1 4  



javab
5
6
    



'''

a=np.array([[3,2],[1,4]])
b=np.array([5,6])


from scipy.linalg import solve

x = solve(a,b)

print(x) #[0.8 1.3]


#x , y --> numerical 






#-----------------------------

'''


Differential Equations

dy / dx



Ordr --->  dy*2 / d*x




ODE --> Ordinary differential equatins --> dy / dx

PDE --> Partial differential --> ro y / ro x + ro y / ro z




FEM --> PDE ---> systems of linear algebric equation --> solve






-------ODE------
F(x,y,y',y'',....)=0

first order ---> dy/dx + y =0

second order ---> d2y/d2x + dy/dx + 2y =0



------PDE-------
F(x1,x2,y,dy/dx1 , dy/dx2 , ....)=0

first order ---> ro u / rox + c  + ro u / ro t =0

second orderd --> ro u*2 / ro x*2 + ro u*2 / ro t*2 = 0





analythical --> nadere , kh kh sade bashe

numerical adadi hal konid

'''


'''

----ODE----------


tahlili hal shan --> dar soratie , yek formate khasi ro dare


SEPERATION OF VARIABLES --> DY/DX = G(X)*G(Y)
M(x,y)dx + N(x,y)dy = 0 
bernouli 
P(x) = Q(x)






**analytical --> exact daghigh behet , equation ---> sade bashe

**numerical --> approximation (taghirbi) --> javab dare baraye pichide tairn maodelat


'''



#--------sympy-----------

x= sympy.symbols('x')
#eq ,...
y=sympy.Function('y')(x)

#dy/dx...

#dy/dx
ode= sympy.Eq(y.diff(x),x*y)
solution = sympy.dsolve(ode,y)
print(solution) #Eq(y(x), C1*exp(x**2/2))
 
#sympy.solve --> analytical mamoplie
#sympy.nsolve --> numerical

#sympy.dsolve --> analytical --> differential 




#y''2 +3y' + 2y=0
x= sympy.symbols('x')
y=sympy.Function('y')(x)

ode=sympy.Eq(y.diff(x,x)+3*y.diff(x)+2*y,0)


solution= sympy.dsolve(ode,y)

print(solution)
#Eq(y(x), (C1 + C2*exp(-x))*exp(-x))





'''
Euler-----
Runge-Kutta-----



goroh ---> na shenas --> nazarsanji 



afrad alagheman db numerical solution of Differential ODE , PDE 


-----> yeksaat ezafe jalaseye ayande --> scipy ravesh ahsho khedmateton bande tadris




Source ---> ro khdmateton ersal mikonam



1500 khat 


tAMAME RAVESH AHRO --> PYTHON 

ba tozihat




ai.2024.pilehvar@gmail.com











more information:
 
    
    https://docs.scipy.org/doc/scipy/
    https://docs.sympy.org/latest/index.html
    

'''























