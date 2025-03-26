
"""
In The Name of GOD

Happy NowRuz


Created on Wed Mar 26 18:04:25 2025

@author: Ali Pilehvar Meibody

-----L9--------

-----ADVANCED---------

-------L10-------

"""

'''
Short Review



Human ---- Python --- machine


1----Reserved words
1.1.Python built in functions (print,input,len,type,....)
1.2.Keywords(if , if else , if elif else, for , while, and , or , as , ...)


2----Unreserved words
--> Zarf variable (moteghayer)
2.1. Numbers ( int, float, complex) ** * + - ,...
comaprison --> == != > < >= <= --> True False 
2.2. Boolean ( True, False)
2.3.Str --> string --> qoutatin word, sentence,... -->
str functions --> variable.upper() .lower() .replace()
.count('a')  .find('a')  .isupper()

2.4. Iterables -> multiple variables
2.4.1. List --> ordered, changable, allow duplicated
a=[10,20,30,ali,True,1.5]
a[] list functions --> .insert(2,'ali') .append()
.pop(2)  .remove('ali')  .clear()  []

2.4.2. Tuple
[] --> ()   unchanble --> list --> 
tuple.functions

2.4.3. set --> not ordered, unchangable , doesnt allow duplicated
{}  --> tekrari haro hazf konid

2.4.4. dict dictionary --> keys , values
index0  value
key
a={'year': 2004 , 'model': 'benz'}
a[0] XX
a['year']

psudocode --> az bala b paen code ro mineveshtim

Box (code ro brizi)

#-----Functions---------

vorodi (inputs) ---> BOX --> Khoroji


1---> Assignment, definition

def name(input1,input2,input3,....):
    body --> (if,else, for , while ,....)
    
    return output1, output2,....


'''


#Calculaotrs-------

'''

Vorodi ha chie?
khoroji chie?


adad 1 , adad2 , amalgar

khorji -> javab



input1,input2,inpou3 --> BOX --> output1

'''

def Calculator(numb1,numb2,operator):
    '''
    This function is used for calculation
    inputs:
        numb1 --> Float
        numb2 --> Float
        Operator --> String (Jam, Tafrigh, Zarb, Taghsim)
        
    Output :
        Answer --> Float
        
    
    '''
    
    if operator =='jam':    
        answer=numb1 + numb2
        return answer
    
    elif operator =='tafrigh':
        answer=numb1-numb2
        return answer
    
    elif operator =='zarb':
        answer=numb1*numb2
        return answer
    elif operator=='taghsim':
        if numb2==0:
            print('Zero division error')
            #return None
            #return 'Infinity'
        else:
            answer=numb1/numb2
            return answer
    
    
    
    
    
    
#print namayersh bde
#khoroji bht mide
#to mitoni yejae zakhrei

a=Calculator(10, 20, 'jam')


#tabe list , 


#default


def force(a,b):
    c=a*b
    return c



def force(a,b=10):
    c=a*b
    return c



#calculator fght b soorat elist

def calculator(mylist):
    '''
    input:
        list --> [numb1,numb2,operator]
        
    outptu:
        answer-->float
    '''
    if len(mylist)!=3:
        print('bayad vorodie shoa listeton 3 ta bashe')
        return None
    
    numb1=mylist[0]
    numb2=mylist[1]
    operator=mylist[2]
    
    if operator =='jam':    
        answer=numb1 + numb2
        return answer
    
    elif operator =='tafrigh':
        answer=numb1-numb2
        return answer
    
    elif operator =='zarb':
        answer=numb1*numb2
        return answer
    elif operator=='taghsim':
        if numb2==0:
            print('Zero division error')
            #return None
            #return 'Infinity'
        else:
            answer=numb1/numb2
            return answer
    




#bejay einke 3 ta vorodi bgrii yedone vroodi list bgiri

a=[10,20,'jam']

b=calculator(a)


#------------------------------------------
#----------FILE HANDLING------------------
#niaz darid yek file ro 

#vorodi ha

#khdoet assignment koni
a=10
sentence='Hello welcome to the progrramming world'
c=[10,20,30,40,50,60]

