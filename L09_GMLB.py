"""
In The Name of GOD
Created on Sun Mar 16 18:25:13 2025

@author: Ali Pilhvar Meibody
L9-----------

"""


'''

-------REVIEW-----

PSUDOCODE neveshtan nistim

hamashon ro dakhele yek capsool gharar  midim 
vorodi ---> BOX ---> KHOROJI



dalile tabe :
    
    1- KHEYLI MONAZAM TAR CODE MINVISIM
    2-rahat tar va asan tar ghabele khandan hast 
    3-mitonim hardafe khastim chanbar sedash bznimharja
    4-baghie mitonan estefad ekonan
    5-debugging
    
    
    
def name(input1,input2,input3,....):
    dastooorat
    
    return output


zarf=name(a,b,c,...)


def name(input1,input2,input3,....):
    dastooorat
    
    return output1 , output2



zarf=name(a,b,c) XXXXX

zarf1 , zarf2= name(a,b,c) 


#------dakheley yek tabe aksare variable ha zarf ha movagahti hastanm


yani LOCAL

yani birone tab eseda zsde nemishe

#---------------

class




'''


def mufunc(a,b,c):
    d=a+b+c
    return d

zarf=mufunc(10,20,30)




#class , name , vorodi nmidi
class myclass:
    
    balance=1000
    
    
o1=myclass()
#o1 yek dot bznm dastresi b koli chiz drm
#Koli khorojhi

o1.balance # 1000


#class --> variable too dele khdoehs dre va koli tabe


#class , name , vorodi nmidi
class myclass:
    
    balance=1000
    
    def welcome(self):
        print('salam')


zarf=myclass()

zarf.balance

zarf.welcome() #salam


#jalaseye gozahste --> ADVANCE --> drmoredesh sohbat shdoe


'''
function


class --> daghighan mese functione , madare

class --> koli avriable , function

dastresi b variable , function ha kafie dot bzni



'''

#NameError: name 'calculator' is not defined


calculator(10,20,'jam')



#hadaf ---> tabe function , class biarish inja

#Biarish , BNNRIZIM , bendazsesh --> herfe ee nis


#importesh koni ****


#import krdn

'''

file .py ---> in script mitoone harjaee save bashe
mitone desktop. folder, ....


ama vaghty dri run mikoni , momkene runi k dre msihe yejaye dg bashe



jaeee k scriptet has
ba jaee k run mishe frgh dre




jaee k dare barname run mishe ---> az kooja befahmam
oon baal samte rasto negah kpon

/desktop/....///////

/users/......



'''

#yek calculator() estefade kojnm
#@khob aval bayad scripti test22.py
#aval bayad b test22.py dastressi peyda konm
#bad bgm boro toosh, tabeye ccalculotoro bekesh biron (import kon)


#agha biar test22.py




#vahleye aval ine ke 
#az tarigeh oon bala samte rast
#beri va peyd akoni


#---step1----------
#oonja ek filet hast


#----step2---------
#import esmefile

import test22




#---step3----
#boro too test22 hala k ovordish
#tooosh tabeye flano bede

#calculator(aa,b,c)

#pytho bfhme , csalculator() tooye in scripte felit nis
#balke dari az y scripte dg mikeshsh biron

test22.calculator(10,20,'jam')

#30

test22.calculator(10,20,'tafrigh')
#-10

test22.calculator(10,20,'tafrigh')
#.........



'''

baraye dastressi b tabe ha ya class ha harchizi 
kadfi hast in 3 step ro brim



------STEP1------
oon bala samte rast , jaee k dare filemon run mishe
ro bbrim jaee k scripte morede nazar vojod darad



----STEP2-----
benevisim
import esme oon script



-------STEP3-----
benevisim esme oon scripto bad dot bznim
az har tabee ee k mikhaym estefade konim

easyyyy




'''


#ravesh haye dg eye import krdn (step2)

import test22


#test_for_ali_pilehjvar_meibody_class_2025


#test_for_ali_pilehjvar_meibody_class_2025.



#mokhafaf krdn

#import esme-vaghei as mokhafaf

import test22 as t

#test22.calculator(10,20,'jam')


t.calculator(10,20,'jam')


#---------------
#tabe ro bekeshi biron fght k khodesho seda bzni
#az test22 fght tabeye calculator ro biar biron
#rahat sedash bzn


from test22 import calculator



calculator(10,20,'jam')


#mokhafaf koni


from test22 import calculator as cl

cl(10,20,'jam')



#----harchi tabe hasto biar vasm
from test22 import *

#esm haye tabe ro bzni




'''
review-----------


step1----> az tarifghe file boro jaee k scriptet hast

step2--->importesh kon (**ravesh haye motefavet)


step3-->call kon estefade kon (ba ch esmi? ba hamon raveshi k import krdi)


'''
#------------1-----------------
#import esme vaghei 
#script.function()

