
"""

In the name of GOd
Created on Wed May 14 16:36:51 2025

@author: apm


-----L18-----
-----> ai ---> ML (70%)

ML --> supervised / unsupervised / reinforcmeent learning / deep learning

DATA----> supervised/unsupervide , deep
DATA In environemnt --> RL

DATA --> kh bozorg (milllion,) --> deep learning

--> supervised / unsupervised

data --> format --> input / output --> supervised
outptu (label) ---> unsupervised


output --> continious --> supervised regression
output---> gosaste --> supervised classification



supervised -->
1-Linear 2-KNN 3-decision tree (dt) 4-random forest (rf) 
5-support vector mahcien (SVM)
6-multi lkayer perceptron (mLP)

ham regressor / classifier




#--------
data --> import -->pandas
cleaning
pandas --> x , y --> numpy array ( x ye soton reshape(-1,1))
train_test_split --> train / test
model = [6 ta mdoedle ba regressor ya clasfier]
model.fit(training dasta)

y_pred=model.predict(x test)
moghayese mikoni ba y_test / y_pred

Regression --> MAE / MAPE 
Classidicaion --> Accuracy % 

#---------
test score
train score





-----L19----------

model = [6 ta mdoedle ba regressor ya clasfier]

model = linear hichi nminvisi Linearregressor() logisticregressor()

ama baghie mdoel ah yeseri parmaeter daran k vaghty msiazi  bayad speicfic begi agah chi mikhay


hyperparameter --> parameter haee hastan k dakheel trianing yad grfte nmishan
ma bayad ghabl az training(fit) moshakhasesh konim
tasire be sezaee roye yadgirie model drn
complexiity / genralization 

momkene --> complex / geenrali biare paeen
momkene --> geenral / sade bashe 



test score // train score

test_scor e--> khob bashe yani modelet az nzre complex , geenral okeye

bad boood--->

train_score --> ag kam bood --> yad nmigire  underfitting--> sade as -> complex tar --> hypeparametrasho 
 
train_score--> ziad bood --> kh dg dare overfitting --> kamtar koni



hey brm hyperparmsaeter taghir bdm hey bbinm kodom behtare ??
test scoramo bbinm

yek darke koli niaze --> reference , search internet, ketab 

ghazie tahlil nis --> try error





yek mesale kamel --> darmorede gol ha bood 

load_iris() --> ine
breast_cancer() -->
too ahr zmaine ee


30 ta azmayesh akrdid --> print yes / no
defect dakhele x-ray tomography --> Keyhole / porosity gas entrapped porosity / lack of fusion 0 1 2


outpute shoam --> gosaste bashe -_> ahdafe shoma daste bandi
supervsied classification --> da rjalsey eghabl goftim
daghighan rahi k gfotim --> regression ham hamone


rahe in dota yeki --> model / accuracy 


regression --> bznm ama harchi migm
nbaraye classification ham sedgh mkone



#--------
jalsae chikar mikhaym koni?
ye data darim --> outptu continious --> seuprvised regression
ink hamon mese clasifictaion jaalse ghabl



ma dg nmikhaym dasti dasti hypeparmaeter entkehab konim

k=10 hey run konim score
k=100
k=1000
bad bgim kodm khobe?
yekam pishrafte trsh konim


hameye in chizae --> classificationham yeksane



"""



