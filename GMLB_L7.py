
"""
In The Name Of God

Created on Wed Mar  5 15:36:24 2025

@author: apm



-------L7---------------

1---6 ----> Python basic --> anaconda, IDE, python variables,
python built in functions, ......
logic (keywords) --> if , else, for , while


7---> Def (function )

8--> Class

9--> Libraries (numpy , scipy) , numerical modeling

AI




---------------
L1_name_lname

Quiz telegram 



3 ta Project (phoroze ejbari)--> MADRAK Gamlab

Project1--> (A1) ---> 20% emroz khedmateton gofte mishe deadline hafteye ayande jome
Project2--->(A2) ---> 30%
Project3---> (A3) ---> 50%

-----------------






"""




#------------------
#------RESERVED--------------

#-----KEYWORDS--------------


#---------SHARTI-------------

#--------JUST IF-----------

sen=int(input('senetoon cheghadre?:'))

if sen>20:
    print('salam')
    
'''

just if--> agar , ....

if shart:
    dastoor(s)
    
    

dorahie
if shart:
    dastoor(s)
    
else:
    dastoor(s)




dorahi dar dorahi
if shart:
    dastoor(s)
elif shart:
    dastoor(s)
else:
    dastoor(s)
    
    
shart--> Javabesh True False
> < == !=
functions --.str functin isdigit isupper

'''


#-------Halghe ha shodim--------

#-----for ha hastan

#-----while


#ideye asli baraye halge ha tekrar hast-->
#tekjrar-->for , while joftesh tekrar ro anjam mide
#ama be raveshe khase khdoesh




#-------FOR----------------------

'''
shomarande --> i ,.....

for i in mahdoode:
    dastoor (dastoors)
    
    
i , j , k , item ,.....

mahdoode--> iterable

iterable--> list, i ro mizare elemenash , set , tuple , dictionary
reshte --> listi az character h hast
range() --> adad miksaze





'''


#numbs=[1,2,3,4,5,6,7,8,9,....,100]
#for i in numbs:


for i in range(0,101):
    print(i)



#dtooye dastor ya az i estefade mikoni ya na

#python az shoamrande estefade mikone k betone tekrar kone
#k b ezaye an dastooor ro anjam bde
#dastoor-->mohasebe
#print
#print static 
#print dynamic (ba esefade az shoamrande)




for i in range(0,101):
    print(i)

#0 ta 101 chanta chanta?


#start --> 0 , 2 ,3 ,
#end+1 --> (0,100) -->akahrio shamel nmsihe 100 shamel nmishe

#az start ta end chanta chanta bere

#(start,end+1,step)



for i in range(0,101,1):
    print(i)

for i in range(0,101):
    print(i)


#range(0,101) --> (0,101,1)

#dota dota boro

for i in range(0,101,2):
    print(i)

#0 2 4 6 8 ,......


for i in range(0,10):
    print(i)

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

for i in range(0,10,1):
    print(i)
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

for i in range(0,10,2):
    print(i)

'''
0
2
4
6
8
'''

for i in range(0,10,2):
    print('salam')

'''
salam
salam
salam
salam
salam

'''

#----for , if 

#---->iteration

mylist=['ali','reza','vahid','hamid']

    
for i in mylist:
    print(i)

'''ali
reza
vahid
hamid
'''

mylist=['ali','reza','vahid','hamid']

    
for i in mylist:
    print('salam')

'''
salam
salam
salam
salam

'''





#iteration --> print
#ballcke yeseri shroot ero check koni---> if if else ,...


mylist=[10,11,12,13,16,18,24,25,23,27,30,39,38]

for i in mylist:
    print(i)

count=0
new_list=[]
#mikham check konm chanta adad bozorgtar az 20 hast?

#be ezaye har i ii ke dar mylist vojod darad
for i in mylist:
    #check kon ke .....
    if i>20:
        #print(i)
        #count=count+1
        new_list.append(i)


print(count) #7

print(new_list) #[24, 25, 23, 27, 30, 39, 38]
    



#----for , if ---> iteration***
#print
#shomrodane
#joda kardan

#--->

'''


pass---> felan boro 

halghe --> tekrar , halghe micharkhi too har charkhesh 

continue--> ignore kon , skip , bepar
break---> beshkoon, ghat kon 

banafash

'''


