
"""
In The Name of GOD


Created on Sun Feb 23 15:35:47 2025

@author: Ali Pilehvar Meibody


GMLB_L4


"""


'''
REVIEW


human ------interface  -----machine


interface-->python ----> 2 section



1-------reserved---------------
1.1.python built in function -->print() , input() , len(),type(), int(),float(),str(),....
1.2.keywords --> if , else, for , while


2------unsreserved--------
variables --> zarf -->yek esm(ghavanin) --> value

2.1. Numbers (int,float,complex)
a=20
b=30

c= a+b

** tavan
c=a**2
c=a**b
c=a**8

*zarb
/ taghsim
c=a/b

+
-
%

c=a%b

c=10%2


#---alaem moghayese
= 
== -->true false
!=
>
>=
<
<=

2.2. Boolean (True, False)

2.3. String -->reshte ha

a= qutation

a[0] #index az 0 shoro mishod
a[2] -->sevomi horof

#slicing

az felan ta felano bde

a[start:end+1]

az indexe 3 ta 8
a[3:9]  --> 3 4 5 6 7 8

a[3:9:1] -->hamon balaee --> az ta 9-1(8) 1 done 1 done
a[3:9:2]
a[3:9:5]

a[-1]
a[-1:-4]  alipilehvar


tabe -->str functions --> emal nmikone balke khoroji mide
3 no tabe has -->taghirate

a= ....

.upper()






'''

a=4

a.upper()
#AttributeError: 'int' object has no attribute 'upper'


a='salam'

print(type(a))
#<class 'str'>



a.upper() #'SALAM'

print(a) #salam

print(a.upper())
 
b=a.upper()

print(a) #salam
print(b) #SALAM

'''

1-->taghirat
.upper()
.lower()
.replace('t','b')
.strip()  --> faseley chapo rasto hazf mikrd


2--> adad

.find('a') --> index

.count('a')



3-->true false (check)

.isupper()
.islower()


'''

'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''


#-------------------------------------------
#task1


name='alipilehvarmeibody'

print(name)

print(len(name))

name_len=len(name)



#6 omin charactero bede


#yani l o mikhad

name[5] #'l'


my6char=name[5]


#task2
#chijroi az karbar senesh begire? --> print() input()

#age=input('salam seneto begooo:')
#sene karabr=input('salam seneto begooo:')

#senekarbar
#SenKarbar
#sen_karbar



sen=input('salam seneto begooo:')

sen**2 #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

type(sen) # str

#'45'
#45

a=45
b='45'

b='salam'

b**2


b='salam'
b*2 #'salamsalam'

b/2



sen=input('salam seneto begooo:')
new_sen=int(sen)

final=new_sen**2

print(final) #2025



#-------------------------------
new_sen=int(input('salam seneto begooo:'))

final=new_sen**2

print(final)


#--------------------------


final=int(input('salam seneto begooo:'))**2

print(final)


#------------------
 
print(int(input('salam seneto begooo:'))**2) #2025

#-----------
name='alipilehvarmeibody'

#str funciton
#upper
#upper(name)
#name.upper()


b=name.upper()

print(b)


c=name.lower()


d=name.find('a')
print(d) #0 -->indexe 0 


z=name.find('z')
print(z) #-1  --> ya nist ya az akhar


name='alipilehvarmeibody'

len(name) #18

name[17] #'y'


name[-1] #'y'


name[-1:-4] #-1 -2 -3

name[-4:-1]

#-------------------------------

vorodii=input('salam vorodi bede:')

count=vorodii.count('a')

print(count)


print('salam vorodie shoma ',count,'ta a dare')

#ye raveshe dg hast k in ravesho haminja yad mid


a=20
a=40
a=50


print('salam man ali a hastam ')

print('salam man ali hastam man 20 salame')

print('salam man ali hastam va man', a,'salame')


print('salam man ali hastam va man a salame')

#f string ro estefade kon

print(f'salam man ali hastam va man a salame')


print(f'salam man ali hastam va man {a} salame')
#salam man ali hastam va man 20 salame






name=input('salam esmeto begoo:')

count=name.count('a')


#print('karbare gerami esme shoma' , count ,'ta a dare')


print(f'karbare gerami esme shoma {count} ta a dare')
#karbare gerami esme shoma 1 ta a dare

