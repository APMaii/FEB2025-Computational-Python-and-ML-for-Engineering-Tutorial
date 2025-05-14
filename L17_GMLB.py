#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The name of GOD

Created on Sun May  4 17:44:37 2025

@author: apm


bad az GMLB_L17.ipynb




workflow



data --> bairi

preprocess

data --> x , y

x, y --> np.array

x,y --> x_test , x_train , y_test, y_train


model improt koni az sklearn (linearegression)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_true=y_test

MAPE , MAE --> y_pred - y_true --> darsadet ghabele ghabol


new_x
model.predict(new_x)


"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.DataFrame([ [10,120],[15,173],[20,230],[25,270],
                   [30,298],[35,380],[40,420],[45,480],[50,520]],columns=['speed','estehkam'])


#data=pd.read_excel()


# 9 ta data drm

#data --> preprocess

data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 2 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   speed     9 non-null      int64
 1   estehkam  9 non-null      int64
dtypes: int64(2)
memory usage: 272.0 bytes

'''

data.columns
#Index(['speed', 'estehkam'], dtype='object')

'''
x=data['speed']
#x=data[['speed','temp','time',..]] #--. resshape
y=data['estehkam']

'''


x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])

plt.scatter(x,y,label='experimental data')
plt.title('ML')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()


#man mikham x , y --> train dataset , test dataset

#dioat --> 
#dasti anjam dadam 

#chanta vrdaram?
#chnata vrdm


#besorate nromal 20% datat ro boro tets kon / 80% train

#20%


#2 taye tah?
#2 taye saro
#2 taye vasato ?

#shuffle kon --> 

#bias --> taasobo mahdodiat varede modelet nakon


#man ham baayd brm ranodm vrdaram
#ham 20 % 

#x_train=x[:7]
#y_train=y[:7]
#x_test=x[7]
#y_test=y[7]


#sklearn --> workflow --> train_test_split


from sklearn.model_selection import train_test_split



#tabe --> vorodi migire , khoroji mide

#onchizi k mikjhya taghsimesh koni
#x , y ro behesh bdi

#zire 1 --> test size


#0.2 --> 20%dataharto test kon

#0.3 --> 30%

#0.8 --> 80%

#--> normal --> 0.2
#20 az akahr vrdarma ya na
#shuffle=False --> az akahr vadar
#shuffle = Tru e--> hamehs mzine , random vrmdiare --> ghabele ghabol tre

#hardafe ino run koni har dafe shuyffl mikone
#y adad var midre
#har dafe k run bshe codet ye dsarsad khatee mide

#9.1
#9.8

#maghalat
#baray karha



#train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

#khoroji --> x , y --> x_test , 


#khoroji =train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)


x_train,x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)


plt.scatter(x_train,y_train,label='train data')
plt.scatter(x_test,y_test,label='test data')
plt.title('ML after train_test_split()')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()


#----------
#model azinja bebad
#faght tarin ro mibinme

plt.scatter(x_train,y_train,label='train data')
plt.title('ML after train_test_split()')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()



#-----model 

from sklearn.linear_model import LinearRegression

model=LinearRegression()

model.fit(x_train,y_train)


#Out[19]: LinearRegression()


#a , b --> rabtee 

model.coef_ #array([9.95238095])

model.intercept_ #21.14285714285728


x_new=np.array([100]).reshape(-1,1)
sample_prediction=model.predict(x_new)
print(sample_prediction)
#baraye speed 100
#[1016.38095238]



#bayad bbini khatye modelet chghdre va bad bri pishbini


#---> x --> y _pred
# x--> y_true (azmayeshgah)
#y_pred - y_true


#test dataset --> 2 ta ro endakhtim brion (split)



#test data--> new data  , unseeen data

#x--> bedi b model --> y_pred
#y---> mogahyes ekoni

print(x_test)
'''
[[45]
 [15]]

'''

'''
agha boro sorate 45 va 15 ro barma pishbini kon
'''
y_pred=model.predict(x_test)


print(y_pred)

'''
agar speed 45
[469.    

 agar 15
     170.42857143]

'''


y_true=y_test

print(y_true)
'''
agar 45 bzari
[480 
 
 
agar 15 bzari  
 173]

'''

#MAE mmean absolute error -->  khatey motlaghe
#MAPE --> darasad khata

#MSE --> 
#RMAE --> root

#baste b jorunal , publication 
#0.00001 , S --> 


#MAE , MAPE 
#agha faseley beyne khataro

#y_pred , y_true 

#tabe daram bhm y_prede , y_true ro bnde man hesba mikonm




from sklearn.metrics import mean_absolute_error

#fasleye beyen y_true , y_pred bartaye har noghte migre
#bsorate miangin pas mide
MAE=mean_absolute_error(y_true,y_pred)

print('my model MAE : ',MAE)
#my model MAE :  6.785714285714249

'''

