#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 16:36:21 2025

@author: apm
----l14-----
review on L14.PY


KHodfemon data misakhtim

df=pd.dataframne([[[]]],index,colkumns)
df.sort_value
df[felan]=df[flean] + 100


----L15-------


df=pd.read_excel(path)  files--> xlsx xls
df=pd.read_csv(path) --> csv


dataframe --> pandas type
soton radif, esm


hameye tavabe ha kare mikone 
df.sort_value,.......


data to vared mikoni hamishe oonjori k fek mikoni nis??????
yani momkene , sotonet jabej ashode bashe
ye esmi file natonese bashe khonde

yekseri adad --> typesho avbaz shod

14.0 float

14


13.4309348448

13



13
'13' object ,...........



data --> import --> df ya data=pd.read_format(path)

preprocessing --> df --> datya anjam bdi k amade she
bartaye inke betoni roosh kar haye dg ro najam bdi 
ML , Model sazi , ........




preprocessing ( namayesh , informationm , description , soton , (manupulation), cleaning , Normalize (manupulartion))



----MAIN STEPS------
preprocessing [description , Manupulation , Cleaning]

Manupulation--> oon bala goftim --> [soton] + - np.exp , .....



description , cleaning

Main work


"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#_ too esm ezafe krdm

#bebinam fielkam chie ? va kojas?
#path ba user shoro mishe
#badesh esme file
#+ formatesh 


# /Users/apm/Desktop/Tensile_test.xlsx
#in adrese file mane



#chie? --> ag .xlsx .xls --> excel / .csv --> csv 


#pd.read_excel(/Users/apm/Desktop/Tensile_test.xlsx)

data=pd.read_excel('/Users/apm/Desktop/Tensile_test.xlsx')


#---------STEP0----------------------------
#-------0.0.columns , rows------------------
print(type(data))
#<class 'pandas.core.frame.DataFrame'>

#->numpy

#np.array(data)
#data --> dataframe

#dataframe --> np.array(dataframe) --> array --> computation



data.shape # (418, 4)
#radif , soton

#4 ta soton , 418 radif

data.size
#1672


#4 ta soton esmashon chie?
data.columns
#Index(['1 _ 1', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'], dtype='object')

data.head()
'''
  1 _ 1 Unnamed: 1 Unnamed: 2  Unnamed: 3
0  Time      Force     Stroke         NaN
1   sec          N         mm         NaN
2     0    0.00302   0.033367         NaN
3     1   0.053088   1.366967         NaN
4     2   0.059605   2.700167         NaN
'''

data.head(10)
'''
  1 _ 1 Unnamed: 1 Unnamed: 2  Unnamed: 3
0  Time      Force     Stroke         NaN
1   sec          N         mm         NaN
2     0    0.00302   0.033367         NaN
3     1   0.053088   1.366967         NaN
4     2   0.059605   2.700167         NaN
5     3   0.065168   4.033433         NaN
6     4   0.070731   5.366833         NaN
7     5   0.072797   6.700133         NaN
8     6   0.075181     8.0335         NaN
9     7   0.082652   9.366834         NaN
'''



data.tail()
'''
    1 _ 1 Unnamed: 1 Unnamed: 2  Unnamed: 3
413   NaN   0.035604   546.7337    268.0336
414   NaN   0.035286   548.0671    269.3670
415   NaN   0.034014   549.4004    270.7003
416   NaN   0.033696   550.7337    272.0336
417   NaN   0.027657   551.6282    272.9281
'''

data.tail(10)
'''
    1 _ 1 Unnamed: 1 Unnamed: 2  Unnamed: 3
408   NaN   0.040054    540.067    261.3669
409   NaN   0.039736   541.4004    262.7003
410   NaN   0.035127   542.7338    264.0337
411   NaN   0.034809    544.067    265.3669
412   NaN   0.034332   545.4005    266.7004
413   NaN   0.035604   546.7337    268.0336
414   NaN   0.035286   548.0671    269.3670
415   NaN   0.034014   549.4004    270.7003
416   NaN   0.033696   550.7337    272.0336
417   NaN   0.027657   551.6282    272.9281
'''




data.iloc[413]
'''
1 _ 1              NaN
Unnamed: 1    0.035604
Unnamed: 2    546.7337
Unnamed: 3    268.0336
Name: 413, dtype: object

'''


