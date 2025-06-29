
"""
in The Name of GOD


Created on Sun Mar  2 15:34:52 2025

@author: apm

L6_GMLB


"""


'''


python


-------reserved--------

python buil in fucntion ---> print() ,input() , type() , len() , max() ,min()
abs()

keywords--> if 

if ---> just if (yek shart)
if else---> dorahi

if elif else --> dorahie ye rahesh dorahie dg hast


halghe ha
for
while





-------unreserved---------
zarf--> (int,float,complex,bool)
(str, strfucntion .upper())

iterables --> list,tuple, set,dictionary (function)
order, change , ...





'''




'''

L4---------


'''

name=input('salam esmet:')

a_numb=name.count('a')
b_numb=name.count('b')

print(a_numb+b_numb)




#-----
a=[10,20,30,40]

a[3] #indexe 3vom

a[2] #elemente 3 --> indexe chand?



#-----
a=[10,20,30,40]

#del a

a.clear()


a.append('salam')

#-------

sen=input('salam seneto begoo:')

print(type(sen)) #<class 'str'>

#14 --> '14'

# + - * / , == > <

#salam > 10

#'14' > 10 


#14 > 10



sen=int(input('salam seneto begoo:'))

#ashar nadare --> adad mishe


#35.5 -->error -->  35 (sahih)


sen=float(input('salam seneto begoo:'))

#chek kone ag bala 18 bege ghanoni ag na bege nis

if sen>18:
    print('sene hsoma ghanonie')
    
else:
    print('sene shoma ghanoni nist')
    
    
    
#--------
#fgth ma m
#rahzani kj doinbale sene balaye 18 


if sen>18:
    print('sene shoma ghanonie')

#sen<18 --> hichi anjam 

#--------

esm=input('salam esmet?')

#< > == !=
#fucntion
#az function haee k true false midn estefade
#str function --> tabe hashon is shoro mishod

#isupper()


if esm.isupper():
    print('tabrik esmet dorose')

#if khalie


#---------


if esm.istitle():
    print('esme shoam formate doros ro dare')
    
else:
    print('esme shoam doros nis')


'''

L5-----


'''

code=input('salam codeto begoo:')
name=input('salam name mahsolo begoo:')
price=input('salam gehymate mahsoolo begoo')


text=f'''

----plutus-------

product name: {name}
product code: {code}
    
    
    total price: {price}
        
        
    company .24
    
------------------
'''

print(text)

#------------------------------------
code=input('salam codeto begoo:')
name=input('salam name mahsolo begoo:')
price=float(input('salam gehymate mahsoolo begoo'))


new_price=price - (30/100)*price

new_price=(100/100)*price - (30/100)*price
new_price=(70/100)*price 
new_price=0.7*price 




text=f'''

----plutus-------

product name: {name}
product code: {code}
    
    
    total price: {new_price}
        
        
    company .24
    
------------------
'''

print(text)




#-----
code=input('salam codeto begoo:')
name=input('salam name mahsolo begoo:')
price=float(input('salam gehymate mahsoolo begoo'))


text=f'''

----plutus-------

product name: {name}
product code: {code}
    
    
    total price: {0.7*price}
        
        
    company .24
    
------------------
'''

print(text)




#-------------------------
code=input('salam codeto begoo:')
name=input('salam name mahsolo begoo:')
price=float(input('salam gehymate mahsoolo begoo'))


text=f'''

----plutus-------

product name: {name}
product code: {code}
    
    
    total price: {0.7*price}
        
        
    company .24
    
------------------
'''

print(text)



#----------------------
code=input('salam codeto begoo:')
name=input('salam name mahsolo begoo:')
price=input('salam gehymate mahsoolo begoo')

#100 --> '100'
#100 , usaddsah


#str man havie rgahame

price.isdigit() #az adad tashkil shdoe bashe True , false


#check kone 
#ag adad bood edame bde namayesh

#age na bege lotfan adad vared kon








text=f'''

----plutus-------

product name: {name}
product code: {code}
    
    
    total price: {0.7*price}
        
        
    company .24
    
------------------
'''

