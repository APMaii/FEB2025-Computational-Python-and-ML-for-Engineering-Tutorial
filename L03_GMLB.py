"""
In The Name of GOD

Ali Pilehvar Meibody
@author: apm

L3_GMLAB
"""
'''

Human (english) --------intermediate language --- Machine ( binary 0,1)



intermediate languages (C , C++, Python,....)


---> Python + Mohite toseye paydar
--> Anaconda ----> python + IDE (spyder,....)


Spyder--> codeto inja minevisi  -> script --> format .py

mese safe chat-->mitoni benevisi ta run nkrdi etefaghi nmiofte


RUN --> SEND


# qutation-->comment bezari

python------------------------
RESERVED----> 1-python built in function ( tabe ha -->amalkard)
print() len() type() ,......
2-keywords--->mantegh if , else , for , and , or , not , ......
python mishnase---> rangi mishe


Unreserved---->  rangi nmishe-->sefid---> esme zarf
esme yek moteghayer (variable)

esm --> mohtava (value)

**esme zarf yekserei ghavanin dare (space,adad, character _)

--->
1- numbers ( int, float, complex)
2- Boolean (True , False)
3-String ( kalame,character ,....)



computation operator
amalgarhaye mohasebe -->
**
*
/
+
-
%
=

dastoor




'''
a=10
b=20

c=a+b
c=a**2

d=(a**2) + (b/2) + 100

'''

amalgar ha --> 
comparison 
moghayese

== --> aya mosavi hast>

a>b aya bozorgtar hast?
a>=b 

a<b
a<=b

a!=b aya a ba b mosavi nist?


benevisi-->ejra nemishe
barname javab mide-->

True
False

--> Boolean



'''

a=True
a2=False
#a=true -->ghalkat

b='True'



a=10
b=20

a==b

a!=b

a>=b


a>b

a<b

a<=b


#==========================================
#=========================================
#===========================================
#==========================================

print()

#tabe --> ()


print(40)


print('salam')


a=20
print(a)


a='ali'
b='semiconductor'

print(a,b)



print('salam man ',a,'hastam va b reshteye ',b,'alaghe mandam')

#salam man  ali hastam va b reshteye  semiconductor alaghe mandam




#mohtaviatesho print mikone

type(a)


c=True

type(c)
#bool


a='salam'
type(a)

print(type(a))



len(a) #5

a='salam '
len(a) #6




#---------------------
#TABE HAYE DAKHELI ---> RESERVED ->1)PYTHON BUILT IN FUNCITON
print()
len()
type()


#castingg----
#khdoe type ha harkodom y tabe drn

int()
str()
bool()
float()
complex()


a=450
b=3.5

print(type(a))
#<class 'int'>

print(type(b))
#<class 'float'>


#b ->yek asharie--> tabdilesh konm b int??
#casting

c=int(b)

print(type(c))


d=float(a)

print(d) #450.0

print(type(d)) #<class 'float'>

#-------------------------------------
#man yad gereftam chijori chizi ro namayesh bedam
print()

#age bekham chizi ro begiram chi? vorodi bgirm

'''
code -->scripte

1--->voroddiiiii
file , download, adadi benevisi , user 

2--->mohasebati
+ - / --->

3-->khoroji
print()
plot --> rasm kone
save 
upload ,.....



'''

a=40
sen=40

#mikham az karbaram senesho beprosam
#YA MIKHAm y bazi trarahi konm
#yek vorodi bgirm
#voroodi--> input

input()



#man miam y soal miporsam az karbaret
#soali k karbartet javab bde ro pas migirm
#pas to bayad mano zakhrie koni

print('salam senetoon cheghadree')

input('salam senetoon cheghadre:')

#zarf bzari zakhirahsh konm



sen=input('salam senetoon cheghadre:')




#---------agha ye barname nevbis
#k esme karbaro begire
#bad benvisi jenabe .. khosh amadid


esm=input('salam esme shoma chist:')


print('salam khosh amadid ',esm)



#-----NOKTE--->INPUT --> Tamame khrooji haro b soorate str pas mide