#2 --> Internet


#3--> File ro inaj baz konish 

#---file format hayte khase khodehon ro drn

'''

Python default --> .txt

python built in function --> open() (shabihe print())



niaz dare be ketabkhoneye khodesh:
doc , docx


CSV (xlsx) ---> pandas

a=open()

a=pandas.read_csv('user/desktop/experimental2.csv')



PDF --->pypdf

Image (png, jpg, jpeg) -- PIL , opencv


animation (gif)
movie( mp4)
audio (mp3)


open()




'''


def openn(path,mode):
    pass
    #mire path ro peyda mikone --> masire file ro
    
    #ag masir ro peyda nkrd
    #return None --> raise Error
    
    #else:
    #openesh mikone
    
    #return mide
    #brizish too zarf
    
#class --> Open
#too delesh --> read() write()  , .....

'''
B BESMELA----------

BARNAMEYE .PY shoma dare yek jae az computerret ejra mishe

mitoni bebinish samte rast baalro negah kon

/users/,.....


mitoni dasti taghiresh bedi
mironi az tarighe Files winodw

velesh koni

aghga man injas
Users/apm


'''

#default midone ke rooye USERS/apm/

#az inaj b bado bayad behesh path

#new.txt
'''

r ---> read bekhonamesh
w ---> read + write
a --> append konm b tahesh chjizi
.....



'''
#/Users/apm/Desktop

#file ro open mikone khrooji mide


#tooye path property --> copy paste

#**yadet nare tahe path esme file ro ba fomratehs bzri
#new.txt

f=open('/Users/apm/Desktop/new.txt',mode='r')

print(f)
'''
<_io.TextIOWrapper name='/Users/apm/Desktop/new.txt' mode='r' encoding='UTF-8'>
'''

#tabe haye dkaheli

#readline()
#readlines()
#write()
#close()

#yek line ro mikhone khoroji mide 

mytext=f.readline()

print(mytext) #salam



newtext=f.readlines()
print(newtext)


f.close()



#----write

f=open('/Users/apm/Desktop/new.txt',mode='w')


f.write('new word')

f.close()


#w --> kolesjo p[ak mikone minevise]

#-----append
f=open('/Users/apm/Desktop/new.txt',mode='a')
f.write('new new new new')
f.close()


#--------------------------
#---------------------------
#---------------------------------
#tabe haye baghie estefade mikonim

'''
Libs --> Ketabkhone 

khode ma miotnim besazim
compnay
free , scientific
Tech company


too deleshon koli scripts
too har script , class, def

**class ---> koli def tooshe
L_Advanced

print()

class2.print()



python---> default

math
random
statistic



download--> Pip kon

search google 
peydash mikoni

pip install numpy
pip install pandas
pip install matplotlib.pyplot
pip install scikit-learn
pip ......


CMD. exe (file telegram)


#***farz mikonam shoma pip ish krdid (darid)

#-------------------------------
math 
datetime
numpy ---> Mohasebat hast
scipy , sympy --> Mohasebate pishrafte tar
Matplotlib --> Rasme nemoodar
Pandas --> Kar ba dade (data preprocessing, cleaning)

Sklearn ---> (Machine learning)



Introduction------
Tensorflow , Keras
*pytorch
opencv --> computer vision
----> Deeplearning


'''
#yekbar run

#impoprtaro mizrn avale code ha
import numpy
#agar nevesht
#numpy is not defined
#numpuy attributes arer not found
#package is not found ,...

#installesh nakardi  ----> pdf telegram , jalseye ghabl , telegram email 


#numpy miad dakhele IDE 


#--------------
#riaziat
#kole math ro impor tkon

import math 

#math.felan function ro mikham

def calcualtor():
    pass

calculator()


#alipm

#import alipm

#alipm.calculator()

import math 


#sqrt

def sqrt(numb):
    #......
    
    pass
    #return radical numb

#sqrt(36)


import math 
#vorodi dddi
#khoroji

a=math.sqrt(36)

p=math.pi


a=math.ceil(4.2) #5


#hameye ina tabe ee hast k vorodi dare
#va khoroji