import test22
test22.caculator()

#------------2-----------------
#import esme vaghei as mokhafaf
#mokhafaf.function()

import test22 as t2
t2.calculator()


#----------3-------------
#from script import kon fght in tabe ro
#esme tabe ro bnvis function()

from test22 import calculator
calculator()

#-------3 mokhfafaf----------
from test22 import calculator as cll
cll()


#-----4----------
from test22 import *

calculator()
#va tabe haye digar



#------------------------------------

#from ali import calculator

#from mohesn import calculator

#from amir import calculator


#calculator

#import ali
#ali.clculator()

#--------------------------------

import test22
#90 % error mide mige man peyda nmikonm in scripteto nist agha

#--------




#---------------------------

#aya baghie company ha ham mitonan bian
#koli tabe benevisn yeja zakhrie konan va bad
#man inja sedashon bznm ieasy va az tabe ha estefade konm?


#chra k na bale
#bale k mishee




#import newtech

#newtech.//
#newtech,()


#-----PYTHON ----> ketabkhane hast


#ketabkhane koli fucntion, class, variable ,.... too dleeshe

#100000 khat code run koni

#esme ketabkhone.function()




#----->ketabkhane ha khosh omdid



'''
baed hast k shoma niaz dashte bashid az tabe haye gozashteye
scripte ghadimie khod estefade konid mesle bala

aksaran shoam mikhahid az tabe haye afrade digar estefadxe konid

pas ravesh 

---step1-----
rooye desktopety k zakhrie ndri
***



----step2-----
import esme__ketabkhone


----step3----
esme_ketabkhone.function()






13000000 kjetabkhone darim too jahan
yeja downloiadesh koni 

sakht nis?download koni
biarish desktop
bad biarish inja desktop
donbale esmeesh bashi va va vaa???




pip ish kon ** ---> downloaesh kon XXX



default -->spyder 
yeseri ketabkhone ha besoorate pish farz rooye pythoneton has



'''

#besoorsate pishfarz bazia inaro drn

#math

import math

#import math

import random


import time



#---------------------------------------------
import math







#gorohe azmayehsi , koli tabe ye riazi k naiz mishe ro
#Neshastan tabasho nvshtn


#import test22
#test22.radical(40)


#karhaye riazito anjam mide


a=4**2




#radical 4???
#alamatie chizie?


#tabe benvism


'''



vorodi ----> radicsal -->khoroji


'''

import math 

#1=!*** yekbar import va runesh koni dg kafieeee
#aksaran 

zarf=math.sqrt(4)

zarf=math.sqrt(16)

zarf=math.sqrt(3)

 
math.sin(30) #-0.9880316240928618

math.tan()

math.e


'''

ketabkhoen ha import



. --> dastrssii b dakhelehs dri

V --> variables



F , c -- function class ()
'''

math.e # 2.718281828459045

math.pi #3.141592653589793


#taqbe

math.sqrt(10)

math.sin()
math.cos()
math.tan()
math.acos()
math.asin()

math.log() #ln 

math.log10()

math.log1()



'''


def tabe(vorodi,vorodi2,vorodi2):
    
    return




'''



#log1()

#math.tabe()


#import time
#import datetime


import random 
#




'''


ketabkhone haee k dar hiteye shoma hasto
mohem trin tavabesh ro bdoni jholoshosh chikar mikone







Numpy ---> mohasebat


scipy , sympy ---> hale adadi hastan 

Matplotlib ---> RASM
Pandas--->kar ba dade ha hast



sklearn
scikit-learn

-----?hoshe masnoee hast

'''

#import numpy

#numpy is not defined

#numpy nist --> download , pip 


'''

WINDOWS


anaconda --->mohiteto entekhab mikoni

cmd.exe pROMPT install , launch

yek safe siah hast 



codi onja benevisi enter bzni ejra mikone

downlao dkon numpppy ro 


numpy ro baray eooin mohit download mikone


import numpy #Numpy ro daram




google 
pip esme ketabkhone



pip numpy


pip install numpy

in dasatoore downlkaode numpy hast

pip install numpy

aval boro google pip numpy


sabz shod-->downlaod shode



import numpy Yes




#------windows--------
FINALLL

Open anaconda
select your environment ( for exmplae EBM)
find CMD.exe Prompt
Install thta
launch that
(you can see black window)

go to google search pip (name of lib)
find pypi website
copy the command (pip install lib_name)

paste in the black window and enter
finish 


go to spyder ( on your envgironment)


#-------MAC-------
command + space --> search bar

terminal

conda activate esme_environemnt

(base) --> (EBM)


pip install numpy

tamam


'''

#t ajalasseye badiu
#hameye azizan


import numpy

'''
import numpy

bedone error

'''





'''
Ai.2024.pilehvar@gmail.com
'''


'''
Numpy
scipy
sympy 
pandas
matplotlib.pyplot
scikit-learn

'''


