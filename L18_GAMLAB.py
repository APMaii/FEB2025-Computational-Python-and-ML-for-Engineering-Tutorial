#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:40:20 2025

@author: apm
"""

#-----regression------

#LR --> Linear regression
from sklearn.linear_model import LinearRegression
model=LinearRegression()

#KNN--> K nearest neighbour
from sklearn.neighbors import KNeighborsRegressor
model=KNeighborsRegressor()


#DT --> Decision tree
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()


#RF --> random forest
from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()


#SVR ---> support vector machine
from sklearn.svm import SVR
model=SVR()


#Multilayer perceptron (mlp )--> ANN (Artificial neural network)
from sklearn.neural_network import MLPRegressor
model=MLPRegressor()


#model ha --> ine ke rabteyee beyne x va y ro bedast biaran 
#ba raveshe amari --> y = a*x + b 
#a va b ro bsats bairan

#model.fit() ---> algorithmie toye fit
#Linear regression --> a, b hayte mokhtalef ro mesal mizd va va va...

#motefavete
#model.predict() --> poishbini --> x 

'''
Linear model

KNN

Decision tree

Random forest

Support vector machine

Multi layer perceptron

too deleshon ham mitonan baraye regression estefade shane ham classificatin

regression --> esme_model regressor()
classificiton --> esme_m odel classifier()

'''

#linear model --> classification
from sklearn.linear_model import LogisticRegression
model =LogisticRegression()


#KNN
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()


#DT
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()

#RF
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()

#SVM --> support vector MMMMACHINE
#--SVR --> SUPPORT VECTOR RRRRREGRESION
#--SVC --> SUPPORT VECTOR CCCCCCLASSIFICTION
from sklearn.svm import SVC
model=SVC()

#mlp
from sklearn.neural_network import MLPClassifier
model=MLPClassifier()





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.DataFrame( [ [10,12,'narges' ],[5,12,'narges' ],[10,9,'narges' ],[8,8,'narges' ],
                    [7,13,'narges' ],[6,8,'narges' ],[10,10,'narges' ],[7,4,'narges' ],
                    [4,8,'narges' ],[6,10,'narges' ],[18,15,'yasaman' ],[17,13,'yasaman' ],
                    [20,14,'yasaman' ],[18,15,'yasaman' ],[19,15,'yasaman' ],[14,20,'yasaman' ],
                    [13,19,'yasaman' ],[15,15,'yasaman' ],[16,18,'yasaman' ],[18,16,'yasaman' ]],columns=['tool','arz' , 'type'])




x=np.array(data[['tool','arz']]) #bsih az yedone sotone oeye
y=np.array(data['type'])

#--------------------------------------
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
final_y=label_encoder.fit_transform(y)


#--->train tesy
from sklearn.model_selection import train_test_split
x_train, x_test , y_train , y_test = train_test_split(x,final_y, test_size=0.2 , shuffle=True , random_state=42)





#----> model sleection
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(x_train,y_train)


#linear--> sade ee hastan


#-----> KNNN --> nazfdik atrin hamsaye ro varmdiare
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=10) #too deleshon modelo , hyperparameter (fara paremetr)
#shoam tanzim mikonid va khodehs yad nmigre
#tasire mostaghhim rooye yad girish dre
#ma az koja bdonim?

#optimization
model.fit(x_train,y_train)





#------Decision Treee--------
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=7)
model.fit(x_train,y_train)

#soal hae k miporse --> joda mikone , pslit --> randoman 





#------RANDOM FOREST------
#ensemble
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=50)
#10 , 100 , 200 --> chanta decision treee besaze

#harchi bsightar --> jangale pichide tari mishe

model.fit(x_train,y_train)




#-----Support vector machine-----
from sklearn.svm import SVC #clasifaction #SVR -> Regression
model=SVC(kernel='linear')
#linear --> khati
#poly ---> chan jomle  ee b tavane 2 , 3 ,4 ,degree
#rbf --> fasele haye data tasmim migire

#gamma, C

model.fit(x_train,y_train)














#----. evaluation

y_pred=model.predict(x_test)
y_true=y_test

from sklearn.metrics import accuracy_score

test_score=accuracy_score(y_true,y_pred)

#tgrain .....

print('accuracy: ' , test_score*100 ,'%')

#logisitic regression --> accuracy:  100.0 %
#KNN --->  K = 3 , accuracy:  100.0 %
#KNN --> K=1 , accuracy:  100.0 % 
#KNN --> k=10 , accuracy:  100.0 %
#DT --> max depht =1 --> accuracy:  100.0 % 
#DT --> max depth =7 --> accuracy= 100%

#RF --> n_est=50 --> accuracy:  100.0 %
##RF --> n_est=200--> accuracy:  100.0 %



#SVC --> kernel= linear accuracy:  100.0 %
#SVC --> kernel= poly accuracy:  100.0 %
#SVC --> kernel= rbf accuracy:  100.0 %




#accuracyt paene --> tesdt scoret paene --> 
#train score

y_pred=model.predict(x_train)
y_true=y_train

from sklearn.metrics import accuracy_score

train_score=accuracy_score(y_true,y_pred)
print(train_score)
#train_score paeene --> udnerfitting --> modelo complexe
#train-score kh balae--> overfitting --> complexity kamesh kon


'''

---------IMPORTANT HYPERPARAMETERS-----------


lINEAR MODEL------
No hyperaprameters



KNN---------

K --> bishtaresh koni  --> complex tar



DT-----
Max depth --> ahrchi bishtar konim --> bishtar jod amikone--> complex tar mishe



RF----
n_estimator --> more --> more complex forest



SVM----




******** SUPERVISED CH REGRESSION , CLASIFICATION
yekseri mdoel

data --> clean
x, y ( numpy)


train test taghsim

model
---> LINEAR, knn, dt , rf , svm , mlp

linearregression ,  kneighbourregressor , decisiontreeregressor , randomforestregressor , SVR , MLPregressor
logisticregression,  kneighbourclassifier , decisiontreeclasifier , randomforestclassifier , SVC , MLPclassifer

Joz linear, hame ye ina hypeprarmeter

MODEL= esme model(hypeparameter)

-->tasir dare rooye yadgirish , ya compel xmikone ya kh geenral --> optimize 


model.fit(x_train,y_train)

---evaluation

y_pred=model.predict(x_train  ya x_test)
y_true = y_train ya y_test


fasley eebyen y_pred , y_true

----Rgeression Metrics darim
MAE --> MEAN ABSOLUTE ERROR
MAPE --> MEAN ABSOULUTE PERCNETAGE ERROR

---clasification metrics 
ACCURACY



test score ya train score

underfgit , overfit --> atsmim bgiri modeleto co0mplex , geenral (bazi ba hypeparamter)



'''



#---------------------
#-------------------------
#----classification
#=---->data

#--data
#clean --> clean hast .info()


#x , y 

#-->: train test
#Model --> 
#logisticregresion
#KNNclassifier
#decisiontree classsifier
#randomfrestclassifier
#SVC


#HYPERPARAETR 
#3 ta hyperpamrter 
'''

13 ta accuracy
13 ta test score
13 ta train score

'''




'''
https://scikit-learn.org/stable/datasets/toy_dataset.html
'''



'''


500 biam r--> ax --> ct scan --> andazeye toomot, shedate , rnage shedat --> adad ha ro

  -------x---------       -y-
1  14    70  .........    0
2
3
4
5

0 ya 1 khoshkhim ya badkhim



input --> model--> output



biamre jadid --> bere ct scan bgire ,in voirodi haro az roosh bbinm bznm b model
model behem ba deghat ekhodehs bge badkhim ya khosh khim e(darsad)


output 0 ,1 --> classification

model haye motevafe

.....


500





'''



from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
#taghsim krde
x=data.data
y=data.target

#info , train tets ,....

#---------------
x.shape #(569, 30)   569 biamr , y ax -> 30 ta featuresho keshidan
y=data.target
y.shape


data.target_names
#array(['malignant', 'benign'], dtype='<U9')
#0   malignant 
#1 benign


data.feature_names
'''
array(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension'], dtype='<U23')

'''


#x --> 30 ta features (input)
#y-->target --> output


#13 


#-->: train test
#Model --> 
#logisticregresion
#KNNclassifier
#decisiontree classsifier
#randomfrestclassifier
#SVC


#HYPERPARAETR 
#3 ta hyperpamrter 
'''

13 ta accuracy
13 ta test score
13 ta train score



ai.2024.pilehvar@gmail.com





agha behtarin mdoel man SVC --> 98% deghat toonese pishbini 




K means -_> clustering , ....
MLP --> multilayer perceptron-->introduction on deep learning 


'''













