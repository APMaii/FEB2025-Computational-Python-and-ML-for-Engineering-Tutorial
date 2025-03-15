#
"""
Created on Wed Mar 12 18:35:42 2025

@author: apm

LL_ADVANCED-----------


"""


#-------------------------------
#PYTHON BUILT IN FUCNTIONS

print()
input()
len()
type()
data=open('desktop/ebm_desk/mydata.csv')

#------------
#https://docs.python.org/3/library/functions.html
#tabe -->khoroji dare

a=abs(-3)

#chnata shart darid

#true true true false

#yek listi az shart ha

#all --> True False
#hameye sharta True bashe --> Truye mide
#age hata yek doone shart false bashe --> False mide



all([True,True,True,True]) #True

all([True,True,True,False]) # False

all([4>2,4>1,5>1,5==5]) #True

all([4>2,4>1,5>1,5!=5]) #False


#---------
#any --> hadeaghal yeki az shart ha age true bashe true mdie
#dar ggheyre insoorat false mdie

any(([True,True,True,True])) # True

any([False,False,False,False]) #False

any([False,False,False,True]) #True




#----------------------------

#10 ta 20 ta shart darid

#if shart and shart and shart and shart and shart:
    
#if all([shart1,shart2,shart3,....])  


#if shart or shart or shart or shart

#if any([shart,shart,shart,....])

#===============================
#casting


int(4.6) # 4
float(4) #4.0
float('4') #4.0

complex()
str()
bool()
list()
set()
tuple()
dict()

a=(10,20,30,40)

#a[2]=60

b=list(a)

#-----------------------
max(10,4,6,7) #10
min(10,4,6,7)

sum([10,20,30,40])

pow(2,3)  #2**3


for i in range(0,10):
    pass

#--------------------


mylist=['ali','vahid','hamid']

for i in mylist:
    print(i)


#done doen ham esmaro bnvisde ham shoamre andi kone

for i in range(0,len(mylist)):
    print(i)
    print(mylist[i])


#-------

for i in enumerate(mylist):
    print(i)
#(0, 'ali')



for i in enumerate(mylist):
    print(i[0])
    
for i in enumerate(mylist):
    print(i[1])
      
    
    
#zip

mylist1=[1000,2000,5000]
myuser=['ali','hamid','reza']



for i in myuser:
    print(i)


#for i in myuser and j in mylist1:
#    print('i',i)
 #   print('j',j)

for i,j in zip(mylist1,myuser):
    print('i:',i)
    print('j:',j)
    

#https://docs.python.org/3/library/functions.html

#------------------------------------
'''
#keywords-->logic
if a>20:
    pass
elif a>40:
    pass
else:
     pass 
#for

#while
and
or

in
is 
    

if user is None:
    print('user vbojod nadarad')


if user is not None:
    print('vojdo darad')

del 

pass
continue
break

def 

#------ketabkhone------
import 
from
as
#---------------------

global

return

#----- print()
False
True
None
'''
#---------

def myfunc():
    return 10

a=myfunc()

a=myfunc()

print(a)


def myfunc():
    #bejaye return
    yield 10
    yield 20
    yield 30
    
a=myfunc()
print(a)

for i in a:
    print(i)

#Khoroji ro bejaye inke yekbar bedii
#chanbar mitoni bndi


#ag chnata khroji dashte bashiii


#chanta vorodi


#eshtebahhhhhhh

def myfunc(a,b):
    
    c=a+b
    d=a*b
    
    
    return c
    return d


def myfunc(a,b):
    c=a+b
    d=a*b
    return c,d



a=myfunc(10,20)
print(a) #(30, 200)

khoroji1,khoroji2=myfunc(10,20)

#@choon dota khorji mdie mitoni dota zarf bzari jolosh


print(khoroji1)

print(khoroji2)

#mahkoomi k tamam ekhrooji hato baham pas bediiii

def myfunc():
    pass
    #......
    #return narmigrde edamaro anjam nmide
    
    
    #.....
    #rffeturn
    
    