data.loc[413]
'''
1 _ 1              NaN
Unnamed: 1    0.035604
Unnamed: 2    546.7337
Unnamed: 3    268.0336
Name: 413, dtype: object
'''


data['Unnamed: 1'].iloc[0] #'Force'


#endakhtane soton --> drop 
#jabe jaee --> []
#manupulation

#data.drop()
#columns
#index

data.columns

#age ino ejra koni , az data ino midnaze behet pas mide
#ama khdoe data taghir nmikone , 
#balke to bnayad y zarfe jadid bairy
data.drop(columns='Unnamed: 3')

#dast nakhrode bashe
#zarf1=data.drop(columns=')

#emal bshe hey nmikhay zar

data.drop(columns='Unnamed: 3',inplace=True)

#man chizi behet pas nmidm , roye khdoe data taghir

data.head()

'''
  1 _ 1 Unnamed: 1 Unnamed: 2
0  Time      Force     Stroke
1   sec          N         mm
2     0    0.00302   0.033367
3     1   0.053088   1.366967
4     2   0.059605   2.700167
'''

data.loc[0]

mycolumn_names=data.loc[0]
print(mycolumn_names)

#data.columns=['esme1','esm2','esm3']

data.columns=mycolumn_names

data.head()

data.columns #Out[124]: Index(['Time', 'Force', 'Stroke'], dtype='object', name=0)

data.drop(index=0,inplace=True)

data.head()

data.drop(index=1,inplace=True)

data.head()

'''
0 Time     Force    Stroke
2    0   0.00302  0.033367
3    1  0.053088  1.366967
4    2  0.059605  2.700167
5    3  0.065168  4.033433
6    4  0.070731  5.366833
'''

data.drop(columns='Time',inplace=True)


data.head()

#row hazf mikoni , sort value 
data.reset_index(drop=True,inplace=True)
#drop --> true


#----data --> zakhrie koni
#hosel nadrm frda pas frda

#taghir ha rooye data. datafram

#read_excell 


#excelle man tyaghir nkrde 

#data dataframe

data.to_excel('clean_tensile.xlsx') #sheet name , ....
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel



data.to_excel('/Users/apm/Desktop/clean_tensile.xlsx',sheet_name='cleaned') #sheet name , ....

#to csv
#format 


#excel --> dataframe

#dataframe --> excel




##-------0.1.DESCRIPTION------------------
data.head()
data.tail()


data.info() #cleaning

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 416 entries, 0 to 415
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Force   416 non-null    object
 1   Stroke  416 non-null    object
dtypes: object(2)
memory usage: 6.6+ KB

'''

data.describe()

'''
0            Force      Stroke
count   416.000000  416.000000
unique  290.000000  416.000000
top       0.135422    0.033367
freq      5.000000    1.000000

'''



#--------0.2 cleaning------------------------

'''

moshkel haye dat aha

1- empty cell --> khalie (khataye ensani , kahli omde bashe ,...)
2- wrong format --> int , float --> str , object , .... 
3- wrong data --> (dama bayad ballaye  0 -> zire 0 bashe , doros , dastgah eshtebah , ..,,) logic 
4- duplicated --> tekrari 


aval bayad tashkhis bdidddd
vghty tashkhis dadi bayad amal konid ( hazf , poresh koni)




'''

data.info()
'''
1-empty cell
2-wrong format
'''

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 416 entries, 0 to 415
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Force   416 non-null    object
 1   Stroke  416 non-null    object
dtypes: object(2)
memory usage: 6.6+ KB


type ghalat bashe --> wrong format
null ----> empty cell


'''


#-------EMPTY CELL------

data.tail()

new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[70,None],[80,100] ],columns=['Force','Stroke'])

new_data.head()
'''
   Force  Stroke
0     10    20.0
1     30     NaN
2     40    60.0
3     70     NaN
4     80   100.0
'''

new_data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Force   5 non-null      int64  
 1   Stroke  3 non-null      float64
dtypes: float64(1), int64(1)
memory usage: 212.0 bytes

'''

#mepty cell injori mitoni befahmi k dare ya nadare

#-----hazf--------
new_data.dropna(inplace=True)

new_data.info()

'''
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Force   3 non-null      int64  
 1   Stroke  3 non-null      float64
