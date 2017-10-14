# coding: utf-8

import numpy as np
from xgboost.sklearn import XGBClassifier
from sklearn.metrics import accuracy_score
import time
import pickle


data_ww=np.loadtxt('data/ww.csv',delimiter=',')
data_zz=np.loadtxt('data/zz.csv',delimiter=',')
data=np.concatenate((data_ww,data_zz))
np.random.shuffle(data)
data_train=data[45000:]
data_val1=data[:10000]
data_val2=data[10000:20000]
data_val3=data[20000:30000]
data_test=data[30000:45000]
np.save("data/data_train.npy",data_train)
np.save("data/data_val1.npy",data_val1)
np.save("data/data_val2.npy",data_val2)
np.save("data/data_val3.npy",data_val3)
np.save("data/data_test.npy",data_test)


print(data_ww.shape)


data_train=np.load("data/data_train.npy")
data_val1=np.load("data/data_val1.npy")
data_val2=np.load("data/data_val2.npy")
data_val3=np.load("data/data_val3.npy")
data_test=np.load("data/data_test.npy")
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

y_train=data_train[:,0]
x_train=data_train[:,1:]
y_val1=data_val1[:,0]
x_val1=data_val1[:,1:]
y_val2=data_val2[:,0]
x_val2=data_val2[:,1:]
y_val3=data_val3[:,0]
x_val3=data_val3[:,1:]

accuracy_val1=[]
accuracy_val2=[]
accuracy_val3=[]
accuracy_train=[]

xgb = XGBClassifier(
        learning_rate=0.05,
        n_estimators=1600,
        max_depth=8,
        min_child_weight=3,
        gamma=0.05,
        subsample=0.9,
        scale_pos_weight=1.0
        )
xgb.fit(x_train,y_train)
pickle.dump(xgb,open('./model/xgboost.pickle.dat','wb'))


xgb=pickle.load(open('./model/xgboost.pickle.dat','rb'))
y_val_pred_1=xgb.predict_proba(x_val1)
y_val_pred_2=xgb.predict_proba(x_val2)
y_val_pred_3=xgb.predict_proba(x_val3)
#accu_val1=accuracy_score(y_val1,y_val_pred_1)
#accu_val2=accuracy_score(y_val2,y_val_pred_2)
#accu_val3=accuracy_score(y_val3,y_val_pred_3)
print(accuracy_score(y_val1,xgb.predict(x_val1)))
print(accuracy_score(y_val2,xgb.predict(x_val2)))
print(accuracy_score(y_val3,xgb.predict(x_val3)))