#harjae az tabat yiel bzari

def myfunc():
    pass
    
    
    #yield
    
    
    
    #yield
    
    
    #yield
    
    
a=myfunc()


for i in a: 
    pass
    
    #i --> javabaee hast k done doen dade
    
    
#-------------
#a*10


def zarb_dar_dah(a):
    
    b=a*10
    return b



zarb_dar_dah(20) #200


#tabe haye short (klootah)

#lambda ----> tabe ha estefade koni

#vorodi --> a
#khrooji ---> a+ - 


#x = lambda vorodi : khoroji

x= lambda a: a*10


x(20) # 200


zarb_dar_dah=lambda a: a*10
zarb_dar_dah(20)


    
#----------------
#list sakhtan etefagh miofte vaghty for dari


myusers=['ali','reza','hamid','vahid','amir','mohsen']


#harkodom k a dar too esm ro joda konmn brizam too ye liste dg

my_new_List=[]
for i in myusers:
    if i.find('a') != -1:
        my_new_List.append(i)
    
    
my_new_List=[]
for i in myusers:
    if i.count('a')!=0:
        my_new_List.append(i)
    
print(my_new_List)
    
    
#['ali', 'reza', 'hamid', 'vahid', 'amir']

myusers=['ali','reza','hamid','vahid','amir','mohsen']


my_professional=[i for i in myusers if i.count('a')!=0 ]

    
print(my_professional)
    
#['ali', 'reza', 'hamid', 'vahid', 'amir']
    
    
my_professional=(i for i in myusers if i.count('a')!=0 )


#---------------------------------------------
#dictionary 


myusers=['ali','reza','hamid','vahid','amir','mohsen']

current_balance=[10000,22233,454345,344334,54554,53553]

#dictionarey

'''

ali : 443343
vahid : 2424432



'''

#for i in myusers:
    #i list
    
#for i in current_balance:
    #j--



my_final={ i:j   for i,j in zip(myusers,current_balance)   }

print(my_final)


#my_final={    for i,j in zip(myusers,current_balance) if j>20000    }



#---------------------
#https://www.w3schools.com/python/ref_keyword_try.asp



def taghsim(a,b):
    c=a/b 
    return c

#yek tabe hast dar dele 1000 tabe rooye yek sherkat


taghsim(10,2) # 5.0


taghsim(10,0) #ZeroDivisionError: division by zero



#--------------

a=10
b=20

c=a/b

d=a*b

z=float(input('your number:'))



d=100

e=d/z
#sefr nist har errori


print('salam')


print('khob hastin')


print('entekhab kondi price moredee nazar')


#_------1000 khat




#aksaran too real world -_> 1000 tabe darid --> 1000 ta tabe beham peyvastan
#ag ysja yek khat 
#eshtebahi beshe
#kole codetooonaz run miofte

#----

def moshtarian_khososi():
    pass



def moshtariane_mamoli():
    pass


def karmandan():
    pass



#kole kodeto dkahele blcoke try gharar bedi



#try codeto bzar jolom ag try mikonam anjamehs midm
#ag error dad
#error nmiznm balke to taeen kon chikar konm print halo faslesh kon


def send_to_developer():
    #apmaaaa
    #telegram
    pass




try: 
    a=10
    b=20

    c=a/b

    d=a*b

    z=float(input('your number:'))



    d=100

    e=d/z
    #sefr nist har errori


except Exception as e:
    print('errori pish omade')
    send_to_developer()





print('salam')


print('khob hastin')


print('entekhab kondi price moredee nazar')




#----------------------------------------------
#calculation
#moshtari dar tartafid
#

#https://www.w3schools.com/python/ref_keyword_assert.asp


#a=4
#b=y

#NameError: name 'y' is not defined


#Namerror
#typeerror

#Listi ghesmate file ha --> tahe liste zabaan englisi





a=input('agha size nozzle ro vared konid:')

#kamtar az 100 bashe