for i in mylist:
    pass
    
    




a=10
b=a+2




for i in range(0,10):
    print(i)



for i in range(0,10):
    if i==5:
        continue
    
    print(i)


'''

i=0 --> if i==5 XX fakls- , print(i) -->0
i=1
i=2
i=3
i=4   
i=5 --> if i==5 True , continue -->hcihkar nmikone
i=6 ---> 6
i=9 ---> 9

0 ---4,6,--->9



'''

'''
0
1
2
3
4
6
7
8
9

'''


myusers=['ali','vahid','hamid','reza']

#esme hamaro print kon joz alio


for i in myusers:
    if i=='vahid' or i=='reza' or i=='hamid':
        print(i)


for i in myusers:
    if i=='ali':
        continue
    
    print(i)

'''
vahid
hamid
reza

'''



for i in range(0,10):
    print(i)


for i in range(0,10):
    if i==5:
        break
    
    print(i)




'''
i=0 --> false --> 0
i=1
i=2
i=3
i=4
i=5 -->true ->break naro badi , beshkon bai biron az halghe
i=6 xxx nMISHE


'''

'''
0
1
2
3
4

'''

#----------------------------------------

#tekrar

print('salam')


#halghe ---> for , while


#for -->tekrar  , iteration ( for i in mahdoode)
#while --> tekrar


#**in mahdode mitone yek list bashe , yek reshte, range,....

#while-->man fargh mikonam
#manam tekrar anajm midm halgeh am ama

#mahdoode --> [start , step,  end]

#mylist=[ali,vahid,reza]



#while--->



#be man ye shart bde

#beman ye shart bde man ta zamani k in shart True hast
#anjam mdiam dastooreto
#false beshe miam biron


#entehaye fix 
#entehash ba y shartee


i=0

#ta zamani k i e man koochiktar az 7 hast 
#print kon --> salam 
#while i<7:
#    print('salam')


#i-->0

#while -->badane dare

#ta zamani k i<7 hast man slaam ro print mikone


'''


while shart:
    dastooor
    
'''


#while True:
#    print('salam')


#shart bzari , ta zamhni k shart baragahrare anajm mide



sen=18

#while sen<20:
#    print('salam')



'''

while-->tooye python neveshte practical





'''


i=0
while i<7:
    print('salam')


'''

i=0 

aya i<7 --> True --> salam
#i nmire bala

***for i ro khdoesh mibord bala

for  i in mahdoode  

i=0
while i<7:
    print('salam')


i=0 --> i<7 true print(salam)
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')

i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
i=0 -->i<7 true print('salam')
,........
d
dar che soorati ejra nmiseh?
dasr soorati ke shart -0-> false bshe

i=7
'''

i=0
while i<7:
    print('salam')
    i=i+1


'''

i=0
i<7 ---> True --> salam , i=0+1=1
i=1 -->i<7 -->True --> salam, i=1+1=2
i=2 -->i<7 -->True --> salam , i=2+1=3
i=3
i=4
i=5
i=6 --->i<7 ---> True --> salam , i=6+1=7
i=7 --> i<7-->fasle  az halgeh maid biroon






'''

#i=7
#i<7 # False
#i<=7 #True



i=0
while i<7:
    print('salam')
    i=i+1

'''
salam
salam
salam
salam
salam
salam
salam

i bokone toye mahdode 


i az aval tarif mikone
shart mizare mige ta inja
ekhtetami 


'''


i=0

while i<7:
    print('salam')
    i=i+1
    


#------------------

i=0
while i<7:
    print(i)
    i=i+1
    

'''
0
1
2
3
4
5
6

i=0
while i<7:
    print(i)
    i=i+1
    

for i in range(0,7,1):
    print(i)
    
'''


#bi shoroooo
#bi ebteda


i=9
while i<7:
    print(i)
    i=i+1
    
    
    

#i ro tarif konid

while i<7:
    print(i)
    i=i+1

#NameError: name 'i' is not defined


#1--> i ro defined kon
#shart ro satisfy --> True -->varede halgeh beshe


i=0
while i>7:
    print(i)
    i=i+1



#i=0
#while i<7:
 #   print(i)





'''
while--->

1*
i= tarif konid satrt

2*
while shart
shart b goone ee bashe ke i varedesh she True


3* dastooor

4** tooye dastooreton sharte ekhtetam bzarid
i=i+1


'''