dtypes: float64(1), int64(1)
memory usage: 72.0 bytes
'''


#------fill --> por koni jash------
new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[70,None],[80,100] ],columns=['Force','Stroke'])

new_data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Force   5 non-null      int64  
 1   Stroke  3 non-null      float64
dtypes: float64(1), int64(1)
memory usage: 212.0 bytes
'''


#nemikham hazf
#shoma fetures , column ziad dari , data kam dari dataha aarzeshmnandan
#va besorat emanteghi oon soton k Nan , Null mitoni jygozin koni

#dastiii

new_data.fillna(10,inplace=True)

new_data.info()



#---------
new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[70,None],[80,100] ],columns=['Force','Stroke'])
a=new_data['Stroke'].mean()


new_data.fillna(a,inplace=True)


new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[70,None],[80,100] ],columns=['Force','Stroke'])

a=new_data['Stroke'].median()

new_data.filna(a,inplace=True)

#np.mean()
#np.max()
#np.min()
#np.mode()
#np.median()
#np.stdev
#np.var()
#.....

#np.sin()
#np.exp,....










#------------
new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[70,None],[80,100] ],columns=['Force','Stroke'])
new_data.fillna(method='ffill' ,inplace=True)
#radife ghabli harchi has kgozashte sasre jash

new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[70,None],[80,100] ],columns=['Force','Stroke'])

new_data.fillna(method='bfill' ,inplace=True)
#badiii


#-----------------


new_data=pd.DataFrame([  [10,20],[30,np.nan] ,[40,60] ,[None,60],[80,100] ],columns=['Force','Stroke'])
new_data.head()
'''
   Force  Stroke
0   10.0    20.0
1   30.0     NaN
2   40.0    60.0
3    NaN    60.0
4   80.0   100.0
'''

new_data.dropna()
'''
   Force  Stroke
0   10.0    20.0
2   40.0    60.0
4   80.0   100.0
'''


new_data.fillna(10)
#a = mean

'''
   Force  Stroke
0   10.0    20.0
1   30.0    10.0
2   40.0    60.0
3   10.0    60.0
4   80.0   100.0
'''

#sotone strok mean strok
#sootn force miangin


new_data.head()
'''
   Force  Stroke
0   10.0    20.0
1   30.0     NaN
2   40.0    60.0
3    NaN    60.0
4   80.0   100.0
'''

force_mean=new_data['Force'].mean()

stroke_mean=new_data['Stroke'].mean()


#new_data.fillna()

new_data['Force'].fillna(force_mean,inplace=True)

new_data['Stroke'].fillna(stroke_mean,inplace=True)


#---------------------------

#------2--Wrong format----
#az ecell

data.columns

data.head()
'''
0     Force    Stroke
0   0.00302  0.033367
1  0.053088  1.366967
2  0.059605  2.700167
3  0.065168  4.033433
4  0.070731  5.366833
'''


data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 416 entries, 0 to 415
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Force   416 non-null    object
 1   Stroke  416 non-null    object
dtypes: object(2)
memory usage: 6.6+ KB
'''
#****
#data.iloc(3)


#pd.to_numeric()

#astype

#column
data['Force']=pd.to_numeric(data['Force'])

data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 416 entries, 0 to 415
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Force   416 non-null    float64
 1   Stroke  416 non-null    object 
dtypes: float64(1), object(1)
memory usage: 6.6+ KB
'''

#=hamino mitoni benvisi ama man y raveshe dg ham miga
#data['Stroke']=pd.to_numeric(data['Stroke])

data['Stroke']=data['Stroke'].astype(float)
#float
#int


data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 416 entries, 0 to 415
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Force   416 non-null    float64
 1   Stroke  416 non-null    float64
dtypes: float64(2)
memory usage: 6.6 KB
'''



#------------
'''
1-empty cell --> info() --> non-null , tedadedk kol
agar null

hazf --> dropna() 

fill --> fillna(khdoet)
fillna(ye soton.mean())
fdillna(method=ffil or bfill)

data[soton].fillna


2-type ghalat --> info --> dtype --> object, float

data[soton] =pd.to_numeric(data[soton])
data[soton]=data[soton].astyp(type)



'''


#---wrong logic
#dama

'''
manupulation

df[df<100]
df['temperature'].apply(lambda x: 0 if x >100 else x)



