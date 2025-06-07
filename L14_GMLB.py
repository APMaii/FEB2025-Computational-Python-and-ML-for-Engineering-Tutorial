
"""
In The Name of GOD

Created on Sun Apr 13 18:04:20 2025

@author: apm


------L14---------

Python fundemental
Funcrtions
Class

----Libraries
math
datetime
numpy ---> array() instead of list()
scipy --> [Advanced ODE , PDE]
sympy 

matplotlib
matplotlib.pyplot ---> Rasm


Pandas ---> dataframe, data manupulation , working iwth data

edameye in jalase --> jalaseye charshanbe +
github ro khedmateton yad midm
+ ODE , ..... moonde
------
Introduction of AI + ML


Project2 --> Pandas, matplotlib , numpy
30%



"""

#---------LIST--------------

a=[10,20,30,40,50,60]

a[1] #20

a[1]=400

print(a) #[10,400,....]

a.append(400)
a.insert(5,30)
a.pop(2)
a.remove(400)

#set (tekrari nmigrft) {10,20,304}
#tuple --> (10,20,30)
#dictionary {keys : values}
#index --> keys


#---------Numpy Array----------
import numpy as np

b=np.array([10,20,30,40,50,60])

b[1]

b[1]=400

#.append

#kheyli ghavi tari dahst
b.max() #60

b.sum() #210

b.mean()


#do bodi besazi

c=np.array([ [10,20,30] , [40,50,60] ,[70,80,90]  ])
#radif , sotoon
c.ndim #2  -> ham radif , sotoon

c.shape #(3, 3)  (radif, sotoon)

#c[radif,soton]

c[1,2] #60

c[1,2]=10000


c[:,2] #sotgone 2 koel radif ha

c[1,:] #radife 1 taamme soton ha

c.max() #10000

c.max(axis=0) # array([   70,    80, 10000])

c.max(axis=1) #array([   30, 10000,    90])



#agar yek data dashte basham 
#chijori biam biaramehs too python

#shoma omdi rajebe .txt --> open()
#ama in tab eb darde man nmikhore

#file.read() .write()

#numpy???? moshkele 1 

#-----data azmayeshgah --> vared koni ???

#----> man mikham mesle tamame data ha

#dar vahele ye aval soton ha nam gzoari shode bashan ,d ar vahleye dovom radif ha

'''
List --> default  , fast nsi, 2D nist
Numpy --> numpy.array --> computation , fast (c/c++) ,2d,3d,4d 
moshkelat --> data mikham vared konm az birone spyder / mikham sotonam ya radifdam esm dahste bashan (label)
pandas --> dataye shoam ro btone csv, xlsx , import koni , betone radifo sotonet label dashte bashad , (na b paye numpy nemirese)

*** list --> numpy --> pandas

data.xlx --> pandas --> numpy computation --> pandas



CLASS-------------
python.list()
numpy.array()
pandas.Series() #S bozorg #1D
pandas.DataFrame() #D , F bozorg ##2D



pandas step before ML
raw data -> working, manupulation , Cleaning, preprocessing

--> final data --> it is prepared for training (ML workflow)


'''

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


#Series

s= pd.Series([10,20,30,40,50,60])

print(s)

'''
0    10
1    20
2    30
3    40
4    50
5    60
dtype: int64

'''
print(type(a)) #<class 'list'>
print(type(b)) #<class 'numpy.ndarray'>
print(type(s)) #<class 'pandas.core.series.Series'>

#az tabehaye numpy estefade koni


s[0] #10

s[2] #30



np.exp(s)
'''
0    2.202647e+04
1    4.851652e+08
2    1.068647e+13
3    2.353853e+17
4    5.184706e+21
5    1.142007e+26
dtype: float64
'''

np.sin(s)
'''
0   -0.544021
1    0.912945
2   -0.988032
3    0.745113
4   -0.262375
5   -0.304811
dtype: float64

'''


zarf= s +1000
'''
0    1010
1    1020
2    1030
3    1040
4    1050
5    1060
dtype: int64

'''


s*2
'''
0     20
1     40
2     60
3     80
4    100
5    120
dtype: int64

'''


'''
a+2
a*100
a.10
a**2
a//10 --> 
a/10
'''


#alaeme condition
s <0
'''
0    False
1    False
2    False
3    False
4    False
5    False
dtype: bool
'''

s<1000