if float(a)<100:
    print('kochiktar az sad nmibashad')



#-----------
a=input('agha size nozzle ro vared konid:')

#kamtar az 100 bashe

if float(a)<100:
    raise ValueError('Lotfan adade bozorg tar az 100 ro vared konid')

#erdameye code tarafo migiri


#-----

#https://www.tutorialsteacher.com/python/error-types-in-python



#-----------
#age inshdo barnamareo motevaghef kon raise

#+---------------------------------------------------
#class ha

#class object oriented programming COO 

#C---------
#c++ ----------

#print
#printf
#cout

#kheyli jozi 

#tabe ha variable ha hame locl bodan


#-----BANK SYSTEM---------


def welcome():
    print('salam be banke plutus khosh amadid')
    
welcome()   #salam be banke plutus khosh amadid

#-----balance

#-----deposit

#---atm vardarid

balance=0

def deposit(poole_vairizi):
    global balance
    
    balance=balance+poole_vairizi
    
    print('shoma be hesabeton ',poole_vairizi , 'hesab karid')
    
    print('mojodie shoam alan hast : ', balance)
    


deposit(3000)

#shoma be hesabeton  2000 hesab karid
#mojodie shoam alan hast :  2000

def show_balance():
    print(balance)
    
    
show_balance()

#atm 
#transection 
#history 
#......
#too dele har trabe ee nbiam gloabl global

#in zarfaro glohbal konam





#----application ha
#$tabe XXXX Class
#sofgtware 
#csimulation
#ketabkhone
#hooshe masnooe


#class yekchzii has
#k shoma mitoni az delesh obejct bekeshi birooon


# CLASS ------- OBJECT

#CLASS ---> TOO DELESH KOLI TABE DARE




'''
class name:
    variable mziari



'''

class BANK:
    name='ali'
    balance='1000'
    
    
#estefade konm??
    
#yek zarf bsazi va seda bzni classeto --> object 

#shey misazi az yek class


myobject=BANK()

#yek zarf dari myobject -->typesh na str, list, ---> BANK

#TYPE SAKHTI




#a
#b
#mohsen
#ali



myobject.name # 'ali'
myobject.balance #'1000'


'''


class --> yek chzii has


k mitoni object besazi azash
ba dot b mohtaviatesh dastresi peyda koni




mohtaviat ----------

attributers --> variables
methods ---> function 


'''






class BANK:
    name='ali'
    balance='1000'
    
    def welcome():
        print('salam khosh amadid')
       
    def new_func():
        print('hich')
        
        
a1=BANK()      
    
#attributes -->vbaribale .
        
a1.name     #'ali'

a1.balance  #'1000'

#methods ---> fucntion --> ()


a1.welcome() #TypeError: BANK.welcome() takes 0 positional arguments but 1 was given



a2=BANK()
a2.name
a2.balance



#----ina motefavet bashe

#ey kash mese bank name , pole avalie, sen , jensiat 

#BANK() ---> BANK(name,pl)

a1=BANK()

#a1=BANK('ali',30,3000)

#class BANK()

#bank()
#Bank(name,age,current)


class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.current=current
        


a1=BANK()

#TypeError: BANK.__init__() missing 3 required positional arguments: 'name', 'age', and 'current'



a1=BANK('ali',20,2000)

a1.name

a1.age

a1.current

#object sakhti az yekl classs
a2=BANK('vahid',40,0)

a2.name
a2.age
a2.current


#atributesd , methods?


class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.current=current
        
        
    def welcome(self):
        print('salam khosh amadid')

a1=BANK('ali',30,2000)


a2=BANK('vahid',40,323424312)


a1.name
a2.name

a1.age
a2.age


#tabe --> dot ()


a1.welcome() #salam khosh amadid
a2.welcome() #salam khosh amadid


#--------------------------------------------

class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.current=current
        
        
    def welcome(self):
        print('salam khosh amadid aghaye',self.name)


a1=BANK('ali',30,2000)


a2=BANK('vahid',40,323424312)