print(text)




#-------
code=input('salam codeto begoo:')
name=input('salam name mahsolo begoo:')
price=input('salam gehymate mahsoolo begoo')

if price.isdigit():
    #vase onaee hast k price ro doros zadan
    price=float(price)
    text=f'''

    ----plutus-------

    product name: {name}
    product code: {code}
        
        
        total price: {0.7*price}
            
            
        company .24
        
    ------------------
    '''

    print(text)
    

        
else:
    #onae hast k price ro doros nzdn
    print('lotfan adad bezan')











text=f'''

----plutus-------

product name: {name}
product code: {code}
    
    
    total price: {0.7*price}
        
        
    company .24
    
------------------
'''

print(text)




'''
3 bar az user esm begirid
doone doone esm haro too ye yek list berize 
ke esme liste bashe users




machine hesabi benevisid k az user
do adad begire va badesh alamat (+ , - ,...)
badesh --> print kone javab ro
(jam,tafrigh,zarb,menha)




L5-------------------
TASK5 - 5 - 6


#-------------------------
TASK8


'''



#---------------------------------------------
#-----------------------------------------

print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')



#---mishod ey kash --> ye khat bnviusm
#ejra kone


#keywords ---> dovom baskha az reserved ha
#logico taghri midan
#banfashan



#tekrar---->Halghe
#for
#while


#------for----------------


#for, while (halghe) barname bekahd yek kario tekrar kone
#niaz dare b yechizi bename 
#shomarande 
#zarfe (i,j ,k salam ,...) --> 
#start shoro mikone (0)

#end (100 , 10)

#az start ta end done done miad dastoro ro ejra mikone





'''



for shomarande in iterable:
    dastoooor
    
    

#shomarande -->i **shoma harchi mitoni benevisi


#iterable--> range(0,10)  ->range(start,end+1)

#range(5,11)


1 -->100 ta dastoor
    
    
    
    
    


'''




print('salam')




#name='alipilehvar'

#name[2:8]  2,3,4,5,6,7


#--------------------------------------
#avalie -->0
#akharie ham include nist
#----------------------------------------




for i in range(0,10):
    print('salam')



'''

python -->yek kari mikone (1*)
yechizi ham ejra mikoen (2*)


1*         2*
i=0 --> dastoor
i=2 --> dastoor
.....
i=9 --->





1*         2*
i=0 --> salam
i=2 --> salam
.....
i=9 --->


'''

for i in range(0,10):
    print('salam')

'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
'''





for i in range(0,10):
    print(1)


'''
1*         2*
i=0 --> 1
i=2 --> 1
.....
i=9 --->1


'''




for i in range(0,10):
    print(i)
    
    
'''
i=0   ---> 0
i=1   ---> 1
i=2   -->2
....

i=9   --->9






*******************
zamani k yek code
yek khat
do khat
bekhay tekrar koni



che sabet che dynamic ( moteghayer)
--> halghe

halgeh too delesh ye mantegh dare --> az shomarande estefade mikone(I)

ama har dafe baraye har shomarande --> dastoor ro ejra mikone


inke to  baraye tekrare dastooret bekhaye mahdoode entkehab koni

az koja ta koja --> zamani k dari migi i az chand ta chand bashe



i in range(0,10)






'''
    
    

for i in range(5,10):
    print(i)
'''
5
6
7
8
9
'''


for i in range(5,10):
    print(i)
    print('salam')
    
'''
5
salam
6
salam
7
salam
8
salam
9
salam

'''


#ta chanta??

#ta madami k tooye badaneye for hasti


#if , else elif, for , while --> yek badane


#choon ina omdn codee ro taghir bdn az halate adi

#pas ina yek gehsmate code ro mikhan tyaghir  bdn




for i in range(5,10):
    print(i)
    print('salam')
    
    
print('khodafez')




for i in range(0,10):
    print('salam')

'''

XXXXXXGHALAT

5
salam
khodafez
6 
salam
khdoafez
.....

5
salam
6
salam
7
salam
8
salam
9
salam