#--------------------------------
#variables----->
#int , float, numb , string hamechi darim



a=40
b=60

c='salam'
d='ali'




#---------->Iterable----------------

'''
list --> 1-ordered 2-changable 3-allow duplicated
tuple
set
dictionary

'''

#3-------iterable varibales 
#3.1---------LISTS-------

#3.1.1. assignment --> value

a=20
harchi = [10,20,30,40]

print(harchi)

print(len(harchi)) #4

print(type(harchi)) #<class 'list'>

#adad bashe>

harchi=['ali','vahid','reza','hamid']

users=['ali','vahid','reza','hamid']

gharoghati=[10,20,'ali',True,1j,10.5]

gharoghati=[10,10,10,10,10,10]



#---taghir krdn yanichi??
#aval bayad dasteresi peyda koni

#3.1.2. ACCESSS
users=['ali','vahid','reza','hamid']


name='alipilehvar'

#string---> string-->reshte --> reshte az character ha

#2 vomin
#name[2] -->i 


#users=[] reshte az element ha hast

#
b=users[1]

users[3]

#---------------

users[0:3]   #0 1 2

#['ali', 'vahid', 'reza']


#[start:end+1:step]

#3.1.3 change------

users=['ali','vahid','reza','hamid']

users[1]='mohsen'


print(users)
#['ali', 'mohsen', 'reza', 'hamid']


#-->taghirate dg ee ham bekhad -->
#str functions
#list functions----> function ha hast


users=['ali','vahid','reza','hamid']

users[1]='mohsen'

print(users)
#['ali', 'mohsen', 'reza', 'hamid']


#-----------------
#add --->

users=['ali','vahid','reza','hamid']

#insert(index,element)  -->element too oon index ezaf mikone

#insert(users)


users.insert(1,'mohsen')

#khoroji nmide -->styr name.upper() --> zakhrie

#*** EMAL MIKONE

#list function emal mikone khoroji nmid

#str function emal nmikone khrooji mide (zarf)

print(users)

#['ali', 'mohsen', 'vahid', 'reza', 'hamid']

users[0]

users[1]

users[2]



len(users) #5


users.insert(5,'amir')


print(users)

#['ali', 'mohsen', 'vahid', 'reza', 'hamid', 'amir']


#len --> ad adadd?


#.insert(index,element)

#----> append --> kafie element ro bdi b tahesh khdokar ezafe mikone


#.append(element)

#['ali', 'mohsen', 'vahid', 'reza', 'hamid', 'amir']


users.append('mostafa')

print(users)

#['ali', 'mohsen', 'vahid', 'reza', 'hamid', 'amir', 'mostafa']


#-----remove???
#2 ta rah

#['ali', 'mohsen', 'vahid', 'reza', 'hamid', 'amir']


users.remove('ali')


print(users) #['mohsen', 'vahid', 'reza', 'hamid', 'amir', 'mostafa']


#agha man value nadrm idnex drm

#Mikahm bgm iudnexe 0 o hazf kon


#users=['mohsen', 'vahid', 'reza', 'hamid', 'amir', 'mostafa']

users.pop(0)

print(users)

#['vahid', 'reza', 'hamid', 'amir', 'mostafa']



#-------------------------------------------
#change , add(insert, append) , remove (remove,pop)


a=[]
print(a) #[]


#eyk listo haminjori khalish konm?

#clear



print(users)

#['vahid', 'reza', 'hamid', 'amir', 'mostafa']


users.clear()



print(users)

#[]



#delete --> tabe nis 
#yek dastoore (keyword  ) baraye hame variable ha

user1=['ali','vahid','hamid']

user2=['mohsenh','amir','reza']



user1.clear()
print(user1) #[]


#del user2
#print(user2)
#NameError: name 'user2' is not defined


#----------------------------
'''
list --> iterable vairables


assignment
a=[el1,el2,el3,el4]

a[index]

a[start:end+1:step]


#change
a[index]=new_value

#add
a.inseret(index,element)
a.append(element) # b tahesh ezaf mikone

#remove
a.remove(element)
a.pop(indedx)


#clear
a.clear() ---> a vojod dare amaaaa a=[]

del a ---> a is not defiend --> a o zarfo hamehchio baham kharab mikone



list --> baraye zakhrie sazie multiple values(variable)

1-ordered 2-changable 3-allow dupicated

'''