mylist=[10,20,30,40,50,60]

i=0
while i<len(mylist):
    
    if mylist[i]>20:
        print(mylist[i])
    
    i=i+1



#iteration -->for
for i in mylist:
    if i>20:
        print(i)






#---tosie nemishe
mylist=[10,20,30,40,50,60]
for i in mylist:
    if i>20:
        print(i)
        
'''
i

30
40
50
60


ali 
vahid
reza

'''

mylist=[10,20,30,40,50,60]

#i ro bezar be ezaye idnex haye in list
#i --> 0 1 2 3 4 5 
#myslit->10,20,30
#ali vahid
#ali 100 240


for i in range(0,len(mylist)):
    print(i)
    

'''
0
1
2
3
4
5
'''

#i -->elementaye list
for i in mylist:
    if i>20:
        print(i)
        
        
        
mylist=[10,20,30,40,50,60]
    
for i in range(0,len(mylist)):
    #check konm
    #i-->0 1 2 3 4 5
    #elemenete on list bzoorgtar az 2
    if mylist[i]>20:
        print('salam')
    


'''

myslist=10,20,30,40,50,60 --> 6 yta ozfg dare
len(mylist)-->6

for i in range(0,6)

i--> 0 1 2 3 4 5

i=0 --> mylist[0] 10 >20 -->false 
i=1 mylist[1] 20 >20 -->false
i=2  myslist[2] 30>20 -->treue
print (salam)

'''




#-----iteration

#sade tarin halat ba fore

for i in mylist:
    if i>20:
        print(i)
        #count=count+1
        #new_list.append
        #continue
        #break
    #else
    #elif
    
    

for i in range(0,len(mylist)):
    
    #****
    #bejaye i
    #chon i dg oon element nis balke indexese
    #i-->0 1 2 3 4 5
    
    if mylist[i]>30:
        pass
    
    


#-------------------------------------

#man yad grftm shabieh for estefade konm

'''


for i in range(start,end+1,step):
    dastooor(s)
    
    
    
i=start
while i<end+1:
    dastooor(s)
    dastoor
    dastooor
    i=i+step





#man asan kari b i ndrmmmmm
aya bdone i ham msihe while nvsht?--> bale

while true


'''


while True:
    print('salam')

#halgheye binahyatii
#endless loop 
#ta abad salam ro print mikone

#khateme --> yek chzii dakhele halgeh mzirn i=i+1
#k shart ro naghs koen k estop she

#alan man chijori mitonm yejori

#shart k inja hamsihe True
#stopesh konam???


#while True:
#    print('salam')
    
    #break
    
    

    
#agha y barnam ebenevsi

#uswere karbaro begir
#passwordesho bgir
#confirm password ham begir
#ag yeksan bod k hich bgo sabt shd
#ag nabodo dobare pasword begire


print('------LOGIN PAGE-----------')
username=input('USERNAME :')

password=input('Password:')

confirm_password=input('Confirm Password:')

if password==confirm_password:
    print('sabt shod ')

else:
    print('sabt nashod')



#------------------
print('------LOGIN PAGE-----------')
username=input('USERNAME :')

password=input('Password:')

confirm_password=input('Confirm Password:')

if password==confirm_password:
    print('sabt shod ')

else:
    print('mtasefane passwordaton yeki nist dobare bezanid')
    
    password=input('Password:')
    confirm_password=input('Confirm Password:')
    
    if password==confirm_password:
        print('sabt shod')
        
    else: 
        pass
        #........
        



'''

az user username begire
azash password begir
confirm password begir

ta zamaniiii k passwordo confirm password yeki nabod
hey azash password begir



'''



print('------LOGIN PAGE-----------')
username=input('USERNAME :')

while True:
    password=input('Password:')
    confirm_password=input('Confirm Password:')
    
    if password==confirm_password:
        break
    else:
        print('passworde shoam ghalate mojadad benevisid')


sen=input('age:')




for i in range(0,10):
    for j in range(0,10):
        print(i,j)

'''
i-->0 j-->0  print(0,0) -->0,0
      j-->1
      j->2
      j-->3
      ...
      j-->9 -->print(0,9 ) -->0,9
      

i-->1





'''