'''
0    True
1    True
2    True
3    True
4    True
5    True
dtype: bool
'''

s<30
'''
0     True
1     True
2    False
3    False
4    False
5    False
dtype: bool
'''





s= pd.Series([10,20,30,40,50,60])

#numpy --> series
myarray=np.array([10,20,30])
s1=pd.Series(myarray)




#dictrionary --> Series

weights = {'alice': 68 , 'bob':70,'colin':80}


s3=pd.Series(weights)

#bejaye 0 ,  1 , 2 --> idnexe man esme

s3[0] #68

s3['alice'] #68

weights['alice'] #68

#bejaye idnex ---> keys



s4=pd.Series([68,70,81])

s4[0] # np.int64(68)




s5=pd.Series([68,70,81],index=['alice','bob','colin'])

s5['alice']


s5['bob']=100

print(s5)

'''
alice     68
bob      100
colin     81
dtype: int64

'''


#---------INDEX---------

s5=pd.Series([68,70,81],index=['alice','bob','colin'])

s5[0] #68
s5['alice'] #68
 

#loc , iloc

#loc--> esm begoo , iloc --> index

s5.loc['alice'] #68
s5.loc[0] #KeyError


s5.iloc[0] #68
s5.iloc['alice'] #TypeError: Cannot index by location index with a non-integer key



s5[0:2]
'''
alice     68
bob      100
dtype: int64

'''



s5.iloc[0:2]
'''
alice     68
bob      100
dtype: int64
'''

s5.loc[['alice','bob']]
'''
alice     68
bob      100
dtype: int64
'''


#Kilidvazhe hat chie


s5.keys() #Index(['alice', 'bob', 'colin'], dtype='object')


#---dictionary ro yad grfrti serie ro yad grfti

s5 +10

s5.add(10)

s2=pd.Series([10,20,30,40,50,60])

s2.abs()
s2.add()
s2.div()
s2.divide() #similar
s2.divmod() #integer
s2.multiply() #*
s2.mul()
s2.pow()

s2.pop() #remove
s2.clip()  #thresholding

s2.all()
s2.any()
s2.max()
s2.min()
s2.argmax()
s2.argmin()
s2.astype() #dtype int --> float
zarf=s2.view() 
zarf=s2.copy() #deep copy hichgone taghiri rosh nmiofte

s2.keys()
s2.items() #for i,j in 



'''
pip install pandas
https://pypi.org/project/pandas/

tutorials
https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html


documentation
https://pandas.pydata.org/docs/user_guide/10min.html

source code
https://github.com/pandas-dev/pandas




'''
#-------2D-------------------------
#_------DATA FRAMES---------------

'''
pd.series()


chanta series ro roo ham ebzarim

ye jadval --> DataFrame


'''

simple_dict={
    'model':'bmw',
    'year':1990,
    'name':'ali'}


simple_dict2={
    'model':['bmw','benz'],
    'year':[1990,1998],
    'name':['ali','vahid']}


people_dict = {
    "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
    "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
    "children": pd.Series([0, 3], index=["charles", "bob"]),
    "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
}

print(type(people_dict)) #<class 'dict'>


people= pd.DataFrame(people_dict)

#data frame sakhtam

print(type(people))
#<class 'pandas.core.frame.DataFrame'>



#-----in bala --> idea 


#dar vagehiat kh sade o rhaat mishe yek dataframe sakht


'''

yade yek np.array 2 D bioft


chanta rdif, chanta soton

'''



b2=np.array([ [10,20,30] , [40,50,60]   ])

d2=pd.DataFrame([ [10,20,30],[40,50,60] ])

#hata mitoni aval arrya bsazi bdad dataframe

d3=pd.DataFrame(b2)



#harchi benevisi --> b column ha mirese
#pandas data frame --> COLUMN KH MOHEME

data=pd.DataFrame([ [10,20,30],[40,50,60] ])

data[0]
'''
0    10
1    40
Name: 0, dtype: int64

'''



#numpy.array?


array=np.array([[10,20,30],[40,50,60]])

#column = [ esm] , index =[]

data=pd.DataFrame([ [10,20,30],[40,50,60] ],columns=['feshar','dama','estehkam'] )


data=pd.DataFrame([ [10,20,30],[40,50,60] ],index=['case1','case2'] )


data=pd.DataFrame([ [10,20,30],[40,50,60] ],index=['case1','case2'] ,columns=['feshar','dama','estehkam'] )