'''
list------ a=[el1,el2,el3,el4]
ordered , changable , allow duplicate

dictionary ---->
ordered , changable , allow duplicate






tuple------>a=(el1,el2,el3,el4)
ordered, unchangable , allow duplicated


set----->a={el1,el2,el3,...}
unordered, unchangable , not duplicated







'''


a=('ali','vahi',20,30)

print(a)
#('ali', 'vahi', 20, 30)

a[0]

a[0]='hamid'

#TypeError: 'tuple' object does not support item assignment


#bayad beham tabdil konid

list()
tuple()
set()
dict()

a=(10,20,30,40) 
print(type(a)) #<class 'tuple'>


b=list(a)

print(type(b)) #<class 'list'>


a[0]=1000


b[0]=1000

print(b)
#[1000, 20, 30, 40]

a=tuple(b)

print(a)
#(1000, 20, 30, 40)


'''
casting --> tabdil krdne variable tyep ha beham

tuple functions

'''

#-----
a={10,20,30,40}

print(a)
#{40, 10, 20, 30}
#a[0]

#@ordered--> index --> access -->change??

#kolan azin set ha jaee estefade mishe -->kole code chizish taghir kone


#duplicated nmizare (tekrari ejaze nmide)


a=[10,20,30,10,10,10,10,10]

a=(10,20,30,10,10,10,10,10)


b={10,20,30,10,10,10,10,10,10}

print(b)
#{10, 20, 30}

#list --> set  --> list 


#---------------

a=[10,20,30,40,50]


a[0]


a[1]


#index oomade ke behesh dastresi peyda koni



#b={10,20,30}


moshakhasat=['ali',30,70,180]



#yadam bmoone k ghad etarafo kodom index gozahstam

moshakhasat[3]

moshakhasat[0]


#dictionary --> { : , : ,      }

#kilidvazhe --> mokhafaf bzaram (key)

#jaye index

a={'name' : 'ali'  ,  'age' : 30 ,  'wighet' : 70 , 'height':180}


a['name'] #'ali'

a['age'] #30

#ghabele taghire ?



a['age']=50


#yek jadid biaram
#machine



a['car']='bmw'


#--------------------------
'''

unreserved------------------------
1-numebrs (int,float,complex)

2-boolean

3-str ( = '' , [index] , [start:end+1:step] , str.function())
**str function ha khoroji midad emal nmikrd



4-iterables ( chanta variables)

4.1. list --> ordered , changable , allow duplicated
a=[el1,el2,el3] 
a[index]
a[start:end+1:step]
list.functions ----> append , insert , remove,pop , clear

4.2.dictionary --> ordered (key) , changable, allow duplciade
a= { 'key1' : 'value1' , 'key2' : 'value2'}
a['key1']

a['key1']='new_value'

a['new_key']='new_value'




4.3.tuples --> ordered, unchangable** , allow duplicated
---> sql, data base (paygahe dade)
a=(el1,el2,el3,el4)
a[index]
a[start:end+1:step]


4.4. sets --> unordered (no index) , unchangable , no duplicated

---> mitoni hazf koni duplciated haro (tekrari haro)






casting funcitons
list()
tuple()
set()
dict()

a=[.....]

b=tuple(a) ---> list --> tuple



'''


#-------------------------------------

#---------------------------------------------------
'''

----reserved-----
1--->built in funcitons

2--->keywords----> logic -->dastoooor


----unreserved----
variables

'''


print('salam')



'''

hadaf--> yek khat az codeto biay bgi
ye shart bzari vase run shodanesj



khate ghablesh --> sharteto benevis


'''



'''


if shart:
    dastooreto inja benevis




dart ---->
if (shart):{
        
        
        } ;



if shart:
    dastoooor


dar yek soorat ejra mikone ke shart --> javabesh True bashe




sharteto bayad begoone ee bnvisi k ya True False

yeki az rahash --> == != > < >= <=
dovomin rahesh --> tabe khorojish true false
khdoet besaz

str.function --> True False
.isupper() 




'''

print(10>20)

print(10==10)

print(10==10.00)


print(type(10)==type(10.00))



#just if----> sharti koni

sen=int(input('salam senetoon ro begid:'))