'''


if --> just if (yekio gir biarid)
if else--->dorahi
if elif else-->roahi dar dorahi

for --> i , harchizi in mahdoode -->lyst, iterable, str , ..
range(start,end+1,step) , dastoooor

for i in range(0,10):
    print(i)
    
    
for --> tekrar + Iteration --> If , if else, ....
count, new_list.append, break, continue

for for 


while-->tekrar

i=start
while i<end+1:
    dstooor
    i=i+step
    
    
raveshe dovom ta abad yechi anajm she magar inke

while True --> if , break



while True:
    
    ...
    ..
    ...
    
    if ...:
        break
    





'''


'''

psudo code--->shebhe code

yek gehsmati too dar too

'''


'''

capsule doros mikonan



psudo bakhsi az code yek kari mikone

BOX harmoghe naiz bod sedashon konim

'''



code=input('code:')
name=input('name:')

#check konam trf adad zade


while True:
    
    price=input('price:')
    
    if price.isdigit():
        
        my_list=[]
        
        for digit in price:
            
            if digit=='۰':
                my_list.append('0')
                
            elif digit=='۱':
                my_list.append('1')
                
            elif digit=='۲':
                my_list.append('2')
                
            elif digit=='۳':
                my_list.append('3')
                
            elif digit=='۴':
                my_list.append('4')
                
            elif digit=='۵':
                my_list.append('5')
                
            elif digit=='۶':
                my_list.append('6')
                
            elif digit=='۷':
                my_list.append('7')
                
            elif digit=='۸':
                my_list.append('8')
                
            elif digit=='۹':
                my_list.append('9')
              
        if my_list==[]:
            new_price=float(price)
            
        else:
            khali=''
            new_price=khali.join(my_list)
            new_price=float(new_price)
            break
        
    
    print('adad vared namaeed')
    
    


text=f"""

management---------

producc code : {code}
product name: {name}


    TOTAL PRICE: {new_price}


CO. 2024
-----


"""

print(text)




#-----

#-------


telephone_number=input('lotfan shoamraton ro bezanid')



if telephone_number.isdigi():
    
    for digit in telephone_number:
        my_list=[]
        
        if digit=='۰':
            my_list.append('0')
        #......
            


#niaz darm k telehgone number -->farsi zad
#englisi konm

#shoamrasho + 1000 samane hast nis
#...






'''

yek safe khali --> product_management_amazon.py

code,name,price, .... , sabt kone , size, rang,...
confirm nahaee--> sabt shdo

100 khat
20 khat 

telephone number-->
address

confirm-> bale

bere roo website etelaat ro ersal kone


etelat_ersal(informations)


'''







'''


1--->kheyli vaghta yeseri kararo shoam dar toole
koel codeton bishtar az 1 bar niaz darid
shayad bgm 100 bar

adad farsi --> adad englisi 

shoamras , price ,..

yechi bood

new_price=persian_to_english(price)

new_phone_number=persian_to_english(phone_number)




input ----> BOX ---->khorojii



output=emse_box(input)


BOX--> amalkardi --> function (Tabe)


Tabe--> BOXI az code bbin k vorodi dar ekhoorji



'''



first_numb=float(input('adade avaleto begoo:'))

second_numb=float(input('adade dovom:'))

amalgar=input('amaliate morede nazar (jam,tafrigh,zarb,taghsim):')


'''
if amalgar=='jam':
    c=first_numb+second_numb
    print('your answer is ',c)

if amalgar=='tafrigh':
    c=first_num-second_numb
    print('your answer is ',c)

'''


first_numb=float(input('adade avaleto begoo:'))

second_numb=float(input('adade dovom:'))

amalgar=input('amaliate morede nazar (jam,tafrigh,zarb,taghsim):')


if amalgar=='jam':
    c=first_numb+second_numb
    print('your answer is ',c)

elif amalgar=='tafrigh':
    c=first_numb-second_numb
    print('your answer is ',c)

elif amalgar=='zarb':
    c=first_numb*second_numb
    print('your answer is ',c)


elif amalgar=='taghsim':
    c=first_numb/second_numb
    print('your answer is ',c)