a=20
b='20'


print(a==b)



print(type(a))

print(type(b))


c=a/2
print(c) #10.0

d=b/2


#====================
#input hame khoroji hash --> str pas mide
#vasash mohem nsi k to chi vared mikone

sen=input('salam senetoon cheghadre:')

print(sen) #40
print(type(sen)) #<class 'str'>
#40 ---> '40'


sen/10 #TypeError: unsupported operand type(s) for /: 'str' and 'int'


#?
#man age bedonam tarafe mogahbelam ghrare adad vared kone
#chijoori 
#input k hamishe behem str barmiugrdone
#chijori tabdilesj konm b ye adad????

#int
#float



sen=input('salam senetoon cheghadre:')

new_sen=int(sen)



print(sen) #40
print(type(sen)) #<class 'str'>


print(new_sen) #40
print(type(new_sen)) #<class 'int'>

final=new_sen/10 + 100

print('salam javab shod:',final)

#salam javab shod: 104.0

print('salam javab shod:',int(final))


#--------------

sen=input('salam senetoon cheghadre:')
new_sen=int(sen)



sen=int(input('salam senetoon cheghadre:'))
print(sen)
print(type(sen))
#amale riazi ro anjam bdi


#flkoat ham bokoni

sen=float(input('salam senetoon cheghadre:'))
print(sen) #40.0




#---------------------------------------------
'''
Variables -->moteghayer ha

1--->numbers (int, float, complex(j,..))
** * / + - %

2--->boolean (True,False)
== > >= < <= !=

3--->string --> quotatiion



'''


#3.1.---------assign (meghdar dehi)
a='salam'
a=str('salam')



print(a)

print(type(a)) #<class 'str'>


print(len(a)) #5




#------inke 
name='alipilehvarmeibody'

print(name)

print(len(name)) #18

#man age bekham dastresi peyda konm b 4 omin horof
#chiakr konam??



#string-->reshte --> reshte e az character ha

#chaarctere1 | chjaarctere2 | charactere 3 ,...-


#---->adade shooroo dar barname nevisi 1 nist
#0 ---> ino hamishe yadet bashe -->

#kodom character

name='alipilehvarmeibody'
#@charactere4 ghalate choon az 0 shoro mishe adad

#charactere 3vome -->in dorose (0 1 2 3)

#index-->

#man ag p ro bekham migan yani to indexe 3 e zarfe name ro mikhay



#age shoma indee 3 ye variablee name ro bekhay -->

name[3] #'p'
#[print ] koni 
#ya inek in khoroji mide zakhriash koni tooye ye zarf


new_char=name[3]

name[7] # 'h'


name='alipilehvarmeibody'
name[0] #'a'
name[1] #'l'


#aya man mitonam chanta chanta var drm?

#yani man az idnexe 


#agar man lip ro bkham


# a l i p i l

# 0 1 2 3 4 5

#   1 2 3

#az 1 ta 3-->

name[1:3] #'li'

#ta --> :
    

#exclude-->dar nazar nemigire


# start to end ---> start:end+1

name[1:4] #'lip'
#1 2 3 

# a l i p
#0 1 2 3 

# 0 : 3+1

name[0:4] #'alip'


name[:4] #'alip'


#ta akahr


#az 4 ta akahr


len(name) # 18

#indexas --> 0 1  2 3       17 

name[4:18] #'ilehvarmeibody'


name[4:] #'ilehvarmeibody'




#[start:end+1:step]



#[3:8]
#[3:8:1]
name='alipilehvarmeibody'


#pileh
#3 4 5 6 7 
name[3:8] #'pileh'

name[3:8:1] #'pileh'

name[3:8:2] #'plh'


#-----------------------


name='alipilehvarmeibody'


#agha boro harja p didi bokonesh b
#ya masalan agha p kojas? indexe chande
#ya agha msihe hamaro bzoorg krd?
#va va va....


print()
input()
type()
#pyuthon built in function-->tabe haye dakhelie python
#ina baraye hamaaaan str, int , float ,....
#varangi ham msiahn