#Khorojish ro bayad zakhire koni

#maa man baraye yadgiri hey zkahrienmikonm

math.e
#()

math.log()

#ln --> log

math.log10()

math.log2()

#bar paye 4 
math.log(50,4) #2.821928094887362
#log | 50 4


'''

#Math Methods
Method	Description
math.acos()	Returns the arc cosine of a number
math.acosh()	Returns the inverse hyperbolic cosine of a number
math.asin()	Returns the arc sine of a number
math.asinh()	Returns the inverse hyperbolic sine of a number
math.atan()	Returns the arc tangent of a number in radians
math.atan2()	Returns the arc tangent of y/x in radians
math.atanh()	Returns the inverse hyperbolic tangent of a number
math.ceil()	Rounds a number up to the nearest integer
math.comb()	Returns the number of ways to choose k items from n items without repetition and order
math.copysign()	Returns a float consisting of the value of the first parameter and the sign of the second parameter
math.cos()	Returns the cosine of a number
math.cosh()	Returns the hyperbolic cosine of a number
math.degrees()	Converts an angle from radians to degrees
math.dist()	Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf()	Returns the error function of a number
math.erfc()	Returns the complementary error function of a number
math.exp()	Returns E raised to the power of x
math.expm1()	Returns Ex - 1
math.fabs()	Returns the absolute value of a number
math.factorial()	Returns the factorial of a number
math.floor()	Rounds a number down to the nearest integer
math.fmod()	Returns the remainder of x/y
math.frexp()	Returns the mantissa and the exponent, of a specified number
math.fsum()	Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
math.gamma()	Returns the gamma function at x
math.gcd()	Returns the greatest common divisor of two integers
math.hypot()	Returns the Euclidean norm
math.isclose()	Checks whether two values are close to each other, or not
math.isfinite()	Checks whether a number is finite or not
math.isinf()	Checks whether a number is infinite or not
math.isnan()	Checks whether a value is NaN (not a number) or not
math.isqrt()	Rounds a square root number downwards to the nearest integer
math.ldexp()	Returns the inverse of math.frexp() which is x * (2**i) of the given numbers x and i
math.lgamma()	Returns the log gamma value of x
math.log()	Returns the natural logarithm of a number, or the logarithm of number to base
math.log10()	Returns the base-10 logarithm of x
math.log1p()	Returns the natural logarithm of 1+x
math.log2()	Returns the base-2 logarithm of x
math.perm()	Returns the number of ways to choose k items from n items with order and without repetition
math.pow()	Returns the value of x to the power of y
math.prod()	Returns the product of all the elements in an iterable
math.radians()	Converts a degree value into radians
math.remainder()	Returns the closest value that can make numerator completely divisible by the denominator
math.sin()	Returns the sine of a number
math.sinh()	Returns the hyperbolic sine of a number
math.sqrt()	Returns the square root of a number
math.tan()	Returns the tangent of a number
math.tanh()	Returns the hyperbolic tangent of a number
math.trunc()	Returns the truncated integer parts of a number


#Math Constants
Constant	Description
math.e	Returns Euler's number (2.7182...)
math.inf	Returns a floating-point positive infinity
math.nan	Returns a floating-point NaN (Not a Number) value
math.pi	Returns PI (3.1415...)
math.tau	Returns tau (6.2831...)



math.acos() کسینوس قوس یک عدد را برمی‌گرداند
math.acosh() کسینوس هذلولی معکوس یک عدد را برمی‌گرداند
math.asin() سینوس قوس یک عدد را برمی گرداند
math.asinh() سینوس هذلولی معکوس یک عدد را برمی گرداند
math.atan() مماس قوس یک عدد را بر حسب رادیان برمی گرداند
math.atan2() مماس قوس y/x را بر حسب رادیان برمی گرداند
math.atanh() مماس هذلولی معکوس یک عدد را برمی گرداند
math.ceil() یک عدد را تا نزدیکترین عدد صحیح گرد می کند
math.comb() تعداد روش‌های انتخاب k مورد از n مورد را بدون تکرار و ترتیب برمی‌گرداند.
math.copysign() یک float متشکل از مقدار پارامتر اول و علامت پارامتر دوم را برمی گرداند.
math.cos() کسینوس یک عدد را برمی‌گرداند
math.cosh() کسینوس هذلولی یک عدد را برمی‌گرداند
math.degrees() یک زاویه را از رادیان به درجه تبدیل می کند
math.dist() فاصله اقلیدسی بین دو نقطه (p و q) را برمی‌گرداند، جایی که p و q مختصات آن نقطه هستند.
math.erf() تابع خطای یک عدد را برمی گرداند
math.erfc() تابع خطای مکمل یک عدد را برمی گرداند
math.exp() E را به توان x برمی گرداند
math.expm1() قبلی - 1 را برمی گرداند
math.fabs() قدر مطلق یک عدد را برمی گرداند
math.factorial() فاکتوریل یک عدد را برمی گرداند
math.floor() یک عدد را تا نزدیکترین عدد صحیح به پایین گرد می کند
math.fmod() باقیمانده x/y را برمی گرداند
math.frexp() مانتیس و توان یک عدد مشخص را برمی‌گرداند
math.fsum() مجموع تمام آیتم ها را در هر تکرار شونده برمی گرداند (تاپل ها، آرایه ها، لیست ها و غیره)
math.gamma() تابع گاما را در x برمی گرداند
math.gcd() بزرگترین مقسوم علیه مشترک دو عدد صحیح را برمی گرداند
math.hypot() هنجار اقلیدسی را برمی گرداند
math.isclose() بررسی می کند که آیا دو مقدار به یکدیگر نزدیک هستند یا نه
math.isfinite() محدود بودن یا نبودن یک عدد را بررسی می کند
math.isinf() بررسی می کند که آیا یک عدد بینهایت است یا خیر
math.isnan() بررسی می کند که آیا یک مقدار NaN (عدد نیست) است یا خیر
math.isqrt() یک عدد جذر را تا نزدیکترین عدد صحیح به سمت پایین گرد می کند
math.ldexp() معکوس math.frexp() را برمی‌گرداند که x * (2**i) از اعداد x و i است.
math.lgamma() مقدار لاگ گامای x را برمی گرداند
math.log() لگاریتم طبیعی یک عدد یا لگاریتم عدد را به پایه برمی گرداند.
math.log10() لگاریتم پایه 10 x را برمی گرداند
math.log1p() لگاریتم طبیعی 1+x را برمی گرداند
math.log2() لگاریتم پایه-2 x را برمی گرداند
math.perm() تعداد روش های انتخاب k مورد از n مورد را با ترتیب و بدون تکرار برمی گرداند.
math.pow() مقدار x را به توان y برمی گرداند
math.prod() حاصل ضرب تمام عناصر یک تکرار شونده را برمی گرداند
math.radians() یک مقدار درجه را به رادیان تبدیل می کند
math.remainder() نزدیکترین مقداری را برمی گرداند که می تواند صورت را کاملاً بر مخرج بخش کند.
math.sin() سینوس یک عدد را برمی گرداند
math.sinh() سینوس هذلولی یک عدد را برمی گرداند
math.sqrt() جذر یک عدد را برمی گرداند
math.tan() مماس یک عدد را برمی گرداند
math.tanh() مماس هذلولی یک عدد را برمی گرداند
math.trunc() قسمت های صحیح کوتاه شده یک عدد را برمی گرداند


#ثابتهای ریاضی
توصیف ثابت
math.e شماره اویلر را برمی‌گرداند (2.7182...)
math.inf یک بی نهایت مثبت ممیز شناور را برمی گرداند
math.nan مقدار ممیز شناور NaN (نه عدد) را برمی‌گرداند
math.pi PI را برمی‌گرداند (3.1415...)
math.tau tau را برمی‌گرداند (6.2831...)

'''