a1.name
a2.name
#age , crrent

a1.welcome()
#salam khosh amadid aghaye ali

a2.welcome()
#salam khosh amadid aghaye vahid





class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
        
        
    def welcome(self):
        print('salam khosh amadid aghaye',self.name)
        
        
a1=BANK('ali',40,4000)

a1.name
a1.age

a1.current #AttributeError: 'BANK' object has no attribute 'current'

a1.balance # 4000



class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
        
        
    def welcome(self):
        print('salam khosh amadid aghaye',self.name)
        
    def show_balance(self):
        print('mojoodie shoma hast:',self.balance)
        
        
        
        
        
a1=BANK('ali',30,2000)


a2=BANK('vahid',40,323424312)   
        
        
a1.name
a2.name

#---> . ()


a1.welcome() #salam khosh amadid aghaye ali
a2.welcome() #salam khosh amadid aghaye vahid
        
a1.show_balance() #mojoodie shoma hast: 2000
a2.show_balance() #mojoodie shoma hast: 323424312




class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
        
        
    def welcome(self):
        print('salam khosh amadid aghaye',self.name)
        
    def show_balance(self):
        print('mojoodie shoma hast:',self.balance)
        
    def deposit(self,amount):
        
        self.balance = self.balance + amount

        print('Varizie shoma ba mablaghe ', amount , 'ba moafaghhiat najam shod')
        print('mojodie shoma: ', self.balance)



a1=BANK('ali',40,0)

a1.welcome() #salam khosh amadid aghaye ali

a1.show_balance() #mojoodie shoma hast: 0

a1.deposit(4000)

#Varizie shoma ba mablaghe  4000 ba moafaghhiat najam shod
#mojodie shoma:  4000


a1.show_balance()
#mojoodie shoma hast: 4000




#a1


#a1.welcome()


#a1.deposit(4000)       
        


class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
        
        
    def welcome(self):
        print('salam khosh amadid aghaye',self.name)
        
    def show_balance(self):
        print('mojoodie shoma hast:',self.balance)
        
    def deposit(self,amount):
        
        self.balance = self.balance + amount

        print('Varizie shoma ba mablaghe ', amount , 'ba moafaghhiat najam shod')
        print('mojodie shoma: ', self.balance)
        
        
        
    def ATM(self,amount):
        
        self.balance=self.balance - amount
        
        print('varizie hsoma anjam sshod')
        
        print('mojdoie shoma hast : ',self.balance)
       
        
a1=BANK('ali',40,0)



a2=BANK('vahid',50,300000)     
       
        
       
#attributes-->vbaribales ha
a1.name #ali
a2.name #vahid

#Methods 
a1.welcome() #salam khosh amadid aghaye ali
a2.welcome()


a1.show_balance()
       
        
a1.deposit(5000)  
        
a1.show_balance() #mojoodie shoma hast: 5000

a1.ATM(2000)
        
a1.show_balance()
        

a2.name

a2.show_balance()  #mojoodie shoma hast: 300000

a2.ATM(20000)
       
        
a2.ATM(278000)

a2.show_balance()
       
a2.ATM(5000)        
       
        
#-------------------------------
#-------REAL WORLD-----------

class BANK:
    
    #vorodi haee k object mikahd sakhte beshe ro inja migi chia mikhad
    

    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
        
        
    def welcome(self):
        print('salam khosh amadid aghaye',self.name)
        
        
    def show_balance(self):
        if self.balance > 500:
            self.balance=self.balance - 500
            
            print('mojoodie shoma hast:',self.balance)
            
        else:
            print('shoma mojoodie moshahede mojodi ham nadarid')
            
        
    def deposit(self,amount):
        
        self.balance = self.balance + amount

        print('Varizie shoma ba mablaghe ', amount , 'ba moafaghhiat najam shod')
        print('mojodie shoma: ', self.balance)
        
        
        
    def ATM(self,amount):
        if amount < self.balance:
            self.balance=self.balance - amount
            
            print('varizie hsoma anjam sshod')
            
            print('mojdoie shoma hast : ',self.balance)
            
        else:
            print('mojoodie shoma kafi nist')
       

