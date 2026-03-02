#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name of GOD


Created on Sun Mar  9 18:04:35 2025

@author: apm


L8


"""



'''

------LAST REVIEW ON BASIC PYTHON---------

Human ----- Python ---- Machine





Reserved Words-----------------

---Python built in functions (print(),input(),len(),type(),sum(),pow(),max(),min())
https://docs.python.org/3/library/functions.html

---keywords (if , if else, if elif else) , loops ( for, while) ,.. and , or , not , in 



Unreserved----------------------
Variables (moteghayer)
1-->numebrs (int,float.complex) operator ** * / + - ,....
2-->Boolean ( True, False) --> == != > >= < <=
3-->string (str) --> [index] , str function (.upper(),..)
4-->Iterables --> elements 
List, tuple, set, dictionary [ordere (index) , changable, allow duplicated]
[index] , functions (append() , remove() ,...)



---PSUDO CODE-----


Capsule --> BOX



Vooroodi ---> BOX --> khoroji 


applications:
    1---> codet khana va sade mishe
    2--> yeseri kara hast --> tekraresh koni 
    3--->baghie azash estefade konan
    4-.......
    



if shart:
    
    
    
    
if (shart):{
        dastooor ;}



'''


'''

TABE RO BENEVISAM

'''


'''

2 gehsmat

besazish (step1) --> run mikone -> sakhte mishe

estefade sedash bzni call (setp1)

'''


'''
ghesmate 1 --> sakhtane yek tabe (too zehnem inke)
yeja badan , man ya baghie ya ahrfardi gharare in tabe ro seda kone

'''

#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================
#=========================================

'''
sakhatar

mynumber=
chaarcteri _ . 
adad nmitoni avalesh biari
az esma hay ereserevshdoe printo ,....
,.....

my_numebrs
MyNumbers
my number XXXXX
my*numebrs XXXX

esme yek zarf ghavanin dahst , esme yek tabe ham hamon ghavanino dre



ta hade momken bayad esme yek tabe neshon bde oon tabe chikar mikone





def  namesho (VORODI):
    badane
    ...
    ...
    .
    
    

birone tab ehast 




#-----------------
def estefade koni
name ro byad bzari
parantez
too parantez -->esme vorodi hat  --> a , b , c




age chanta vorodi dahstam chi?

(minevisi, input2 ,inpu4 ,input4,......)




'''


a=20
b=40

c=a+b

print(c)




#tabe besazma benam esme JAM

'''
ghabel inke tabe besazi vorodi khoroji hato moshakahs koni


vorodii ----> BOX --> khoroji


vorodi----> ( paranteze)
khrooji --> ag dare---> return , nadare print()


'''


def JAM(a,b):
    c=a+b
    print(c)
    
    
    

'''
estefade

'''

JAM(10,20) #30


d=JAM(10,20)

#yek zarf msiaze bname d
#@jtabeyte JAM ro seda mizne
#a=10 , b=20 
#a+b -->30
#print(30)--> 30

#nadare

#d=None

print(d) #None



#--->aksare tabe ha vorodi, khoroji daran

def JAM(a,b):
    c=a+b
    #print(c)
    return c #harja esme JAM ro seda zad in adade k inja gozaashtam



d=JAM(10,20)
    


print(d) #30



#----** TABE 
'''

VORODI ()
BADANE --> HARKAIR DOS DARI BOKON (PRINT)

KHOROJI --> Return, y zarfd mzirn jolosh migirnsh

'''


def JAM(a,b):
    c=a+b
    return c 
   

    
d=JAM(10,20)




#------------------------

def JAM(a,b):
    c=a+b
    print(c)
   

JAM(10,20)    



d=JAM(10,20)




#-------------------------

def JAM(a,b):
    c=a+b
    return c
    print('saalam')
   



d=JAM(10,20) 



#----------------------------


#vorodi , khoroji 

#-----na vorodi na khoroji

def welcome():
    print('salam')
    
    

welcome()

#zarf bzrm? --->none
d=welcome()



#----vorodi dare, khoroji nde
def jam(a,b):
    c=a+b
    print(c)
    
    #return None
    
    
    
jam(30,20)

d=jam(30,20)



#--vorodi ndre khoiroji dare

def pi():
    return 3.14



d=pi()




#-------ham vorodi ham khoroji 
def jam(a,b):
    c=a+b
    return c

d=jam(10,20)




def jam(a,b):
    c=a+b
    print(c)
    return c

d=jam(10,20)


#---------------------------------------------------------
#calculator ---> 

'''

vorodi bgire

adad 1 , adade 2 , operator


--> javab ro (bede? print kone?)


'''

def calculator(number1,number2,operator):
    if operator=='jam':
        answer=number1+number2
        return answer
    
    elif operator=='tafrigh':
        answer=number1-number2
        return answer



d=calculator(20,10,'jam')


f=calculator(20,10,'tafrigh')


#-----------------------------------------------------
def calculator(number1,number2,operator):
    '''
    
    In tabe yek mashin hesab hast k adad 1 ro  ba adade 2 ro migire
    bar asare operator tasmim migire k ch kari kone va answer ra barmigardane
    
    operator haee k in tabe support mikone --> (jam, tafrigh, zarb, taghsim)
    

    '''

    
    if operator=='jam':
        answer=number1+number2
        return answer
    
    elif operator=='tafrigh':
        answer=number1-number2
        return answer



def calculator(number1,number2,operator):
    '''

    Parameters
    ----------
    number1 : float
        adade avale morede nazar.
    number2 : float
        adade dovome morede nazar.
    operator : str
        yeki az gozine haye robero (jam,tafrigh,zarb).

    Returns
    -------
    answer : float
        javabe mohasebe shoma.

    '''


    
    if operator=='jam':
        answer=number1+number2
        return answer
    
    elif operator=='tafrigh':
        answer=number1-number2
        return answer




#--------------------------------------------

#tabe ha miutonan default dashte bashan


#newton

#f=m*a

#JERM , nirooee bde -->jesm ba shetab a hrekat mikone


#nirooye 20 newton  , 10 kilogerame

# F= M * A 

#F/M = A 

#a=f/m = 20/10 = 2


#tabe besazam 
'''

Masale (farsi)

vorodi chian-->BOX -->khoroji chie 



niroo , jermo bede----> shetabo begre


F, m ---> BOX ----> a





'''




#def acceleration_calculator():   
#def newton_law():



#def acceleration_calculator(f,m): 

    

def acceleration_calculator(force,mass):
    
    acceleration=force/mass
    return acceleration



my_acc=acceleration_calculator(40,10)





#-----

def acceleration_calculator(force,mass):
    '''
    This is based on second law of newton 

    Parameters
    ----------
    force : float
        force you put on something.
    mass : float
        mass of your objct.

    Returns
    -------
    acceleration : float
        acceleration of that mass under your force based on second law of newton.

    '''
    
    acceleration=force/mass
    return acceleration








def acceleration_calculator(force,mass):
    '''
    

    Parameters
    ----------
    force : TYPE
        DESCRIPTION.
    mass : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    acceleration=force/mass
    
    print('acceleration is :',acceleration)



#predict_bitcoin()


#import sklearn

#sklearn.




#predicted=predict_bitcoin('11jan')

#vorodi 
#too haminja











def acceleration_calculator(force,mass):
    '''
    

    Parameters
    ----------
    force : TYPE
        DESCRIPTION.
    mass : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    acceleration=force/mass
    
    print('acceleration is :',acceleration)
    
    

acceleration_calculator(30,11)



user_force=float(input('salam forcet ro bede'))
user_mass=float(input('jermet ro bede:'))

acceleration_calculator(user_force, user_mass)


#-----anjam nemidann
#----> xxxx input-->amozeshi


acceleration_calculator(30,10)








def acceleration_calculator():
    '''
    

    Parameters
    ----------
    force : TYPE
        DESCRIPTION.
    mass : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    force=float(input('salam nirogton ro begid:'))
    mass=float(input('salam jermet ro begoo:'))

    acceleration=force/mass
    
    print('acceleration is :',acceleration)
    

acceleration_calculator()


#----------------------------
#***
#esm hay evorodi argument
#yek az tabe estefade mikone bedone in vorodi ha chian
#dakheel tabe bahash estefade mishe


def acc_newton(force,mass):
    acc=force/mass
    return acc



a=40
b=30

acc_newton(a,b)


acc_newton(40,30)



acc_newton(40,30,10)


#TypeError: acc_newton() takes 2 positional arguments but 3 were given


acc_newton(40)

#TypeError: acc_newton() missing 1 required positional argument: 'mass'


acc_newton(force=40,mass=30)
acc_newton(40,30)


#-----------------
#----kole oon baal rasto palk kon

def acc_newton(force,mass):
    acc=force/mass
    return acc

#force, mass, acc , variable ii k dakheel tabe hast
#yek zarfe movaghate k az birone tabe b dakhele tabe biad va amalaiat ro anjam bde
#****


myobject=acc_newton(40,10)



#print(force) #NameError: name 'force' is not defined
#print(mass) #NameError: name 'mass' is not defined
#print(acc) #NameError: name 'acc' is not defined



#****
#tamame variables haee k dakhele function hastan movaghat hastan
#pas biroone tabe nemitonim beheshon ebresim
#sakhte nashode

#local --->

#variables ha




#global --> sarasari
#local 






#asle code
#global --> misaze zarf ro

#local --> nmisaze, biron az tabe shenakhte nmishe




def jam(a,b):
    c=a+b
    print(c)
    return c


d=jam(50,60)

#print(c) #NameError: name 'c' is not defined



c=200

def jam(a,b):
    c=a+b
    print(c)
    return c


d=jam(30,40)



#------agha man 

def jam(a,b):
    d=a+b
    return d




myanswer=jam(50,100)


#print(d) #NameError: name 'd' is not defined



#local -->local avriables 


#---> agha man shaayd yeja


#local --> global



def jam(a,b):
    global d
    d=a+b
    return d



myanswer=jam(50,100)

print(d)



#-----------------------------------------

#f=m*a

#jerm * a --> f


def newton_force(mass,acceleration):
    
    force=mass*acceleration
    
    return force


#10 jermesh , 5  --> 50


myans=newton_force(10,5) #50


myans=newton_force(10)
#TypeError: newton_force() missing 1 required positional argument: 'acceleration'


#aya mitonam yjori tabe benevism


#----> zamino dar nazar begiri --> a --> geranehs = 9.8


#jermi 10 * 9.8 --> 98 newton


#jermamo 

#jerm * 9.8 -->


def gravity_force(mass):
    
    force=mass*9.8
    
    return force


myans2=gravity_force(10)

#myans2=gravity_force(10,5)




#dota tabe
#ye tabe dashtam

#ag taraf jerm mdiad , shetab --> m *a --> force

#ag trf fght mass --> m ---> m * 9.8 --> force




#(input1,inpu2) bayhad gtaman user 2 ta input bde
 
#(input1,input2=...) mitone 2 ta bede , ama ag yekiam dad iradi ndre
#baslek b sorate default input2 --> 



def general_force(mass,acceleration=9.8):
    
    force=mass*acceleration
    
    return force



general_force(10,20)

general_force(10)





#----> hamishe nbiaz niost koli tabe besaziiii
#ba if o ....

#to dele tabe


#tabe dar asl yek code ke gozahsatmsh toye yek capsool

#if , for , ......

def jam(a,b):
    c=a+b
    return c


def tafrigh(a,b):
    c=a+b
    return c 

def zarb(a,b):
    c=a*b
    return c

#jam(10,20)
#tafrigh(10,20)




def general_calc(a,b,amalgar):
    if amalgar=='jam':
        c=a+b
        return c
    elif amalgar=='tafrigh':
        c=a-b
        return c
    elif amalgar=='zarb':
        c=a*b
        return c
    
    
#for ,...



#vorodi hato bgi ya chant achant abgiri list



def myfunction(a,b,c,d,e,f,g,h):
    pass
    

def myfunction(mylist):
    
    pass


myfunction([10,20,30,40,50,60])

#mylist= [10,20,30,40,50,60]






#agha adad 1 , dovom , amalagreto brize too y listo bde b tabe


#[10,20,'jam']



def calcualtor_based_on_list(list1):
    
    if list1[2]=='jam':
        c=list1[0]+list1[1]
        return c
    
    #.....



mylist=[10,20,'jam']


calcualtor_based_on_list(mylist)
    




#count


reshte='salam'


reshte.count('a')


#vorodi --reshte.character 
#khorji -->adad


'''


reshte, character ---> bOX ---> ADAD

'''




def my_count(reshte,character):
    
    count=0
    
    for i in reshte:
        if i==character:
            count=count+1
            
    return count




my_count('salam','a') #2



#miangin??

#10,20,30,40,50,60


a=[10,20,30,40,50]

sum(a)

def miangin(list1):
    
    #for i in list1:
        
   mysum= sum(list1)
   mylen=len(list1)
   
   mymiangin=mysum/mylen

   return mymiangin
            
    

    
miangin([10,20,30,40,50,60,70,80,90,100]) #55.0



pow(4,2) # 16




def my_pow(numb1,numb2):
    result=numb1**numb2
    return result


my_pow(4,2)



#------------------------------------

'''

Project 1

A1 --> 

A1_NAME_LASTNAME 

ai.2024@pilehvar@gmail.com

--->20%




#--se ghesmat



yedoone file --> A1_ALI_PILEHVAR.py
3 ta section





section 1--->

# hadeaghal 5 ta adade moheme reshtato benevis

gravity_acceleration=9.8



section2 -->
2 ta tabdil (reverse) ---> 4 

milimeter --> meter


inch --> cm 

esm daghighan 

Millimeter_to_Meter()
Meter_to_Millimeter()

Inch_to_Centimeter()
Centimeter_to_Inch()

#yek vorodi yek khoroji 




Section 3***


2 ta function dar hiteye khodetan 

esmashoon , consth
 

yek esme --> Bozorg ...
Newton



#dota 
#_ avale har harf bozorg
Newton_Law_Of_(mass,acceleration)  awli

newtonlaw(m,a) bad



2 ta tabe tooye resdhtato benevisid 



ide ? --> **payam email 

ide begiri ,ide dari

listi telegram --.ersal mikonam (koli tabe dakhelesh hast)

** azoon tabe ha estefade nakonii *** tabe haye tekrari hasan




 


vorodi khorji

***

riazi , hooshe masnooe -->numerical solution








#-----------

A1_name_Lname

ai.2024.pilehvar@gmail.com

deadline : jalaseye 9 --> 12 shab shanbe 25 esfand mah 


yek file.py --> 3 sectioin

section 1----> 5 ta adade sabet
sectione 2 --> 4 ta tabe --:> 2 ta tabeye converter (reverse)
sectione 3 --> 2 ta tabe dar hiteye khdoeton (ghablesh ba list check shavad)

#-------


jalaseye advanced ( ekhtiari) --> charshanbe 22 esfand mah hast 

jalaseye badi -->jalaseye 9 --> yekshanbe 26 esfand mah





'''





def Millimeter_to_Meter():
    '''
    parameter
    Millimeter ->
    
    
    
    
    '''
    
    

# x**2 + x +3 =0

#root??

#vb2- 4 ac --> delta 
#ag delta>
#<
#=0



#a*x **2 + b*x + c =0


    
def root2(a,b,c):
    
    delta=b**2-4*a*c
    
    
    if delta>0:
        return None
        
        
    elif delta==0:
        pass
        #return r
        
        
    elif delta<0:
        pass
        #return
        
        
    
    