#---datahye azmayeshgah aksaran fght sootn nam gzoari shdozan
data=pd.DataFrame([ [10,20,30],[40,50,60] ],columns=['feshar','dama','estehkam'] )


#dastrsiii
#b columns --> DATAFRAME --> COLUMNNNNNN

data['feshar']
'''
0    10
1    40
Name: feshar, dtype: int64

'''


zarf=data['feshar']


#chanat soton [  []  ]

data['feshar','dama'] #in ghalate

data[ ['feshar','dama']]

'''
   feshar  dama
0      10    20
1      40    50
'''

#********
#--------ACCESS------------
#inaro too ye yekj zarf zakhire koni easyyyy
data=pd.DataFrame([ [10,20,30],[40,50,60] ],index=['case1','case2'] ,columns=['feshar','dama','estehkam'] )



#zmaani k shoma soton haro bekhaye
data['feshar'] #SOTYONE FESHARO MDIE
data['dama']
data[ ['feshar','dama']]


#zamni k shoma radif haro bekhayyyyyyy
#case 1 --> radif

data['case1'] #eroorr mide

#loc.  iloc
#iloc --> indexi
#loc --> esmesho bdi

data.loc['case1']
'''
feshar      10
dama        20
estehkam    30
Name: case1, dtype: int64
'''

data.iloc[0]
'''
feshar      10
dama        20
estehkam    30
Name: case1, dtype: int64

'''




#fereftan yek column ya yek radif


#hata mitone shoma #yek value begiri


#radice case1 , fehsarsho mikham
#bar khalafe numpy k aval radif, sdoton
#inaj soton , radif

data['feshar'].loc['case1'] #10



#manually

# 4 nmafar hasrtan 
#sale tavalod, tedade bache  sargarmi, weight

#********************
#numpy array --> int, float, stre , object

my_array=np.array([
    
    [1985,1,'biking',68],
    [1984,3,'dancing',83],
    [1992,0,'football',70]

    ])



my_array2=[
    
    [1985,1,'biking',68],
    [1984,3,'dancing',83],
    [1992,0,'football',70]

    ]




df=pd.DataFrame(my_array2,columns= ['birthday','children','hobby','weight'], index=['alice','bob','charles'])


#df=pd.DataFrame([ [1985,1,'biking',68],[],[]      ],columns= ['birthday','children','hobby','weight'], index=['alice','bob','charles'])



df['birthday']
'''
alice      1985
bob        1984
charles    1992
Name: birthday, dtype: int64
'''

df.loc['alice']
'''
birthday      1985
children         1
hobby       biking
weight          68
Name: alice, dtype: object
'''

df.iloc[0]
'''
birthday      1985
children         1
hobby       biking
weight          68
Name: alice, dtype: object
'''


#weight bob

df['weight'].loc['bob'] #83




#----------------filtering

#harki bnirthday <1990 hast ro bhm bde
#[] column
#condition bezari baraye filtering
clean_df=df[ df['birthday'] < 1990]



#besazid
#age

df['age']= 2025- df['birthday']

df['age+5'] = df['age'] + 5


df['over 30'] = df['age']>30


#filtering
#afradi k balaye  40 jastam

zarf=df[  df['age']>=40 ]


#dota shart
#==

zarf2=df[  (df['age']>=40) &( df['children']==3  )    ]



#column az column haye 
#.apply lambda

#--categorization------

#onae k bishtar az 2 bache daran --> busy  , free



#df['weight'].apply(lambda x:)

df['weight']=df['weight'] + 100

df['weight']=df['weight'].apply(lambda x: x+100)


df['category_busy_or_not']=df['children'].apply(lambda x:'busy' if x>2 else 'free')



#----
df.loc[df['age']>30,'status']='experienced'
df.loc[df['age']<30,'status']='junior'


#----hzarf remove------


#--------hzaf kardane yek sotoooon
#parid raft

df.pop('birthday')

#ya

del df['children']



#man in ravesh ro behet pishnehad mdim --> *******
#.drop()

zarf=df.drop(columns='age+5')

#zarf --> chizi bename age + 5 ndreeeee


#tabeye drop --> in tabe emalk nmishe balkke taghiro anjam mide va yk dataframe jadid misaze
#berizi too yek zarf


#emal bshe chii?


df.drop(columns='age+5',inplace=True) #False




#cleaning --> drop