+- 6 ta adad

100 - 1000


200 --> 194 / 206 

'''



from sklearn.metrics import mean_absolute_percentage_error



MAPE = mean_absolute_percentage_error(y_true,y_pred)


print('My model MAPE : ',MAPE*100)

#My model MAPE :  1.8890207817230726

#2% kharta modelet




#-----------

#x_new--> 

#model.predict()


#-----------
#az speed 1 ta 100 --> modelet 



my_all_x=np.arange(0,200).reshape(-1,1)

y_for_all=model.predict(my_all_x)


plt.scatter(my_all_x,y_for_all,s=1,label='Prediction of my model')

plt.title(f'Linear regression model with {MAPE*100} %')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()







#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================

#improt data
data=pd.DataFrame([ [10,120],[15,173],[20,230],[25,270],
                   [30,298],[35,380],[40,420],[45,480],[50,520]],columns=['speed','estehkam'])
#preprocesing , cleaning
data.info()
data.columns

#--> numpy array x , y
x=np.array(data['speed']).reshape(-1,1)
y=np.array(data['estehkam'])


#---> test data set , train dataset-----
from sklearn.model_selection import train_test_split
x_train,x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

#model import-----
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#from sklearn.tree import DecisionTreeRegressor
#model=DecisionTreeRegressor()

#from sklearn.svm import SVR
#model=SVR()



#---> FIT, Training
model.fit(x_train,y_train)

#optional
model.coef_ #array([9.95238095])
model.intercept_ #21.14285714285728

#---evaluation (predict)

#-------TEST SCORE-----------
y_pred=model.predict(x_test)
y_true=y_test

from sklearn.metrics import mean_absolute_error
test_score_MAE=mean_absolute_error(y_true,y_pred)


from sklearn.metrics import mean_absolute_percentage_error
test_score_MAPE = mean_absolute_percentage_error(y_true,y_pred)




#-------Train SCORE-----------
y_pred=model.predict(x_train)
y_true=y_train

from sklearn.metrics import mean_absolute_error

train_score_MAE=mean_absolute_error(y_true, y_pred)

from sklearn.metrics import mean_absolute_percentage_error
train_score_MAEP=mean_absolute_percentage_error(y_true, y_pred)


#----TAHLILK KONI
#nesbat b train score, test scorer
#ag joftessh khoban mobarake awlie

#ag test score  paeene

#train scoretam ag paeene --> yad nagrfe --> underfiti(modelto complex)
#train scoret kh balae --> bish az had yad (noise) --> overfittin ( complexity kam kon)



#--optional koel range ro predict 
my_all_x=np.arange(0,200).reshape(-1,1)
y_for_all=model.predict(my_all_x)
plt.scatter(my_all_x,y_for_all,s=1,label='Prediction of my model')
plt.scatter(x_train,y_train)

plt.title(f'Linear regression model with {test_score_MAPE*100} %')
plt.xlabel('speed')
plt.ylabel('estehkam')
plt.grid()
plt.legend()
plt.show()



#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#========================================
#=========================================
#b ina migan score
#MAE , MAPE

#train score
#test score

y_pred=model.predict(x_test)
y_true=y_test

test_score=mean_absolute_percentage_error(y_true, y_pred)

#fasleey beyen y_test va pishbinish

print(test_score*100)
#1.8890207817230726


#agar oon x_train --> y_train --> data train dide

y_pred=model.predict(x_train)
y_true=y_train

train_score=mean_absolute_percentage_error(y_true, y_pred)
print(train_score*100)
#2.1876857632850046


#behtarin noghtaro peyda krde
#am ahamon khat ham khata dare
#b in khata migan train score


'''

Data --> Train | Test

model. did .fit (Train dataset)

evaluation ---> 2 score --> train score / test score

model.predict(x_train ) --> moghayesash kon ba y_train --> train score

model.predict(x_test) -->moghatyese kon ba y_test --> test score




train score---> behet mige model cheghad khoob tonese yad bgire az data
test score --> behet mige model chjegahd khob mitone data haee k nadide ro pishbini kone



#----test scoret khafan nis --> baray etah;lil koni modeleto 
test sciore, train score



train scoretg kh paeen bod --> test scoretam paeen bood --> underfitting (modele kh simple o kh sadas, complex taresh koni)

train scoret kh kh balast , test scoret paeene -->  overfitting ( complexity modelet inghd balas , noise, pishbini kone , general bshe,complex modeleto kam koni , general tresh koni)





'''


'''

pip install scikit-learn


DATA --> 

yek soton x , yek sotone y --> real world , kar haee bashe k khodron mikhay d konid

10 ta adad --> azmyeshgahi 



test score
train scoresho bnvisi

MAE , MAPE

tahlilesh konid



ai.2024.pilehvar@gmail.com

'''


