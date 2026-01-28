"""
In The name of GOD
Created on Wed May 21 16:31:55 2025

@author: apm


----L20---------


----3 PART --------





----PART1------------
python --> IDE , python , anaconda ,...
basic 
built in functions (print, input, .......)
variables (int, float,bool , str, str functions)
iterable variables(list,set,tuple,dict , funciton)
keywords(if , if else, elfi , for , while ,.....)

function --> def
advanced --> class (def ,.. attributes)
special keywords, built in function



**ketab ha
** video haye youtube
**course coursera
--->review + nokate ezafi 


-----PART2------
#ketabkhane hayemohem
from lib import function

matth , random , statiustic, datetime

numpy --> np.array() functions --> instead of list
scipy ---> function
sympy ---> symbolic
matplotlib --> rasm (plot,pieplot , barchart ,....)
pandas--> dataframe , import data z excel, csv, cleaning data



**khode site ketabkhone ha
** documentation --> dakheelksh tamame tabe haro
tutorial yad dadan
##videohaye youtube mohemtrin tabe haro yad ddn
**ketab khaee k vase khode site 



-----PART3---------
cleanin data 
Machine learning ---------

----AI-----(70,80% --> Machine learning)

tamame data -->

input ----> [box] --->output


4 no machine learning

1-Supervised
2-unsupervised
3-reinforcement learning
4-deep learning


data ---> input ham output ---> 
supervised learning , deep learning
ag datat kh bnozorge ---> deep learning (million, sad hezar)
supervised ---> 
output --> countinious --> supervised regression
----> gosaste --> supervised classsification


--------
output nadasht ---> unsuypervised 

----
dataee nadahsti , environmenet --> 
reinforcement learning (RL)










#---------Supervised learning-----------------
--------raveshe aval --> levele 1-------
step0----> import datatono
step0.1--> clean data
step0.2 --> x , y  (numpy array)

step1 --> train test dataset tabdil konid

step2 -->modeltono entkehab konid ( 6 --> Linear,KNN,
                                   DT , RF , SVM , MLP)ba hyperpaameter
step3 --> model train roye train dataset

step 4--> evaluation ( test dataset )--> metrics



-----raveshe dovom--> levele 10 --------
step0----> import datatono
step0.1--> clean data
step0.2 --> x , y  (numpy array)

step1 -->
model -->modeleto entkehab mikoni
step2--> grid params -->{hyperparametratp}

step3---> gridsearch ( model)

step4 ---> gridsearch.fit (kole data)

step5 -->  gridsearch.best_score .best_estimator




classification
regression
kole kar ha yeksane

fght tooye ghesmati k mikhay modelo biari
braye regression --> trahe model --> regressor
baraye classification --> classifier


evaluation --> 
regresssion --> metric MAE , MAPE 
classification --> accuracy 


"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#raw_data= pd.read_excel(path)

# Define column names
columns = [
    'Rows', 'nonsolvent-ethanol', 'nonsolvent-water ', 'non-solvent- DMF',
    'Concentration ', 'Speed', 'Temp', 'Extrusion multiplier',
    'linear mass flow rate', 'printability', 'Shrinkage'
]

# Generate synthetic data
np.random.seed(42)  # for reproducibility
data = {
    'Rows': np.arange(1, 75),
    'nonsolvent-ethanol': np.random.uniform(0, 100, 74),
    'nonsolvent-water ': np.random.uniform(0, 100, 74),
    'non-solvent- DMF': np.random.uniform(0, 100, 74),
    'Concentration ': np.random.uniform(0.5, 10, 74),
    'Speed': np.random.randint(100, 2000, 74),
    'Temp': np.random.uniform(20, 100, 74),
    'Extrusion multiplier': np.random.uniform(0.5, 3.0, 74),
    'linear mass flow rate': np.random.uniform(0.1, 5.0, 74),
    'printability': np.random.randint(0, 2, 74),  # binary: 0 or 1
    'Shrinkage': np.random.uniform(0, 30, 74)
}

# Create DataFrame
raw_data = pd.DataFrame(data, columns=columns)


#cvlean---> pandas yad dade shod

raw_data.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 74 entries, 0 to 73
Data columns (total 11 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Rows                   74 non-null     int64  
 1   nonsolvent-ethanol     74 non-null     float64
 2   nonsolvent-water       74 non-null     float64
 3   non-solvent- DMF       74 non-null     float64
 4   Concentration          74 non-null     float64
 5   Speed                  74 non-null     int64  
 6   Temp                   74 non-null     float64
 7   Extrusion multiplier   74 non-null     float64
 8   linear mass flow rate  74 non-null     float64
 9   printability           74 non-null     int64  
 10  Shrinkage              74 non-null     float64
dtypes: float64(8), int64(3)
memory usage: 6.5 KB

'''



raw_data.drop(columns='Rows',inplace=True)
#raw_data.drop(index=4,inplace=True)


#------x , y az delesh bairi biron
raw_data.columns

'''
Index(['nonsolvent-ethanol', 'nonsolvent-water ', 'non-solvent- DMF',
       'Concentration ', 'Speed', 'Temp', 'Extrusion multiplier',
       'linear mass flow rate', 'printability', 'Shrinkage'],
      dtype='object')

'''


x=np.array(raw_data[['nonsolvent-ethanol', 'nonsolvent-water ', 'non-solvent- DMF',
       'Concentration ', 'Speed', 'Temp', 'Extrusion multiplier']])

y=np.array(raw_data['Shrinkage'])






#----step1----------

from sklearn.tree import DecisionTreeRegressor

model=DecisionTreeRegressor() #hypeparsamter fix --> fix 


#---steop2------

#myparams={'max_depth': [5,6,7,8,9,10,11,12,13,14,15],
#          'esme ye hyperparamert': range [], np.arange(0,100)}


myparams={'max_depth': [5,6,7,8,9,10,11,12,13,14,15]}


from sklearn.model_selection import GridSearchCV

#classification--> accuracy
#regression --> MAE , MAPE

gs=GridSearchCV(model,param_grid=myparams,scoring='neg_mean_absolute_percentage_error',
                cv=7)





'''

60 10

50 10 10 


miangin
'''


gs.fit(x,y)



gs.best_params_ #{'max_depth': 5}

gs.best_score_ # -1.498899034360243

raw_data.columns

new_x=np.array([40,10,50,3,100,40,1]).reshape(1,-1)

gs.predict(new_x)


my_new_data={}

for i in range(0,100):
    my_new_data[i]=np.array([40,10,50,3,i,40,1]).reshape(1,-1)
    
    
predicted_values=[]


for data in my_new_data.values():
    new_res=gs.predict(data)
    predicted_values.append(new_res)
    
    

import matplotlib.pyplot as plt

new_x=np.arange(0,100)
new_y=predicted_values

plt.plot(new_x,new_y)
plt.xlabel('speed')
plt.ylabel('predicted shrinkage')
plt.grid()
plt.show()



plt.scatter(new_x,new_y,s=1)
plt.xlabel('speed')
plt.ylabel('predicted shrinkage')
plt.grid()
plt.show()

#===============================

#===============================
'''
agar ma dade ee k dashtim 
output nadasht --> khoroji nadasht

onmoghe chi??


input boood 

label --> khoroji ndre



SUPERVISED (REGRESSION , CLASSIFICATION)


UNSUPERVISED ----> input --> XXXXOUTPUT



dataye kh ziadi dari , label nakhorde



Tomography CT scan --> 


------------>   volume  , surface area , diameetr , compactness, sphericity
defect1  ---->  1.33       2.334           34      

defect2 ---->

defect3 ---->

defect4 ---->
....

80000



khorojie peyvaste gossaste egression --> khoroji
label jnadarim--->


clustering ---> clustering --> khoshe bandi

bar asase tafavot ha va shabahat ha biad befahme

'''

#y eshpo hazf kon --> y dnadari

#load_iris()
#khodm nevehstam --->


from sklearn.datasets import make_blobs
x,y=make_blobs(n_samples=30000,centers=4,cluster_std=0.60 , random_state=0)


#print(y)
#NameError: name 'y' is not defined


#az 4 bo gol --> 30000 --> tool , arzesh has

#khoroji --> supervised, deep leanring, reinforceme

#input --> moshakahsat --> features---> unsupervised

#--> clustering ro anjam bde

#-----unsupervised ha
#--------------
#Kmeans
#DBSCAN
#hirerchechial


from sklearn.cluster import KMeans

model=KMeans(n_clusters=4) #b chnata khoshe taghsim konam?

model.fit(x)   #x,y 

y_pred=model.predict(x)


'''
Evaluation nadare


y ro dahste bashi
y_predict

y_true


- ham koni



jaee unsupervsied miad k khorji ndrim

y ndrim

y_pred --> ba chi moghayese konm??



semi-supervised -----> []

metrics --------------
SK---> misanje k har datae k tooey khosheye khodeshe chghd
gerde oon khoshe he



'''

#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================
#==================================================

'''

REINFORCEMENT LEARNING


data

modeletono --> environment



agent ---> modelet

Environemnet


state ---> snapshot az hamon environemnt lahze


Policy ---> ghanonie 

ACTION---> Decision


bar asase policy dar oon environment va state --> action


agar doros bashe --> reward (jayeze)


ag ena ---> jayeze nemdian



bar asase ooon ---> 
policy doros mikone 



state jadid 
policy taghir mide



action haye avalie --> momkene ghalaty bashan

hey bere jolo tar---> policy ghavita rmishe action



----------

S F F H H F
F F H F F H
H H F F F H
H F F F F G

S start --> Goal ( hadafete)


'''



#--------------------
#------ravesh1------> traain test
#------ravesh2 -----> gridsearchCV
#-----raveshe3-----> pipeline


#x , y
#model
#grid_param
#gridsearch(model)
#gridsearch.fit()



#ghabl az hameye ina
#x,y ---> preprocessing --> normalize , standard 

'''
1  monaseb
0

ghad (fasleey bini ta lab)  --> monasebe ya na
180      2
170      1
190      4







170 - 180 ---> 2


model --> bias -->ghad
normalzie


b ranges



0 - 1   | 0 - 1



#----> 2 ta etefagh
model dg mifhme tafavot , bias nmsihe, ignore nmikone

#--> modle ha ag dataee k bhshon bdim normalize shod , standard 
kh kh kh sarii tar amal mikonan




standardization , normalziation data yek stepe preprocessing
k kh kh kh moheme
scaling---->

model , scaler

minmaxscaler()
standardscaler()
robustscaler()

rnage haye mokhatlef

0-1
-1 1 
tamarkozesh 0 1  4 5 


data behtr represent
gridsearch max depth --> 


sklern import standardscaler
scaler=standardscaler()
scaler=minmaxscaler()


polynomial --> sotone 1 --> **2 

preprocessing haye pishrafte --> sklearn vojod drn



x_scaled , y_scaled=scaler.fit_transform(x,y)

model.fit(x,y) bejay ein

model.fit(x_scaled, y_scaled)


post procesing --> logarithmy --> pishbini 
exponential , sin





fght model ---> pipeline ( preprocessor , model , post processor)

model -->
gridsearch(model)



pipeline(model, sclaer, post process)
gridsearch(pipeline)



'''


from sklearn.datasets import fetch_california_housing
all_data=fetch_california_housing()


x=all_data.data
y=all_data.target



#---raveshe 3-------

#data import ---> data=pd.read_excel() pd.read_csv()
#data.info()  cleaning ,.....
#x, y ---> numpy array()

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler



'''


scler  , model

'''

from sklearn.tree import DecisionTreeRegressor

model=DecisionTreeRegressor()

pipe=Pipeline([  ('scaler',MinMaxScaler()) , ('model',model)   ])



#gridsearch(model)
#gridsearch.fit()



'''
myparam= { 'max_depth': [10,20,30,40,50,60],
             'criteration': ['mean_square','',....]}



'''
myparams={'model__max_depth':[2,3,4,5,6,7,8,9,10]}


from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(pipe,param_grid=myparams ,scoring='neg_mean_absolute_percentage_error',cv=10)


#gridsearch(pipe)
#gridssearch.fit()

gs.fit(x,y)

#----------
#gs --> datahato standard ---> b adesh fit mikone








#-=---------
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
pipe=Pipeline([  ('scaler',MinMaxScaler()) , ('model',model)   ])
myparams={'model__max_depth':[2,3,4,5,6,7,8,9,10]}

from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(pipe,param_grid=myparams ,scoring='neg_mean_absolute_percentage_error',cv=10)

gs.fit(x,y)




from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()
pipe=Pipeline([  ('scaler',MinMaxScaler()) , ('model',model)   ])
myparams={'model__max_depth':[2,3,4,5,6,7,8,9,10],
          'model__min_samples_split':[1,2,3,4,5,6,7],
          'scaler' : [MinMaxScaler(),StandardScaler(), RobustScaler()]}



from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(pipe,param_grid=myparams ,scoring='neg_mean_absolute_percentage_error',
                cv=5)

gs.fit(x,y)


gs.best_params_

'''

behtarin scaler maslaan --> standardscaler()
vase modelet
behtarin max depth --> 8
behtarin min_sampel -->


{'model__max_depth': 10,
 'model__min_samples_split': 4,
 'scaler': StandardScaler()}


'''

gs.best_score_

'''
-0.31915625534902003



ahan damet grm
'''

#new_x --> khdoet miomdi standardization fit.transform 

#badesh ono  middi b gs


gs.predict(new_x)




'''

FURTHER INFORMATION




gridsearchcv etefade nmikonim
best scoret ag paeen bashe
modeleto ghavi tr koni
hyparaprametr --:> rangesho bbri bala


rangesho bbri bala 840 model
1 million modelo train


done done 1 miilion takribe hyperparameter ro train koni
az ravsesh haye optimization




genetic algorithem
particle swarm optimization
gradiant descent
....... (>100 raveshe )



'''
#=======================================
#=======================================
#========================================
#========================================
#========================================


#--------RAVESHE NAHAEI----------

from sklearn.datasets import fetch_california_housing
all_data=fetch_california_housing()

x=all_data.data
y=all_data.target



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

#from sklearn.
#linearegresion | logistic regresssion
#kNN regressor | classifier
#Decision tree regressor | decision treee classifier
#Random forest regressor | classiifer
#Supportr vector machine  SVR (regression ) | SVC (classification)


#multi layer perceptron
#https://blog.faradars.org/شبکه-عصبی-چیست/
#Multi layer perceptron --> mLP
#basic tarin halaye ANN --> artificial neural network 
#shabake asabie masnooe

from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier

#1 laye ---> 100


#model=MLPRegressor(hidden_layer_sizes=(100,))
#model=MLPRegressor(hidden_layer_sizes=(10,))

#2 laye 10 , 20
#model=MLPRegressor(hidden_layer_sizes=(10,20))

#5 , 15 , 30

#model=MLPRegressor(hidden_layer_sizes=(5,15,30))


model=MLPRegressor()

pipe=Pipeline([  ('scaler',MinMaxScaler()) ,('model',model)  ])

#https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html
myparams={'model__hidden_layer_sizes':[ (10,) , (50,) , (100,) ,(10,10) ,(50,50), (100,100)   ],
          'model__activation': ['relu','tanh'],
          'model__solver':['sgd','adam'],
          'scaler':[StandardScaler(),MinMaxScaler()]}


from sklearn.model_selection import GridSearchCV

gs=GridSearchCV(pipe,param_grid=myparams ,
                scoring='neg_mean_absolute_percentage_error',
                cv=5)

gs.fit(x,y)

best_score=gs.best_score_

best_param=gs.best_params_


print(f'my best score is {best_score} with this detail :')
print(f'best hypeparamtewrs : {best_param}')


'''

2 laye


10  10





100   100



10000 neuron --> (W , Bias) 

10 000 parameter






Model haye rooze donya CHat gpt

160 B parameter



deep learning --> bahs pichide tar mishe



MLP --> pichide taresh krde ---> niz b danesh dare




sklearn --> supervised MLP

datahat --> million --> deep learning

tensorflow
pytorch

#-->model haye ANN -> artifical neural network 
bashah kar koni




ANN------------------

MLP ---> raveshe BASE --> regression, classification

CNN --> shabakeye pichesh --> computer vision 

RNN --> datahat donableye ham hastan --> translate , minevisid pishbini mikone suggest mikone kalamey badi

GAN (generative adversial network) --> image genration


Attention-based learning (transfer learning) --> MLP hast k bjaye adado -->  text midan
ketab ,-p----> mitonan yad bgiran ye vorodi bhshon ( soale oon fard nbsorat) --> bsorate text javab midn




sklearn--> MLP --> nmmizare memari ro taghir bdi , CPU run mishe

pytorch , tensorflow --> MLP (balaee memarisho dre , mdoel haye amadaro
                              ejaze mide model haro memarisho taghir) , GPU shoma run konid


'''






'''
P3 --> PROJECT3 --> 50% 





1---> ravehse (train test)
2--> ravehse ( cross validation --> gridsearchCV)
3---> raveshe3 (pipeline)



raveshe 2 , 3 --->  (nmishe estefade krd)



data ---> shoma bayad dar oon zamine ee k hastid 
dataye khdoeton ro peyda konid
mitone ba search dar website, chatbot (ai) , google scholar

dataye mortabet

Voordi , khoroji dahste

fetch_california_housing() 
natijeye search --> dar ooon zamine data vojo nadashte



data --> x , y 
y --> peyavste , gosaste 



6 model -->
Linear , KNN , Decision tree, random forest , svm, mlp 

6 ta model cross validation 6 kfold 
train konid rooye dataton
va dar neteha dar yek file yek safe ee word 
gozarehs konid natayejo


behtarini model baraye har modelo

in model ba in hyperparameter --> MAPE 4%

#MAE

in model behtarine --> prediction rasm koni ya nakonid



deadline --> 

code kamelton + safeye gozareshe modle haro
free-template

P3_firstname_lastname
ai.2024.pilehvar@gmail.com




'''





