(9?? tahe halghas --> 10 bshe miad biron)
edamey code
khodafez





'''



for i in range(0,10):
    print('salam')
    
    

    
for k in range(0,10):
    print('salam')
    
'''

k--0   dastor
k-->1



'''  

for k in range(0,10):
    print('salam')
    print(k)



#esme zarf i index

for item in range(0,10):
    print('salam')



for item in range(0,10):
    print(item)

'''
item -->0  print(item) -->print(0) -->0
.....



'''



for chiz in range(0,10):
    print(chiz)







 
    
'''

******************************
halghe ha b 3 chiz niaz daran

1-->shomarande dashte bashi (i , k , j , ...)
2-->baraye shomarandat yek mahdoode bezari bgi i ro bokon felan ta felan
3--> dastoori k mikhay dar in mahdode ewjra bshe


shomarande,mahdoode, dastooor(s)









i in range(0,10)



in karesh ine ke to baraye shomarande range bezari

i in ......


harchizi k iterable bashe





'''

    


for i in range(0,10):
    print(i)



mylist=[0,1,2,3,4,5,6,7,8,9]

for i in mylist:
    print(i)



'''
range--> 0 ta 9


zarf[]




list,tuple , str  --.element


yek list besazi
ag bgi



for i in mylist:




done done
i ro mziare oon element




'''


mylist=['ali','vahid','reza']

for i in mylist:
    print('salam')

'''

shomarande, mahdoode, dastooor



i-->shoamrande

i--> ali  i=ali   dastooor | salam
i-->vahid i=vahid  dastooor | salam
i-->reza i=reza  dastoooor |  salam




'''

mylist=['ali','vahid','reza']

for i in mylist:
    print('doroood')


'''
doroood
doroood
doroood

''' 
a=10 
    
mylist=['ali','vahid','reza']

for i in mylist:
    b=a+2


'''
i=ali  --> b= 10 +2 --> b=12
i=vahid --> b = 10 +2 --> b=12
i=reza -->b=10+2 --> b=12




'''
    
a=10 
b=a+2
b=a+2
b=a+2


#---------------------------------------






mylist=['ali','vahid','reza']

for i in mylist:
    print('doroood')



mylist=['ali','vahid','reza']
for i in mylist:
    print(i)



'''


i=ali     --> print(I)  -->print(ali) -->ali
i=vahids  -->print(i)   -->print9vahid -->vahid
i=reza                                reza


'''


'''

ali
vahid
reza


ITERATION..........


'''

mylist=['ali','vahid','reza']

print(mylist) #['ali', 'vahid', 'reza']


for i in mylist:
    print(i)

'''
ejazeye dastrsi b done done elementat mide

'''

#i o taghir bdm
#i o check konm(if)

#i o beshmoaram
#bekeshma biron
#hazf konm


#iteration --> bazressii --> varressi




mylist=['ali','vahid','reza']


for i in mylist:
    print(i)

'''

ali
vahid
reza

'''

#baraye hargoone elementi k dar in list hast:
    
    #ahr element ra ....
    

for i in mylist:
    print('salam ',i)
    
    
'''
salam  ali
salam  vahid
salam  reza

'''
mylist=['ali','vahid','reza']


for i in mylist:
    print(f'salam arz shod be karbare azizo gerami jenabe {i}, khosh amadid')


'''
salam arz shod be karbare azizo gerami jenabe ali, khosh amadid
salam arz shod be karbare azizo gerami jenabe vahid, khosh amadid
salam arz shod be karbare azizo gerami jenabe reza, khosh amadid

'''




#1 ta 10 ofoghi kenare ham print kone

print(1)
print(2)
#1
#2

#print(1) ,print(2)

print(1,2) #1 2



print(1,end=' ')
print(2,end=' ')
#1 2 




for i in range(0,10):
    print(i)

#i->0 print(0) enter
#i--1 print(1)  1 zire 0

'''
0
1
2
3
4
5
6
7
8
9