#------str functions--------
#yekseri tabe hastan-->ke mokhtase str ha hastan

#function haee hastan k fght baraye str hastan na int na batraye float,....

#ina rngi nmishn
#asan injori estefade nmishe


#tabe -->upper() --> bozorg mikone hamechio


name='ali'


#upper(name)

#bayad aval esme zarfeto benevisi

name.upper() #'ALI'


name='ALI'

name.lower() # 'ali'



#replace-->


name.replace('A','B') # 'BLI'


#soale 1 --> ina aya rooye khode moteghayer taghir ijad mikonan?
#aya mitonim inaro zakhire konim?
#tooye parantez chia mitonim benevisim ?
#chantan? hamaro fhefz konim?

name='ali'

print(name)  #ali


name.upper() #'ALI'


print(name) #ali

#in tabe ha emal nemikone balke khorji mide
#yani bayad zakhriash koni tooye yek zarf


new_name=name.upper()

print(name) #ali
print(new_name) #ALI

#tabe haye str (str functions)--> emal nemikone, balke khoroji midahad


sent='in the name of god'

sent.upper()
#'IN THE NAME OF GOD'

print(sent)

sent.title()
#'In The Name Of God'

sent.capitalize()
#'In the name of god'



'''

str functions--->
1--> tabe haee hastan k fght baraye str hatsan
2---> in tabe ha be soorate esme_zarf.esme_tabe()
name.upper()   name.lower()

3--> taghiri rooye zarfe asli k roosh dot zadi emal nmikone
(emali nist) --->khoroji mide--->khoroji ro to mitoni too y zarf zakhrie koni


4--->mage nagofti khoroji mide? 40 ta function
hame ina 3 dastan


1--> taghiri k ijads mikoen ro khoroji mide
hamoon value ba yekseri taghirat pas mide

.upper()   bozorg pas mdie
.lower()  kochik mikone pas miude
.title()  avale har kalamaro bozorg mikone pas mide
.capitalize()   avale kole jomle ro bozoreg mikone
.replace(old,new)  harchi olde b new tabdil mikone
.strip() ---> faslee csamte chap va rast ro hazf krd



2----> yek adad pas mide beht 
.find(characteeri k donbaleshi) --> find mikone -->adad
adade-->shoamre indexo mige


.count(character) -->mige chanta dari


3-->tabe ha ham check mikonan yechizio --> True False
are ya na

va in tabe ha hame ba --> is --

.islower()

.isupper()

.isdigit()



'''



name='batman'


name.replace('b','h') #'hatman'

print(name) #batman

new=name.replace('b','h')

name.replace('a','z')
#'bztmzn

name='ali'

name.replace('z','b')


name='ali pilehvar'

name.replace(' ','')
# 'alipilehvar'






print(name) #batman

print(new) #hatman


a='bale'
b=' bale'

print(a==b) #False

print(len(a)) #4
a[0] # 'b'
 

print(len(b)) #5
b[0] # ' '



#gahan to niaz dari space haye samte chap
#va space haye samte raste yek string ro hazf koni


#strip()



b=' bale'

print(len(b)) #5

new=b.strip()

print(len(b))#5

print(new) #bale

print(len(new)) #4

new[0] #'b'
 



name='ali'


name.count('a') #1
name.find('a') #0 -->index 0 -->horofe a 

name[0] # 'a'





name='alipilehvarmeibody'
name.count('a') #2

name.find('a') #0

name.find('p') #3
name[3] #'p'


name='ali'

print(name)

print(type(name))

print(len(name))

#az koja befahmam k name kochike ya boizorg

name.isupper() #False


new=name.upper()

new.isupper() #True
new.islower() # False






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
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
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