'''
description

3d printing --> fdilament --> damae --> zob mishe
mesle yek khamir dandond (dagh) roo ham roham
print mikone
(fek kon ba yek kajmri dandon mikhay mokaab besazi)

chape afzoodani
additive manufacturing --> 3d printign polymer / metal (LPBF , EBM ,....)

IP3DP ---> raveshe jadid tari --> halal / zede halal ham ezaf emishe
faz haee gharar migire ---> vizhegie print ro kh behtar mikone
biomaterials kh kh dastemon ro bazmikone


ma settingi k hasto nmidonim chie

azmayeshgah --> darsadde halla emotefavet bznid
damaro taghir bdid
soratesho taghir bddid
zamani k bayd anjam bdm taghri


--> process parameters hast k daste shomas


taghirmidid --> oon chizi k pritn krdi ham taghir mikone

to ahr masale e yek vzihegi -_> paramete quality --> kh khobn bashe / kare man awli
mechancial , thermal proeprty , ......

dimentional mechanical property --> shrinkage

bad az print --> cheghad taghire shekl mide khodesho


shrinkage --> bala --> oonchizi print mishe, kh tafavot ijad mikone
unifrom . 



ma hadafemon ine k chizi k print mikonim kamtarin shrinkage ro dashte bashe

setting --> hey mirid azmayeshgah --> 3dprinting -> temp , sorat , . , chegdhr halal
inaro taghir midi karo anjam printet mikone --> shrinkage ye adadi

yek rabe te ee inja dare ba in process parameter


proces parmaetr --> tasiri mziren roye --> shrinkage

man donbale paen tarin shrinkage 


5 parmaet 
0-100
0-100
0-100
0-100
0-100

10**10 bar bayad pritn konm
2 saat

2 * 10 **10 saat tool mikshe 

hameye parmaetra --> shrinkage , -->  kmatarin kodome
hazine / vaghte 


nahayt 70 , 80 ta migire


process parmaetr --> shrinkage

agar befahmid

tamam ernage ro ---> [box] --> shrinkage ro pishbini mikrd

va mirftm middim kodom kamtare
10**10 anjam midad too arze 1 dieghe






---data-----
too range haye mtoefavet print kridfm
va avse har nemone -> shrinkage hesab krdim


azmayehsgahi --> chizhaye ezafe dare, chizhaye dg ham


75 ta nemone --> 75 ta sampel print shode

fargehshon chie?


ghelzate Ethanol , ab , DMF

ghelzate kolie 

speed , temp , extrusion multiplier


---> dast ema bode --> afrad taghir mdiadan smapel print

process parametrs



quality parameters ---> hesab mikonim (pritn anjamshe, azmayesh)
linear mass flow rate
shrinkage
printability


shrinkage ro bbinim --> quality parameter



'''

#-------step0-------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path='/Users/apm/Desktop/Data.xlsx'
#raw_data=pd.read_excel(path)



import pandas as pd
import numpy as np

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






#berim vase mL

#bayad bri vase cleanrn


#----step0 - cleaning ------
#negah koni datat kame
#ama ziade , 