'''




#_---duplicated
#**** gahan shayad shoma nmikhay tekrari bashe

data.drop_duplicates(inplace=True)

#data --> tamame tekrari haro hazf mikone



#mesle tamame chiz haee k bod
#drop , duplicate ,.....

data.reset_index(drop=True,inplace=True)






#-----0.1. description------

data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 416 entries, 0 to 415
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Force   416 non-null    float64
 1   Stroke  416 non-null    float64
dtypes: float64(2)
memory usage: 6.6 KB

'''


#adade 


data.describe()

'''
0           Force      Stroke
count  416.000000  416.000000
mean     0.145620  275.670673
std      0.054596  159.728760
min      0.003020    0.000000
25%      0.114878  137.750000
50%      0.135263  276.500000
75%      0.174046  413.250000
max      0.278950  551.000000

'''

data.describe(include='all')


#------

#har soton ro bbin

data['Force'].mean()

#.media()

#.mode()

#.var()


#.skew()
#.kurtosis()

#quantitle(0.25)

#.sum()


data.corr()

'''
0          Force    Stroke
0                         
Force   1.000000  0.584274
Stroke  0.584274  1.000000




+1    -1

sehdat --> correlated hastan in dota soton

.corr()---> correlation matrix --> columns

'''


data.cov()
'''
0          Force        Stroke
0                             
Force   0.002981      5.095230
Stroke  5.095230  25513.276825

'''


#---adad --> category , good, best 
#0 1 2 

#data['category'].unique()
#.value_counts()



import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(data['Force'])
plt.show()


#plt.hist



#2 ta ......
#sns.boxplot(x='Force' ,y='Stroke',data=data['Force'])
#plt.show()


sns.pairplot(data)
plt.show()




#----------

data.reset_index(drop=True,inplace=True)


#data --> 
data.to_excel('save_path///////esm.xlsx')
data.to_csv()
data.to_json()



#code ML , ......


'''

Hafteye ayande jOme 


ML ----- Shoro mikone

16 ,17 , 18 , 19 20



Project2 



P2_Fname_Lname

P2_Ali_Pilehvar_Meibody


ai.2024.pilehvar@gmail.com

payame daryaft



Python bashe



Project1 --> 20 %

PROJECT2 --> 30%



#-------------------
project3 --> 50%
#-------------------


'''

#Tensile_Test(data,application):
    

#data= pd.dataframe(path)

#esme_ye_test(data) --> toye tabat


def esme_ye_test(data,application):
    
    if application=='':
        
        #yek kari
        pass
    
    elif application=='chize dg':
        #yek kare dg
        pass
    
    
    
    



#Tensile test--->


'''

STress , Strain 




s1=data['Stress']







'''

#1-->plot
#2--> calculate hesab


data=pd.read_excel('')

def Tensile_Test(data,application):
    
    
    '''
    Tensile Test : .....
    
    
    Input-----
    data : datafram . xlsx , csv , datafram 
    columns : Stress , Strain
    
    
    application= [plot , uts , modulus]


    output ------
    plot , number (float)
    
    
    '''
    
    
    if application=='plot':
        
        x=data['Stress']
        y=data['Strain']
        
        plt.plot(x,y) #ziba sazi
        plt.title('Stress strain curve')
        plt.xlabel('Strain')
        plt.ylabel('Stress')
        
        plt.show()
        
        
        
    elif application=='UTS':
        uts=data['Stress'].max()
        return uts


'''

berid begardi --> data alaghe darid


FTIR --> intensity , disatnce

x=data['intensity']
y=data['distance']

plt.plot(x,y)
plt......





    

Tensile Test
XRD
FTIR




ai.2024.pilehvar@gmail.com



'''




import pandas as pd
import matplotlib.pyplot as plt


'''
#-------
data --> Tensile xlsx




farz mishe kard



'''

data=pd.read_excel('/////////')

data.columns


def myfunc(data,application):
    if application=='plot':
        x=data['strain']
        y=data['stress']
        plt.plot(x,y)
        #....
        
        
        
    
    
data=pd.read_excel('/////////')
    
myfunc(data,'plot')
    
    
#_---------------------

'''

FTIR --> 


data=pd.read_excel('.....')

data --> data frame


column s----< intensity , deisplacement





'''
    


def myftir(data,application):
    
    if application=='plot':
        
        x=data['displacement']
        y=data['wavelength']
        plt.plot(x,y)
        plt.show()
        



        
        