#===========================
#===========================
#===========================
#===========================
#===========================
#===========================
#===========================
#===========================
#===========================
#===========================
#===========================
'''
PYTHON ------>


1----------reserved--------------

1.1. python built in function --> 
print() , print( , , )
input() [str] , len() , type()
int() str() float() bool()

narenji-->yek amalkard --> parantez bezani
vorodi daran , kjhoroji daran




1.2.keywords -->
manteghan-->yekseri kar mikone ama besoorate manteghi
logic -->banafsh mishe

mohem trineshoon ---> if 





2---------unreserved--------------
zarfan-->esme zarf
esme zarf -> [1-->adad aval,2-character na _ ,3-case sensetive,4-reserve shdoe ha nmeitoni]

mohtaviaye zarf chi mitone bashe? value

2.1. numbers (2.1.1. int (sahih) ,2.1.2. float , 2.1.3.complex( 3j , 1+4j))
** * / + - %

2.2. Boolean ( True , False)
== != > < >= <= ->javabeshon True False Boolean

2.3.Strings (reshte ha , reshte ee az characte rha)
a= qutation yade nare
a=str(harfe ,....)
type()
len()

bekhay b kcharactersh dastrsi dahste bashi

name=

name[2]  indexe 2vom
*index ha az 0 shoro  mishe --> 0om 1om 2om

slicing
name[2:5] ->az 2 ta 4 yedone done --> 2 3 4


name[start:end+1:step]
#age step=1 -->nanevisish

name[start:end+1]



str functions--->tabe haye mokhtase khgode str
dot mizni 
name.

ina taghir emal nmikonan--> khoroji midan

3 no khoroji daran

1--> convert --> .upper() .lower() .title()
2--> adad pas mide .count() .find()
3--> TRUE FALSE MIDE chekc mikone -0->is  isdigit() islower() iosupper()




'''


#zakhire--> zarf variable =
#namayesh bede ---> print()
#begiure -->input()
#andaze--->len()
#noesh -_> type()






#shoma mikhay sene yek karbar ro azash begiri 

sen=int(input('salam senetoon cheghadre:'))


print('salam khosh amadid usere aziz ba sene', sen)



#----> taraf mige
#agha sene taraf ro begir--> agar balaye 18 bood benevis salam
#age nabood chi? hichi velesh kon


#agar 





#python--> az bala be paeen chap be rast

#migay yeki az khat haye codeto shart (agar )
#agar ok bod bor nabood ejra nkonn in khato

#


sen=int(input('salam senetoon cheghadre:'))

#agar balayue 18 bood inkaro kon -->if
print('salam khosh amadid usere aziz ba sene', sen)


'''

if shart:
    print('khosh amadiddd')
    
    
    
    
    
    
    
salam

s
s
s
s
s
s




if shart:
    print('khosh amadiddd')
    
    
    
shart --> == != > < >= <=

javabesh True False



True ---> oon kaht ro ejra mikone

ag False shod nemikone



'''




sen=int(input('salam senetoon cheghadre:'))


if True:
    print('salam khosh amadid usere aziz ba sene', sen)


if False:
    print('salam khosh amadid usere aziz ba sene', sen)




#to bayad yek shart bezarii k jabvabesh ag true bood ejra mishe
#ag false bod nemishe

sen=int(input('salam senetoon cheghadre:'))

#sen>18

#age trf sensho bala 18 bshe
#sen>18 --> True
#sen>18 --> False



if sen>18:
    print('khosh amadid')



#--------------------
sen=int(input('salam senetoon cheghadre:'))
if sen>18:
    print('khosh amadid')

    
#--------------------------------





'''

TASK 1--> ESMETO BENEVISI
va 6 omin character ro dar bairy


Task2---> az yek karbar senesho begir
bn tavan 2 kon va print kon


TASK3-->
yek string besaz va tabe haye zir ro estefade kon
upper()
lower()
4 ta tabe ye dg



TASK4-->
yek vorodi az karbar begire va beshmore tedade 'a' ro


task5 --> 
az karbaer esmesho begrie ag esmesh
bishtar az 2 ta a dasht print kone bege esme shoma bishtar
 az 2 ta a dare


task6(advanced):
    az fard esmesho begire
    age user esmesho haamsho ba hoorofe bozorg zade bood 
    behesh tabrik bege
    
    
ai.2024.pilehvar@gmail.com


subject --->
L3_name_lname


'''