raw_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 74 entries, 0 to 73
Data columns (total 11 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Rows                   74 non-null     object 
 1   nonsolvent-ethanol     74 non-null     int64  
 2   nonsolvent-water       74 non-null     int64  
 3   non-solvent- DMF       74 non-null     int64  
 4   Concentration          74 non-null     int64  
 5   Speed                  74 non-null     int64  
 6   Temp                   74 non-null     int64  
 7   Extrusion multiplier   74 non-null     float64
 8   linear mass flow rate  74 non-null     float64
 9   printability           74 non-null     float64
 10  Shrinkage              74 non-null     float64
dtypes: float64(4), int64(6), object(1)
memory usage: 6.5+ KB


age non-null ---> dropna  / fillna 
ag drtype --> .astype(sotono doros)



'''


raw_data.columns

'''Index(['Rows', 'nonsolvent-ethanol', 'nonsolvent-water ', 'non-solvent- DMF',
       'Concentration ', 'Speed', 'Temp', 'Extrusion multiplier',
       'linear mass flow rate', 'printability', 'Shrinkage'],
      dtype='object')
    '''
    
    
raw_data.drop(columns=['Rows'],inplace=True)

#raw_data.drop(index=0,inplace=True)
#raw_data.reset_indexes(inplace=True, drop=True)


#raw_data['temp'].astype(float)



#awlio va okeye


raw_data.hist()
plt.show()



#box plot
#rasm koni inja k khob tahlilehs koni
#k gahbelsh bbini datahat chijorian

#correlationm 

correelation=raw_data.corr()


#pearson correlation for linear correlation
#+1 / -1 ---> intensity 
#+ 1 ---> harchi nazdik b 1 ya -1 bashe
#yani chapie rooye rastie asar dre
#byen on dot aasar

'''

process parmaetr has effect on quality parameter

'''


#step 0.1.--> x , y 

#x--> process parmaeters
#y--> qualirty parametr--> shrinkaeg



raw_data.columns
'''
Index(['nonsolvent-ethanol', 'nonsolvent-water ', 'non-solvent- DMF',
       'Concentration ', 'Speed', 'Temp', 'Extrusion multiplier',
       'linear mass flow rate', 'printability', 'Shrinkage'],
      dtype='object')

'''



x=np.array(raw_data[['nonsolvent-ethanol','nonsolvent-water ', 'non-solvent- DMF',
       'Concentration ', 'Speed', 'Temp', 'Extrusion multiplier']])


y=np.array(raw_data['Shrinkage'])

#y=np.array(raw_data['printability'])


#vroodi --> x
#khrooji --> y

#az delet dat assoton hasho ekshidam brion
#tabdil b x , y 

#numpy array --> mohasebat


#-----step1--------

from sklearn.model_selection import train_test_split

#74 ta hast
#ye ghesmati --> bendazam biron --> test --> unseen data , bew evaluation model 

#15 -->  endakhtam biron
#59,60 data--> train --> ino drm mdoelo rooye in train midam
#15 taro pishbini mikonam --> y_pred
#y-true (azmayehs kardm)

#y_pred - y_true --> test score



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)

#6 model --> regressor/ classifier


#shrinkage --> regression --> adade continious 

#1.3 #4.2 #4.54590854834908
#regression

from sklearn.tree import DecisionTreeRegressor

#hyparparameteramo entekhab konm
model=DecisionTreeRegressor(max_depth=3)


model.fit(x_train,y_train)


y_pred=model.predict(x_test)

y_true=y_test

from sklearn.metrics import mean_absolute_percentage_error as mape


test_score=mape(y_true,y_pred)


print('our final model with max depth of 5 has MAPE TEST SCORE OF: ', test_score*100)

'''
our final model with max depth of 5 has MAPE TEST SCORE OF: 
    4.916385705917151 %
    
    
15 ta ro k nadide --> 


yeja 70% 80%

train-score --> taghri bdi hyperparameter


max depth 3 --> 4.650401880674783
max depth 4 --> 4.595834925017958
max depth 5 --> 4.916385705917151 %
max depth 7 --> 5.616299315738871

max depth 10 -->5.468907025489437 %
max depth 20 --> 5.468907025489437


'''



#dasti taghir bdi hyperparwmeterto , automate


#------inja regreso r, clasifier ------
#automate ---> automate hypeparameter tuning ---------

#hypeparameter optimization
#behine sazi --> ffara parametr haye mdoelamo 


#my_params
#model_params
#model_hjyperparameetrs
#dictionary
#my_params={'max_depth' :  [2,3,4,5,6,7,8,9,10]]}



#-----------------------------------------------------




#min_samples_split

#----sjhoro----

#data import
#data clean
#data -> x , y
#x , y -> np . array

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=42)


from sklearn.tree import DecisionTreeRegressor

my_params={'max_depth' :  np.arange(2,30)}



score_list={}


best_score=0

best_max_depth=None

from sklearn.metrics import mean_absolute_percentage_error as mape

for hypeparameters in my_params.keys():
    
    for number in my_params[hypeparameters]:
        
        model=DecisionTreeRegressor(max_depth=number)
        
        model.fit(x_train,y_train)
        
        y_pred=model.predict(x_test)
        y_true=y_test
        
        
        test_score=mape(y_true,y_pred)
        
        score_list[f'max_depth : {number}'] = test_score*100
        
        
        print(f'for max_depth = {number} out test score is {test_score * 100}')

        
        if best_score<test_score:
            best_score=test_score
            
            best_max_depth=number



print(f'Best max_depth is {best_max_depth} and best score with this is {best_score}')




'''
for max_depth = 2 out test score is 4.580140506705569
for max_depth = 3 out test score is 4.650401880674783
for max_depth = 4 out test score is 4.595834925017958
for max_depth = 5 out test score is 4.916385705917151
for max_depth = 6 out test score is 5.508508852953426
for max_depth = 7 out test score is 5.616299315738872
for max_depth = 8 out test score is 5.533457290039703
for max_depth = 9 out test score is 5.45964776623018
for max_depth = 10 out test score is 5.468907025489437
for max_depth = 11 out test score is 5.468907025489438
for max_depth = 12 out test score is 5.468907025489437
for max_depth = 13 out test score is 5.468907025489437
for max_depth = 14 out test score is 5.468907025489437
for max_depth = 15 out test score is 5.468907025489437
for max_depth = 16 out test score is 5.468907025489437
for max_depth = 17 out test score is 5.468907025489437
for max_depth = 18 out test score is 5.468907025489437
for max_depth = 19 out test score is 5.468907025489438
for max_depth = 20 out test score is 5.468907025489438
for max_depth = 21 out test score is 5.468907025489438
for max_depth = 22 out test score is 5.468907025489438
for max_depth = 23 out test score is 5.468907025489438
for max_depth = 24 out test score is 5.468907025489438
for max_depth = 25 out test score is 5.468907025489437
for max_depth = 26 out test score is 5.468907025489437
for max_depth = 27 out test score is 5.468907025489437
for max_depth = 28 out test score is 5.468907025489437
for max_depth = 29 out test score is 5.468907025489438

'''



#Best max_depth is 7 and best score with this is 0.05616299315738872

#------********--------
#------ Gridsearch ------

#---data import
#--clean
#--> x, y
#-->numpy array
#x , y darid

#niaz nist k b train_test_split tabdil konid
#khdoe gridsearch in karo mikone

'''

gridsearch --> class rooye class model sklearn

model --> gridsearch , parametr


train data / test data


paramters =[max dpeth 1 , 2,3,4,5,6,7,]

done done model(max_depth ) .fir(train)
.predict(test)

hey inkaor mikone
vba behtrino

'''

from sklearn.model_selection import GridSearchCV

from sklearn.tree import DecisionTreeRegressor

model=DecisionTreeRegressor() #bdone hich hyeprpameter
#default -->

#model ro midm b gridsearch 
#param_grid 

#griddy --> done done mire hyeparparmetra

#toye dictionary besazid


#myparams={'max_depth': [2,3,4,5,6,7,8,9,10]}

#kafie searhc bzni bbini 
myparams={ 'max_depth' : np.arange(2,50),
         'min_samples_split' : [2,3,4,5,6,7,8,9,10],
         'criterion' : ['squared_error', 'friedman_mse',
                        'absolute_error', 'poisson']}



#https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

#improt skelarn.m,etrics

#MAPE?
#MAE?
#tooye scoring




gs=GridSearchCV(model,param_grid=myparams,
                scoring='neg_mean_absolute_percentage_error',
                cv=2)


#b chna gehsmat ? --> train / test tabdil kon


#gs (too delehs modele)
#Model , --> gs

gs.fit(x,y)

#tamam shod


#gs --> chanta chize k kghobe shoma bdonid


zarf_cv=gs.cv_results_


gs.best_score_
#-0.10962429492913561



gs.best_params_

'''
{'criterion': 'absolute_error', 
 'max_depth': 14, 
 'min_samples_split': 6}


'''


#predict --> prodcuytion


y_pred=gs.predict()




#==================================================
#cross validation -->
#train test datato --> 80% train , 20% test


# 1 2 3 4 5 

#adadi k mdie kazebe



#cross validation --->

#5 ta laptobn
#har laptobet
# yedonaro test grfti
#hasr laptob --> score darsad khata

#darsad khataey miangien hamashon --> kazebv nis

#hame ye datahat yekabram k shdoe --> test data set gharar grftn

#cross validation > train test split motabar tare

#70 ta data 

#10 tasho test , 60 train


#fold


#->7 fold taghdimesh mikonm


#10   10    10   10   10  10  10


#score---> miangine hamashon mishe


#test scoree

#cross valkidated test score

#7fold cross valdiation test score >>>>  test score


#grdisearchCV
#grdisearch cross validatoipn
#( cv --> foldesh kone)

#20% ---> chanta fold kon


#yek mdoele dg , in karo brt ana


#----step0------
#x, y --


#from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import StandardScaler

#MinMaxScaler.fit(x,y)
#StandardScaler.fit_transform(x,y)








from sklearn.model_selection import GridSearchCV

from sklearn.ensemble import RandomForestRegressor

model=RandomForestRegressor()

myparams={'n_estimators':[10,20,50,100],
          'max_depth':np.arange(2,20)
          }

gs=GridSearchCV(model,param_grid=myparams,
                scoring='neg_mean_absolute_percentage_error',
                cv=7)


gs.fit(x,y)


zarf=gs.cv_results_


gs.best_score_
#-0.051015523477315576

gs.best_params_
# {'max_depth': 10, 'n_estimators': 10}




#gs.predict()




#74 --

#10 taro adad migire

# 0.135 test split



#mAPE --> neg_mean_absolute_percentage_error
#MAE---> neg_mean_absolute_error

#clasification
#accuracy


#74 tas 

#7 ta fold --> 

#10 10 10 10 10 10 10

'''
10 taye kahar --> test
60 taye avalo train 

ba kole hypeparametre k ddm (10,20,30,40,..) 

3% --> n estiator10
5 % --> n estiamtor 20



--------
10 taye vasat--> test 
60 

...
.



#_-----


#7 ta fold

koel dataye man yekabram k shode test shodan

bartaye har hyperparmeetri k man drm miangiensho zde


n estimator 20 --> 7 fold test score = 3 %
n estimator --->
...
haperparmeetr ham haminakreo krde



pas ag in bege
best_params---> hatman hamie




'''







'''

regressor

hamin datahaye khdomeono -->(jalase ghabl classification , ino)

gridsearch 6 fold bezanid -> model haye mokhtalef
dataton
x,y 

model
myparams()
gs(model, cv=)
gs.fit()


natiajro migid


model dcisiotn tre max depth 5 -200 taghir ddm
behtrijn result max depth 18 --> 3% khata awlie

random forest n estimatros --> 5- 100
bhtrin result n estimator 50 --> 2 %

behtarine mdoel haro baham moghayese mikonid








Tamrin
breast_cancer --> dataase3et 

train _test split 



model haro --> gridsearchCV


classification 

#-------
regression vaghe ie ham midm




https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing






'''

from sklearn.datasets import fetch_california_housing


all_data=fetch_california_housing()


all_data.DESCR


x=all_data.data

y=all_data.target

#numpy --> tahvil
#cleaning ,......

#esm ndre columns

# 8 ta vorodi darid
#ydone khoroji


len(x)

#20640

#20 hezar khone ro rftn etelaatesho dar ovordn

'''

jadvakle excell drim
2000 radi dre


-----x---------                                       ---y-----
4 otagh, 2 bed , 6 , adade joghrafias , 20 sal sakhte  gheymatesh



20 000 khoen hame moshakahsato nvshtn ba gheymatesh okeye


mdoel --> fit roo data

badan too california ye khoen ag frd 

5 otagh ,2 ta takht , felan jaye california , 10 sal skaht
ba deghate kh kh bala -> gheymat



x --> y --> dat,op 20 000 --> supervised


y --> price --> 4,000  4.345 -->peyvaste
supervised regression



mnodel--> random forest (n estimator , max_depth)
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html



svr --> (kernel ,C )
https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html





gridsearchcv

cv --> foldesho --> 7

mean absolute percentage ERROR



kodom model , ba kodm hyperparameter chand darsad dghgigh pishbini mikone





ai.2024.pilehvar@gmail.com

befrestid khate vaaleton ham eshtebah bod






'''



all_data.feature_names

'''
['MedInc',
 'HouseAge',
 'AveRooms',
 'AveBedrms',
 'Population',
 'AveOccup',
 'Latitude',
 'Longitude']

'''



all_data.target_names
#'MedHouseVal']










'''

Further information


yeseria migan --> agah bazam train / test
bezoor modeleto baraye test dataset (dide nashode bashe)
hypeparametro tune mikoni fght baraye oon test dataset

train / test / validation


gs (hyperparmeetr ) --> fit --> train / score--> test

validation (evaluation) --> fit(train+test) , score --> validation





joda az hamin ham
train / test / validation --> nested cross validation begir
7 fold X 8 fold


https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html

https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html



#-----standardization --> standard ham mikonim 

standardization , polynominal , post processing, pre procesing --> pip line

model train (gs) charta 


pipline -->
https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html



'''



'''
unsupervsied --> kmeans, dbscan 

reinforcement learning --> tozihatesh , code zanisho 


(supervised)
MLP -> multi layer perceptron ---> 
sar aghazi bar deep learnign hast --> tozihe dseep learning


GITHUB -> chei , chijori estefade konim
POROZHE POROZHEYE JALASETE AKAHREMON HAS 
github bargozari bshe


'''