a1=BANK('ali',100)
a1=BANK('ali',40,4000)


a1.name


a1.show_balance() #mojoodie shoma hast: 3500

a1.ATM(1000)

a1.show_balance() #mojoodie shoma hast: 2000
       
        
a1.ATM(2100)
#mojoodie shoma kafi nist




#yek class
#atributes 
#functions 



#yek class jadid besazi k function haye ghabvli ham dashte bashe

#inhrettence --> ERS BARI az clas ghabli



class BANK:
    
    
    def __init__(self,name,age,current):
        pass
    
    def welcome(self):
        pass
    
    #......
    
    

#nobitex ---> bank haye ramz arz

#banki besazam k shoma biay too banke man
#poleto b dollar bzni b felan bzni


class CRYPTO_BANK:
    
    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
#----

a1=CRYPTO_BANK('ali',40,0)

a1.name

a1.welcome()

#AttributeError: 'CRYPTO_BANK' object has no attribute 'welcome'


#BANK ---> TABE HA RO DARE
#CRYPTO NADARE



#NIAZ DARID YEK CLAS JADID BESAZID K TABE HAYE GHABLIO DAHST EBASHE 

class CRYPTO_BANK:
    
    def __init__(self,name,age,current):
        self.name=name
        self.age=age
        self.balance=current
        
        
#cypro bank yek clasi hast k ers borde tabe hay eclas bank ro
class CRYPTO_BANK(BANK):
    #vorodi haye injat hamoon vorodi haye class bank 
    
    def __init__(self,name,age,current):
    #def __init__(self,name,age,current,cypro_id)
        super().__init__(name,age,current)
        
        
    

a1=CRYPTO_BANK('ali',40,4000)


a1.welcome() #salam khosh amadid aghaye ali

a1.show_balance() #mojoodie shoma hast: 3500

       




class CRYPTO_BANK(BANK):
    #vorodi haye injat hamoon vorodi haye class bank 
    
    def __init__(self,name,age,current,crypto_id):
        super().__init__(name,age,current)
        
        self.crypto_id=crypto_id
        
        
        
    def welcome_english(self):
        print('hello welcoem to our crypto bank ,m this is way to the future')
        

n1=BANK('ali',40,4000)
n1.crypto_id

n1.welcome()
n1.welcome_english()


    
a1=CRYPTO_BANK('ali',40,4000,1234)
a1.name
a1.crypto_id
a1.welcome_english() #hello welcoem to our crypto bank ,m this is way to the future

a1.welcome()



class CRYPTO_BANK(BANK):
    #vorodi haye injat hamoon vorodi haye class bank 
    
    def __init__(self,name,age,current,crypto_id):
        super().__init__(name,age,current)
        
        self.crypto_id=crypto_id
        self.crypto_balance=0
        
        
        
    def welcome_english(self):
        print('hello welcoem to our crypto bank ,m this is way to the future')
        

    def exchange(self,amount):
        
        self.balance=self.balance-amount
        
        dollar_amount=amount /90000
        
        self.crypto_balance=self.crypto_balance + dollar_amount
        
        print('ba moafaghiat anjam shod')
        
        print('hesabe rialie shoma:', self.balance)
        
        print('hesabe arzie shoma:', self.crypto_balance)
        
        
    def show_balance_arzi(self):
        
        print('hesabe arzie shoma:', self.crypto_balance)
        
        
a1=CRYPTO_BANK('ali', 40,400000,1234)    

a1.name
a1.age
a1.balance

a1.crypto_id

a1.welcome() #salam khosh amadid aghaye ali

a1.show_balance() #mojoodie shoma hast: 399500

a1.deposit(500) #Varizie shoma ba mablaghe  500 ba moafaghhiat najam shod
#mojodie shoma:  400000


a1.welcome_english()

a1.exchange(100000)




#---------------------------------------