'''

box

vorodii ---> box -->khrooji bgiri


consoel , input ,...
hamedhci too editore


#esm ghavaninesh mese esme zarfas


def esm(vorodii):
    badaneye tabe hast




calculartor 



-----> BOX --->



vorodi --->(adad1,adad2,amalgar) ---.BOX --> khroojimon miudad

'''


def calculator(adad1,adad2,amalgar):

    if amalgar=='jam':
        print(adad1+adad2)
        
    elif amalgar=='tafrigh':
        print(adad1-adad2)





#hich etefaghi nmiofte 

#a=2

#calculator --> skahtari

#calculator



#sedash bezani

calculator(10,20,'jam')






'''

miad mikhoen b parantez mirese mifahme yek tabas

mire bala va mibine bayad vojod dashte bashe
!**--.tabe ro baayd aval tarif kard bad seda krd (call)

#miad mibien chanta vorodi migire va vefgh mide
#vorodi hato migire



'''










#---------4 no tabe darim---------
'''


Define function

Call 



Hadaf ey kash y box bodo 
vorodi midadi khrooji migrftim

sedash mirkdi 


input ---> BOX ---> Khoroji






1-Input
2-->calculation (body)
3--->output

#calculation

'''


#------------------------------------------------
#1---> tabe ee ke  vorodi dre ama khrooji ndre


#jam

def jam(a,b):
    
    c=a+b
    print(c)



jam(30,50)


#vorodi ? ---> a , b --> 30 , 50
#khoroji??


zarf=jam(30,50)

print(zarf) #None



#2-->ham vroodi ham khoroji

def jam(a,b):
    c=a+b
    return c

zarf=jam(20,30)



def jam(a,b):
    c=a+b
    print(c)
    return c

zarf=jam(40,30)



#3------>
#_--tabe ee mitone vorodi nadashte bashe khrooji dahste bashe?

def pi():
    return 3.14


zarf=pi()


#def pi():
    




#4-->na vorodi na khoroji


def welcome():
    print('salam khosh amadid')
    
    
    

zarf=welcome()
    
    
    

#----------------------------------------

'''


def --> adade farsi--> BOX _--->ADADE KHAREJI



box --> persian_digit_to_english

adad ---> persian_digit_to_english --> adad


vorodi , khoroji



'''

def persian_digit_to_english(persian_numb):
    my_list=[]
    
    for digit in persian_numb:
        
        if digit=='۰':
            my_list.append('0')
            
        elif digit=='۱':
            my_list.append('1')
            
        elif digit=='۲':
            my_list.append('2')
            
        elif digit=='۳':
            my_list.append('3')
            
        elif digit=='۴':
            my_list.append('4')
            
        elif digit=='۵':
            my_list.append('5')
            
        elif digit=='۶':
            my_list.append('6')
            
        elif digit=='۷':
            my_list.append('7')
            
        elif digit=='۸':
            my_list.append('8')
            
        elif digit=='۹':
            my_list.append('9')



    khali=''
    new_price=khali.join(my_list)
    new_price=float(new_price)
    
    #print....
    return new_price
        
    





code=input('code:')
name=input('name:')
#check konam trf adad zade
price=input('price:')

new_price=persian_digit_to_english(price)
    
print(new_price)


#-----
telephone_number=input('shomarato begoo:')

new_number=persian_digit_to_english(telephone_number)

print(new_number)








'''

L7--------------------------
yekshanbe -0--->Proje





task1--->
ba while 1 ta 100 ro chap kone

ba while 1 ta 100 2 ta 2 ta chap kone


task2--->
code , name , price , 

confirm kon (aya taed mikoni? yes/no)
yes-->sabt shod

ta zamani k karbar yes nazade ---> hey azash coded , name , price jadid begire



task3-->
password ro ** ba while bezanid



task4--> 
machine hesab ro b soorate fucntioni bnvsidi k
vorodi dqshte abshe khoroji ndshte bashe 

task5--->
machine hesab ro b sorati k vorodi begire va khorji ham dashte bashe






TASK6--->
yek function benevisid ke dota string behesh bedid
age stringe avali dakhele stringe dovomi bashe , hazfesh kone bargardoonatesh

age nabashe, stringe avalio be avalo tahesh bechasboone badesh bargardoone



TASK7---->

yek fucntion benevisid yek list begire , bad age list tekrari dasht
tedade tekrariash ro bargardoone

age nadasht adade -1 ro bargardoone



'''



