'''

for i in range(0,10):
    print(i,end=' ')

#i-->0 , badesh print(i) -->0 enter bzni space bzn


print(1,end=' ')
print(2,end=' ')
print(3,end=' ')




for i in range(0,10):
    print(i,end=' ')

#0 1 2 3 4 5 6 7 8 9 


mylist=['ali','vahid','reza']


for i in mylist:
    print(f'salam bh msohtarie aziz {i}',end='||' )



'''
salam bh msohtarie aziz ali||salam bh msohtarie aziz vahid||salam bh msohtarie aziz reza||
'''



mylist=['ali','vahid','reza']

print('salam b moshtariane aziz')

for i in mylist:
    print(f'jenabe {i}',end=' ')

'''
salam b moshtariane aziz
jenabe ali jenabe vahid jenabe reza 

'''


mylist=['ali','vahid','reza']

print('salam b moshtariane aziz',end=' ')

for i in mylist:
    print(f'jenabe {i}',end=' ')

#salam b moshtariane aziz jenabe ali jenabe vahid jenabe reza



mylist=['ali','vahid','reza']

print('salam b moshtariane aziz',end=' ')

for moshtari in mylist:
    print(f'jenabe {moshtari}',end=' ')
    
    
    
#moshtari -->ali
#avhdi
#reza

#iteration


#for -->iteration

#bre dakhele yek reshte, yek list


name='alipilehvar'


for i in name:
    print('salam')

'''

i-->a   salam
i--->l  salam

b tedade horofoe esm , salam




'''


name='alipilehvar'


for i in name:
    print(i)

'''
a
l
i
p
i
l
e
h
v
a
r

'''



#list, (tuple,dictionary) / reshte

#done done elementasho i ro mzire jash




#-------------------
#------>Iteration-------------

#dastoor sade nis print .....

#2 ta dastore asliii

#for --> done element (iteration)

#vase har i --> yechizio check konim



#l print kon yaft shod
#bayad done doen beramdone doen 
#aval check mikone ( check mikone k elemetn aya l hast ya na)

name='salam salam'


for i in name:
    if i=='l':
        print('yaft shod')
    
'''
yaft shod
yaft shod

'''



'''

i-->s   / s==l -->false -->chizi ejra nmishe
i-->a  / a==l -->false --> chizi ejra
i-->l / l==l -->True -->  yaft shod
...
..
i-->l ----> yaft shod
i-->a  -->
m----->


2 bar chap mikone yaft shod


'''

#---------iteration--------------

name='salam salam'


count=0

for i in name:
    if i=='l':
        count=count+1
        
    


#beshmoran yechizio 

#chizi bname print ->na
#jrea mikone chizi print

print(count) #2






name.count('l') #2
    








#----iteration 3 ta kar varresiie reshte,list,....
#for if

#1--->print


for i in name:
    if i=='l':
        print(i)


#2--->beshmor
count=0

for i in name:
    if i=='l':
        count=count+1

print(count)


#3-->jodash koni brizi too ye liste dg

mylist=[]

for i in name:
    if i=='l':
        mylist.append(i)
        

print(mylist)
#['l', 'l']



#for i in reshte:
    
    
#count -->


#for i in list --> 3 takaro mikonan

#-------------------

my_numb=[10,20,30,40,50,60,70,80,90,100]


for i in my_numb:
    print('salam')

'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam

'''

my_numb=[10,20,30,40,50,60,70,80,90,100]


for i in my_numb:
    print(i)


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
100
'''


my_numb=[10,20,30,40,50,60,70,80,90,100]


#chi mikhjay check??

#khodet , barnameniaz , porozhe

# har adadi k balaye 50 bood 


#for i in my_numb:
#    if i>50:
    

#soal mishe --> chiakr kone??? --> 3 ta kar

#print

my_numb=[10,20,30,40,50,60,70,80,90,100]
for i in my_numb:
    print(i)


my_numb=[10,20,30,40,50,60,70,80,90,100]
for i in my_numb:
    if i>50:
        print(i)
'''
60
70
80
90
100