def calcualtor(numb1,numb2,operator):
    if operator=='taghsim':
        if numb2==0: 
            answer=math.inf
            return answer 
        else:
            answer=numb1/numb2
            return answer


#-----------------------------------------------
#ketyabkhone haye default --> python
import datetime
'''
-------1---------
import lib


lib.function()




-------2---------
import lib as mokhafaf

mokhafaf.function()


-------3---------
from lib import function
function()



-----4--------
#recommend nemishe XXXXX
from lib import *

function()
funcitn

'''


import math

math.sqrt(36) # 6.0


import math as m
m.sqrt(36)


from math import sqrt
sqrt(36)


from math import sqrt , sin , cos , tan


sqrt(35)

cos(10)
tan()

#pi




import math
math.pi



#-------Datewtime--------
#time
#datetime

from datetime import datetime

#datetime --> datetime()

a=datetime.now()
print(a)
#2025-03-26 18:52:32.493723

#str

print(type(a))
#<class 'datetime.datetime'>
#time --> str , int ,float


a.year #2025

a.second

a.month

a.hour




#type time --> Str
#str ---> time

a.strftime('%h') #'Mar'

#datetime madule python --> search in google
 

#https://www.w3schools.com/python/python_datetime.asp


#---------------------------------------
#-----------------------------------
'''

NUMPY

Anaconda --> Environment entkehab mikonid

CMD. exe  install , launch --> black window

#search google pip numpy

#safe --> pip install numpy --> copy paste

#blakc iwndsow paste
pip install numpy

#enter

#... ---> koli neveshte --> install


#badesh hatman bayad briu tooye spyder hamon environmentet

#oonja numpy ro mishnase jaye dg nmishynase

#injori importesh

import numpy


**yek bar bishtar niaz nist k import konid
import numpy --> runesh 


'''
import numpy