'''

PANDAS

series
dataframe


[] column

loc
iloc ---> rows


[] = 

[ df[]>]


.apply()

.pop()

.mean()
.max() ---> 
.add() ---> yeseri adad




------
drop() ---> ina behet khoroji mide , va emal nmishe
ag khasti emal koni
drop(inplace=True)


'''

df.drop(index='alice',inplace=True) #False


#ham column pak koni ham radif

#.drop(index or column , inplace=True)



#bar ch asas ? bar asase vaznb? ghad ? kodom soitoon?

#bar che asas --> by what???


#sort_value() , drop() khoroji pas mdin , khode df ro tagir nmidn
#inpalce=True


df.sort_values(by='age',inplace=True)


#az bala b paeen michine


#az bishtar b kamtar bchine
df.sort_values(by='age',ascending=False,inplace=True)


df['children']=[1,2]


#------PLOT()
import matplotlib.pyplot as plt
x=df['children']
y=df['age']

plt.plot(x,y)
plt.title('childrfen vs age')
plt.xlabel('number of children')
plt.ylabel('age')
plt.show()


import matplotlib.pyplot as plt
x=df['children']
y=df['age']

plt.scatter(x,y)
plt.title('childrfen vs age')
plt.xlabel('number of children')
plt.ylabel('age')
plt.show()


#------PANDAS TOO DELESH --> Pltro poshesh mide

#yani mitoni rooye datat dot bzni va esm bbri


df.plot(kind='scatter',x='children',y='age')
plt.show()



df.plot(kind='scatter',x='children',y='age')
plt.title('childrfen vs age')
plt.xlabel('number of children')
plt.ylabel('age')
plt.show()


#scatter()
#plt.scatter(s=[10,20])




df.plot(kind='scatter',x='children',y='age',s=[10,40])
plt.title('childrfen vs age')
plt.xlabel('number of children')
plt.ylabel('age')
plt.show()




#_----------
'''
data frame chie


yadesh gereftam


mersi mnamno

ama dasti mitonam baz adad bdm

mesle list
mesle np array


pd.daraframe([z rooye excellam?])
'''

a=pd.DataFrame([10,20,30,40,50,60])


#yek adad dari , bad azash dataframe msiazi vba zakhriash mikoni to ye zarf


#ey kash man yek data dashtam , azash dataframe misakhjtram mriikhjtamesh troo zarff




#df -->dataframe
#tamame karaye balaro roosh anajm bdmm



#man baraye sakhte dataframe fght 
#tabeye pd.dataframe ro ndrm

#yseri tabe daram ke ba read shoro mishe




#pd.read_

'''

yek jadvali darim


file ha yekseri format drn


image ---> .jpg .png .JPEG
film ---> .gif .mp4 .movie ,....

barname -->  .pmebm 

.txt  --> file matne
.pdf --> file haye pdf

word---> .docs .docx



----> data ha

.xlsx .xls   ---> excelli
.csv ---> comma seperated values


open(),.....


open(path)


#masir bayad masire filet bashe az aval

fielt -> get info, p;roperties --> amsiresh

open('') --> file behet pas



.csv
pandas.read_csv(path)




.xls
.xlsx

pandas.read_excell(path)




spyder bayad pathe file shoamro peyda kone dastresi peyda kone
bede be tabeye read_excell --> 

read_... ---> yek tabeye open() bazesh mikone
adado mikeshe biroon

tabdilesh mikone be yek dartaframe

DataFrame behet [as ,mdoe
                 
                 pas briz to y zarf benamse df
                 
data ,.....

tamam etavabeye bala ro mitoni roosh kar koniiiii

users/desktop/nameshoam/name felan folder/..../esmefile.format

/Users/apm/Desktop


//Users//apm//Desktop


\\Users\\apm\\Desktop




'''



#mydata=pd.read_csv('/Users/apm/Desktop/FTIR-B.txt')


mydata=pd.read_excel('/Users/apm/Desktop/Tensile test.xlsx')


mydata.columns 
# Index(['1 _ 1', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'], dtype='object')

mydata['Unnamed: 1'].iloc[4] #0.05960464


mydata.drop(columns='Unnamed: 3',inplace=True)

mydata.drop(index=1,inplace=True)

zarf=mydata.loc[0]


mydata.columns


mydata.columns=zarf

mydata.drop(index=0,inplace=True)

mydata.reset_index(drop=True,inplace=True)

#cleran--------
#mydata.astype('int')