if sen>20:
    print('salam')







sen=int(input('salam senetoon ro begid:'))


if True:
    print('salam')





sen=int(input('salam senetoon ro begid:'))


if sen>20:
    print('salam')





sen=int(input('salam senetoon ro begid:'))


if False:
    print('salam')









'''


if shart:
    dastooor
    
   #body (badane)
   
   
   
   
    
if shart:
    dastpooor1
    dastoor2
    dastoor3
    




'''




sen=int(input('salam senet cheghadre:'))



if sen>20:
    print('salam')
    a=10
    b=a+10
    c=a*b
    print(c)
    
    print('welcome')



#------------------------



sen=int(input('senet cheghadre?'))


if sen>20:
    print('salam')

    
    
  
    
    
print('khodafez')






'''


if shart:
    dastooor1
    dastoor2
    dastooor3
    dastoor4
    
    
    
    
dastoor(birone sharte va asan sharte mohem nsi va rabti ndre)





'''




sen=int(input('salam seneton cheghadre:'))



if sen>18:
    
    print('salam khosh oomadid')
    
    
    
'''

--------just if-----------
just if ---> fght yedone if


if shart:
    dastoorat
    
    
age sharte True shod --> dastoor ejra mishe
age nshod chi?? False?--->ejra nmishe
ejra nmsihe--> bikhialehs 
khali




-----------------
y dorahi baz koni

shart 0---> ag shod inkaro kon (dastor1)
age nashod (nemigi bikhial) (dastoor2)


            shart
          /      \
         /        \
       True       false
       yekaro      yekare dg
       
       
       
      
'''





sen=int(input('salam seneton cheghadre:'))


if sen>18:
    
    print('salam khosh oomadid')
    

#20 ---> slam khosh amadid
#15 --> hichi
#----> JUST IF 



#age false shod hichi na yekare dg kon


#shart --> ag true shod dastoore 1
#ag false shod dastoore 2

#if else


'''
shart darim

ag shart True shod dastoore1
ag shart False shod dastoore2



if shart:
    dastooor1
else:
    dastoor2
    


'''





sen=int(input('salam seneton cheghadre:'))


if sen>18:
    
    print('salam khosh oomadid')

#20 ---> slam khosh amadid
#15 --> hichi







sen=int(input('salam seneton cheghadre:'))

if sen>18:
    print('salam khosh amadid') #mese ghabli
    
else:
    print('shoma zire sene ghanoni hastid')
    
#20---> slam khosh amadid
#15---> shoma zire sene ghanoni hastid





'''
NOKTEYE PAYANI


zamani k kalameye agar , check, sharti ---> if statement




Just If

age sharte1 shod dastoore 1
age nashod k hichi


if shart:
    dastoore1
    


if shart:
    dastoore1
    dastoore2
    dastoore3
    
    
(birone body , adie hamechi)



#-----------------------
if else-->
age shart true shod kare 1
age nashod kare2



if shart:
    dastoore1
else:
    dastoore2
    
    
    
if shart:
    dastoor1
    dastoor2
    dastoor3
    dastoor4
    ....
    
else:
    dastoore5
    dastoore6
    dfastoore7
    dastore....
    
    
    
[if o else nadare]


'''




'''



Task1-----------------------
yek esm begire va tedade a ro hesasb kone
va tedade b ro hesab kone
+ ham kone

va ino namayesh bnede

--> salam arz shod javabe nahaeie shoma .... mibashad




TASK2------
yek list besazid va indexe 3 vomesho taghir bedid





TASK3------
yek list besazid va clear konidesh va badesh behesh yek esme jadid ezafe konid ba yek tabe




TASK4------ (hard)
3 bar az user esm begirid
doone doone esm haro too ye yek list berize 
ke esme liste bashe users



TASK5------
sene fard ro begirid va agar balatar az 18 bood bege ghanonie ag nabod bege ghanoni nist





TASK6------
sene fard ro begirid va agar balatar az 18 bood bege ghanonie 




TASK7------
az fard esmesho begire check kone ag hame horof ro bozorg zade 
bege tabrik migam




TASK8--------
az fard esmesho begire check kone age besoorate title neveshte bod
bgee sabt shod
age naneveshte bod bege motyasefane format doros nist






'''






