#ma mikhastim chanta adad ro zakhri ekonim

a=list((10,20,30))

a=[10,20,30]


#---> python

a=10
#name, type , size, value --> har 4 taro mire too memory zakhire mikone



'''
C , C ++

int a=10;


10 --_> ye goshe e zkhre mikoen --> 1 done chiz

'''



#------
'''
a=[10,20,30,40]

name , type, size ---> 
adad --> type , size, value
adad2---> type , size , value
adad3
adad4--->

12+3 --->15 ta jaro tooye memory ehsghal mikone


c++ 

list[int] a=[10,20,30,40]

4 ta jaro migire



100 ta adad dari


c , c++ ---> 100 ta memory

python --> 320 t aja memory

konde --> fast nist


#--------1------------
1----> yek chizi kash bood k sari bood

numpy mige man yechizi daram bejaye list bia az man estefade kon
60X apprimately --> fast tare az list



#-------2------------
list--> 10,20,30,40,


radifo sotoon --> 2 bodu

10 20 30 40 50 60
70 80 90 10 20 30
11 12 13 14 15 16

3 ta radif , 6 ta soton

Bod hjaye bishtari dashte basham chi?
numpy mige man yechi daram
ham sari tar az liste (60X)
ham behet ejaze mdie chan bod adad zakhire koni



Idea Numpy ---> Ideye aslie man ine tamam shdoo raft




'''

#------REVIEW LIST------

a=list((10,20,30,40))
#a=[10,20,30,40]

print(len(a)) #4
print(type(a)) #<class 'list'>

a[2]


a[2]=100
print(a)
#[10, 20, 100, 40]


a[1:4] #[20, 100, 40]

a.append(400)

#a.insert(2,200)
#a.pop(2)
#a.pip(20)
#a.clear()
#del a



#-----NUMPY mese listy daram
import numpy

a=list((10,20,30,40))


#yek class --> array

b=numpy.array([10,20,30,40])


print(type(a)) #<class 'list'>
print(type(b)) #<class 'numpy.ndarray'>


print(len(a)) #4
print(len(b)) #4


#indexe 2 --> 10 , 20 --> 30 r mikhay
a[2] #30

b[2] #30


a[2]=400
print(a) #[10, 20, 400, 40]

b[2]=400
print(b) #[ 10  20 400  40]


#_-------sri tar, bod hay ebalatar hgam dashte bashi
import numpy

#dota aprantez bzni

a1=numpy.array((10,20,30,40))
a2=numpy.array([10,20,30,40]) #recommend