'''

#2-->man mikham tedsade element hae k bozorgtar az 50

count=0
my_numb=[10,20,30,40,50,60,70,80,90,100]
for i in my_numb:
    if i>50:
        count=count+1
        #print(i)
    
        
print(count) #5



#3--->
new_list=[]

my_numb=[10,20,30,40,50,60,70,80,90,100]
for i in my_numb:
    if i>50:
        new_list.append(i)
        
        
print(new_list)     
#[60, 70, 80, 90, 100]




#------------------------------



list_50bozorg=[]
list_50kochak=[]

my_numb=[10,20,30,40,50,60,70,80,90,100]
for i in my_numb:
    if i>50:
        list_50bozorg.append(i)
    else:
        list_50kochak.append(i)
        
        
print(list_50bozorg)
print(list_50kochak)


#------------------------------------


my_numb=['ali','vahid','hamid','reza']


#boro too ye list begard
#harkodom k andaxzeye oon esmesh bishtar az 3 bodo 
#beshmor

'''
ma yek list darim az user ha
 lotfan tedade userhaee k esmashon bish az 3 harf darad r
 ra beshmorid
 
'''


'''
man yek list daram
done done bayad bekeshamehson biroon
done donashon ro bayad check konam ke
andazashon bsitra az 3 bashe
age bashe beshmorameshoon
'''


count=0
my_numb=['ali','vahid','hamid','reza']
for i in my_numb:
    if len(i)>3:
        count=count+1


print(count) #3


my_numb=['ali','vahid','hamid','reza']
for i in my_numb:
    if len(i)>3:
        print(i)

'''
vahid
hamid
reza

'''



new_list=[]

my_numb=['ali','vahid','hamid','reza']
for i in my_numb:
    if len(i)>3:
        new_list.append(i)


print(new_list)



#----
mynumbs=[10,20,30,40,50,60]


for i in mynumbs:
    print(i)


#y shart --> ag in shart True shod oon dastoro ejra nkon bepar broo badi
#eleemnto ignore (nadide begir)


mynumbs=[10,20,30,40,50,60]

for i in mynumbs:
    if i==30:
        continue
    print(i)
    
'''


10   --> 10
20  -->20
30  -->  XXX
40 --> 40
50   50
60  -->60



10
20
40
50
60


'''  
    

mynumbs=[10,20,30,40,50,60]

for i in mynumbs:
    if i==30:
        break
    
    print(i)
    
'''
10 -->  10
20 ----> 20
30 --> motevaghef mishavad

10 
20
    
    

'''












'''

TASK1-------
yek listi az adad ro darim
tedade zoj haro beshmore

TASK2-------
yek listi az adad ro darim
ADADE ZOJ ro dar yek list
adade fard ro dar liste dg berize



TASK3-----
users=[ali,vahid,reza]

yek listi az asami user darim
done done shon begare
tedade usere haee k too esmeshon a daran ro beshmore

3



TASK4---->
az user passsword begiree
be tedade passworde oon fard
* chap kone

1234
****



TASK5-->
az user yek password begire
va check kone k password ghavie ya na

- andaze bayad bishtar az 8
- bayad hatman yek horofe bozorg dashte bashe
- bayad hatman character dashte bashe



L6------


advance ---->

---- 
adade 1 ta 100 ro yeki dar mioon chap kone



---
count down beshmore yani
10 second remaining
9 second remaining
...
...
...
...
...


---
bere dakhele yek list begarde harkodom k fard bood 
ro joda kone 
badesh dar nahayat bayad yek list bede ke tekrari ham
dakhelesh nabashe

mesal--> [10,20,13,14,14,15,16,17,17,24,27]

khoroji--->[13,15,17,27]



----
mesale ghabl hamoon bashe ama khoroji
na tanha tekrari nabashe balke soodi moratab shode bashe
az koochik b bozorg



------
yek listi az kole file ha darim
bere va bema formatesho bede dar yek list


myfiles=[new.py , screen.jpg , data.csv , animation.gif]

output--> [py,jpg,csv,gif]


----
10 bar az karbar esm begire har dafe be list ezafe kone
age karbar esmi ferestad ke ba 'a' shoro shdoe bood
dg az karbar esm nagire va motevaghef beshe






'''

        
        
        