#-----------------------------------------------------
#---------------PART 2 DORE SHORO MISHE--------------


a=20

#yekjaee too delesh

#yek jaye bozorg , python object zakhire mikone

#tooye memoryt ---> khoen ha hastan k toosh mitoni adad zakhir ekoni


#esme zarf, 
#type e zarf
#size e zarf
#adade tooye zarfo
'''

[] [] [] []


'''

#hajm bare -->hajme kh balaee eshghal mikone




#C , C++ --> COMPUTATIONAL

a=20

'''

int a=20


[20]

double a=20.02

def add(a,b):
    c=a+b
    return c



double def add(int a , int b):{
    double c ;
    c= a+b ;
    return c;
    }

#kh tool mikeshe ba beneviusi ama vaght  ejra mishe kh fastre

[] [] [ ] finish




[] [] [] []
a--> [] [] [] []
b--->[] [] [] []
c--> [] [] [] []


Mohasebe

list--->

[] [] [] []


python
[]  [] [] []

[] [ ] [] []



c++ 100 elemnt --> 100 ta khoneye memoryiio migire

python --> list4 , 4 --> 404 khoenye memory ro eshgal mikone






advantages: zabane asan , koli ketabkhone, 
user friendly, englisi 


----> MOHASEBE--------------

1---->python is not effficient for computation
python baraye mohasebat be sarfe nist

cython , .......

2--> 
table --> 

. . . . . 
. . . . .
. . . . . 


10 20 30 40 50
60 70 80 90 100
11 131 14 1  5


list--> [10,20,30,40,50,60,70,80] radis
1D , bod haye balaytar bkhay
2bodi-->ham radif ham soton






--->Company anjoman --> Num py 

Numpy --> esme ketabkhonashone

oon zir C , C++ estefade krdn 
va goftan ma yechizaee miarim k hajme memory kamtar
va kh kh khafan tar bshe 



'''

#--------REVIEW--------------
#------LIST HA---------

a=[10,20,30,40]

a=[10.5, 4 , 1j , 'ali', True]


#name , type , size , value


#click kjon oon bala rast rooye a

#index, type , size , value

a[1]

a[2]

a[3:5]

a[3:5:2]

#change
a[2]=2000

#methods

a.insert(3,150) 
a.append(200) #tahesh
a.remove(100)
a.pop(2)
a.clear()
# del a 


#*******
#1-----> konde kh kh kond hast baraye mohasebaat
#2-->fght yek radife (1D), radifo soton bashe 




#----->NUMPY GOF SALAM MAN INJAM


#1----> HODODAN 40 X FASTER ( core on C , C++)

#2---> az 2d,3d,4df,5d,... bod hay ebala ham mitoni adad brizi , matrix, table

#3-->koli tabe ye khafan too deleshe k koli kar hay emohasebati anjam mide


#niaz hast k man numpy ro aval download (Pip)
#import
#estefade konm


'''
boro bala bebin bar asase window , mac

pip install numpy ---> cmd.EXE (terminal) safe siah
download k shod

importesh kon

'''


import numpy 


#agha kole numpy ro (script) import kon

#ag bkhay b tabe ha , class harchi k dakhele
#Numpy hast dastressi peyda koni

#numpy. felan tabe ro mikham

#Numpy.add()
#numpy.felan()


#class dashte bashe


#class --> tabe daran

#felan script boro toosh, felan class boro toosh , felan tabe
#numpy.felan_class.felan_tabe()


#mohem tarin tabe --> array()


#list()

#set()
#dict#
#tuple


#array( ) az hameye balee ha ham mohemtre
#ham khafdan tare
#ham karbordi tare


#array ro khdo epython ndr


list((10,20,30,40)) #[10, 20, 30, 40]
set((10,20,30,40))
tuple(())
#khdoe python ino ndre
array()


#ki dare??

#numpy mige man yechizi drm bname array
#mese liste


#bayad impro tkoni numpy ro yehbar
import numpy

#bad beri toosh va array ro bekeshi biron azash


numpy.array()



#----list ,array


#10 , 20 ,30 ,40

#a=[10,20,30,40]
a=list((10,20,30,40))

b=numpy.array((10,20,30,40))


a[0] #10
b[0] #10


a[0:2] # [10, 20]
b[0:2] #array([10, 20])


a[0]=200

print(a) #[200, 20, 30, 40]


b[0]=200
print(b) #[200  20  30  40]



a.append()
a.insert()
a.remove()
a.pop()
a.clear()

import math
new_list=[]
for i in a:
    b=math.sqrt(i)
    new_list.append(b)
    

#-----Inghadri numpy tabe dare ke vaghean nemidonam chanta
#

b.max()
b.min()
b.sum()

b.argmin() # 1
b.argmax()

#--->jalaseye badi say drim
#Mohem tarin tavabe ro bhtron yad bdim ****
#bad inke beri documentation






























