mylist=[10,20,30,40]
a3=numpy.array(mylist)




a2=numpy.array([10,20,30,40]) #recommend
print(a2) #[10 20 30 40]
a2[2]



#-----PROPERTIES--------
a2.size #4 element
a2.nbytes #32

a2.ndim #1
a2.shape #(4,)


#----BOD?




#n umpy.array( 0 , ......)



#D--->DImention
#-------0D---------

a=10

a=numpy.array(10)

a.ndim #0
a.size #1

a.shape #()


print(type(a))
#<class 'numpy.ndarray'>




#--------1 D--------------
#--->hamon liste khodemone

a=numpy.array([10,20,30,40])
a.size #4
a.ndim #1 1 raid adad tooshe
a.shape #(4,)   4 ta too yek radifan ,

#cope liste

a[2] #30
a[3] #40
a[2]=200
print(a)
#[ 10  20 200  40]

a[1:4] # array([ 20, 200,  40])


#append, ......
print(type(a)) #<class 'numpy.ndarray'>
#array



#-----2D---------
#inja asle kare
'''


Niaz darid yek chizi bash ek radif, soton dahste bashe



radife1  10 20 30 40 
radife2  50 60 70 80


array()  hamishe sare jashe


#toosh []



[  [radife1] ,[radife2]       ]

[    [10,20,30,40] , [50,60,70,80]   ]


aval radif
bad soton
***numpy array


'''
b=numpy.array([  [10,20,30,40] ,[50,60,70,80]   ])

b.size #8

b.ndim # 2

b.shape #(2, 4)

#******* numpy array hamishe aval radif, bad sotoon

#(radif, soton)
#chanta radif , chanta soton

#2 ta radif , 4 ta soton

print(b)
'''
[[10 20 30 40]
 [50 60 70 80]]

'''

#b[index]

#kodom radif?
#kodom soitoon?


#adade 60 rto mkham poeyda konam



#aval--> kodom radife? radife 0 ya radife 1 --> radif1

#bad --> kodom sotone? sotonme 0 , 1 , 2,3 --> sotone1

#b[radif,soton]

b[1,1] # 60

#-->adade 70 ro mikham

#radife 1
#sotone 2

b[1,2] # 70


#a[2]=200

b[1,2]=70000
print(b)
'''
[[   10    20    30    40]
 [   50    60 70000    80]]

'''

#agha man mikham bgam 

#a[2:3]

#kole radife 1 ro bede

#radife 1 , kole soton ha 

b[1,:] #array([   50,    60, 70000,    80])

b[0 , :] # array([10, 20, 30, 40])


b[: , 1] #array([20, 60])


#radife 0 , sotone 2,3

b[0 , 2:4] #array([30, 40])






#-------3D-------------

'''


numpy.array()
dakhele parnatez

[] default


[ [jadvale1] , [jadvale2]  , [jadvale3]   ]


[ [  [radif1] , [radif2]  ] , [[radif1] , [radif2]  ]  , [[radif1] , [radif2]  ]   ]

tooye yek parnatez




'''
a=numpy.array([  [ [10,20],[30,40] ]  ,  [ [50,60],[70,80]  ]  ,  [[90,100] , [110,120]]     ])

a.ndim #3
a.size # 12

a.shape #(3, 2, 2)

#(chanta jadval , chanta radif, chanta sotoon)


#indexing --> kodom jadval? kodom radif, kdom soton

#Masaln 40 rto mikhay?


#kodom jadval?
#jadvale 0
#radife 1
#sotone 1

#[jadval,radif,soton]

a[0,1,1] # 40





'''

Numpy array --> Faster , More dimentions




0D numpy array --> Number
1D numpy array --> List --> [,,,,,]  [index]
2D numpy array --> Matrix, matriced, jadval --> radif, soton --> [ [] , [] ,[] ,[]  ] ,  matrix[radif,soton]
3d numpy array --> koli jadval dari rooye ham dg


'''



#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------

#---ARRAY FUNCTIONS----------

#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------
#-----------------------------

#nketye aval

import numpy


import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt

#inghad sade

#numpy.array()

a=np.array([10,20,30,40])


#-----ASSIGNMENT------
#dasti
a=np.array([10,20,30,40])


#az 1 ta 2000 bzrm

#a=np.array([1,2,3,4,5,6,])



#numpy --> arange -->

#start , stop , step , dtype

#az chand ta chand , step=1 , dtype = int, float ,..


a=np.arange(1,200) #1 ,.... 199

a.ndim
#a=np.array([1,2,3,4,5..........,199])


#int minvise

#az 1 ta 20 
#b 100 ghesmat taghsim kon
a=np.linspace(1,20,200)
#1--------20 200

a=np.linspace(1, 5,12)

print(a)
'''
[1.         
 1.36363636 
 1.72727273 
 2.09090909 
 2.45454545 
 2.81818182
 3.18181818 
 3.54545455 
 3.90909091 
 4.27272727 
 4.63636364 5.        ]

1 ------------ 5  12 ghemsate msoavi taghsim

'''
# log tor 
#a=np.log(0,10,10,base=e)

#--------------------
#----1D------

#0 ta 100 bsazam
#0 , .. 50 radife 1
#50   99 radife 2

#2 ta radif , 50 ta soton
'''
0 1 2 3 4
5 6 7 8 9


'''
a=np.arange(0,10,size=(2,5))
#TypeError: arange() got an unexpected keyword argument 'size'


#-----ayande --------

#ama yekseri tabe ha size migire



#vagty mikhay bsazii

#-----
#numpy.array()


#k sari tar miszi

#---> size daran --> (size)
#age nadare --> 1D --> reshape() --> 2D


a=np.zeros(10)

print(a) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#a=np.array([0,0,0,0,0,0,0,0,])

'''

1D


2D
2 ta radif 5 soton
0 0 0 0 0
0 0 0 0 0

'''
a=np.zeros(20)
print(a)
#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

a=np.zeros(10)
print(a)
#[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]


#
'''
2 ta radif 5 soton
0 0 0 0 0
0 0 0 0 0
'''

#2 , 5 

#(2,5)

#(radif, soton)

a=np.zeros(10)

a=np.zeros((2,5))
print(a)

'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''


#-------empty
#0 mikjay khali

np.empty(10)
#array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])



#----ones --> 1

np.ones(10)
# array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

#2d
np.ones((2,5))
'''
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

'''



#----full-----
#az 1 
#yek 1d 10 taee adade4

np.full(10,4)
# array([4, 4, 4, 4, 4, 4, 4, 4, 4, 4])

np.full(10,3.14)
#array([3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14])


#dobodi
#avalin vorodi --> shape ro migiran
np.full( (2,5) , 4  )
'''
array([[4, 4, 4, 4, 4],
       [4, 4, 4, 4, 4]])
'''

#------eye-----
np.eye(3)  #yek matrix morabe misaze ke ghotre vasate vataresh az adade 1

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


#1 , diognal matrix  1 2 3

np.diag([1,2,3])
'''
array([[1, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])

'''

np.diag([10,12,20,40])
'''
array([[10,  0,  0,  0],
       [ 0, 12,  0,  0],
       [ 0,  0, 20,  0],
       [ 0,  0,  0, 40]])

'''


#------REVIEW-----------
#numpy---> fast, dimentions


import numpy as np

#---0D----
np.array(10)

#---1D---
np.array([10,20,30])

#---2D---
np.array([[10,20,30], [40,50,60]])


#---arrange
np.arange(1,10,2)

np.zeros(10)
np.zeros((2,5))


np.ones(10)
np.ones((2,5))

np.empty()
np.eye(3)
np.diag([10,20,30])



#-------------------
'''

L10_NAME,LNAME

Ykek array 1D

misazid , dastressi ba index , 
taghir midid , ndim , shape ro mgiirid



2D  --> 10 ta onsor dashte bashe

b dota adadesh dastresi peyda konid va taghir bedid




az tabeye arange b 3 ravesh, v aaz tabey haye zir b y ravehs

ones
empty
zeros
eye
diag


.py baraye bande errsal koniod





ai.2024.alipilehvar@gmail.com

'''










