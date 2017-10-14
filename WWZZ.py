# coding: utf-8

def main():

    import numpy as np
    from xgboost.sklearn import XGBClassifier
    from sklearn.metrics import accuracy_score
    import time
    import pickle

    #data_ww=np.loadtxt('data/ww.csv',delimiter=',')
    #data_zz=np.loadtxt('data/zz.csv',delimiter=',')
    #data=np.concatenate((data_ww,data_zz))
    #np.random.shuffle(data)
    #data_train=data[45000:]
    #data_val1=data[:10000]
    #data_val2=data[10000:20000]
    #data_val3=data[20000:30000]
    #data_test=data[30000:45000]
    #np.save("data/data_train.npy",data_train)
    #np.save("data/data_val1.npy",data_val1)
    #np.save("data/data_val2.npy",data_val2)
    #np.save("data/data_val3.npy",data_val3)
    #np.save("data/data_test.npy",data_test)

    data_train=np.load("data/data_train.npy")
    data_val1=np.load("data/data_val1.npy")
    data_val2=np.load("data/data_val2.npy")
    data_val3=np.load("data/data_val3.npy")
    data_test=np.load("data/data_test.npy")

    N_test = data_test.shape[0]
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print("There are: ", data_test.shape[0], " test events")
    
    y_train=data_train[:,0]
    x_train=data_train[:,1:]
    y_val1=data_val1[:,0]
    x_val1=data_val1[:,1:]
    y_val2=data_val2[:,0]
    x_val2=data_val2[:,1:]
    y_val3=data_val3[:,0]
    x_val3=data_val3[:,1:]
    x_test=data_test[:,1:]
    y_test=data_test[:,0]
    
    accuracy_val1=[]
    accuracy_val2=[]
    accuracy_val3=[]
    accuracy_train=[]
    
    xgb = XGBClassifier(
            learning_rate=0.05,
            n_estimators=500,
            max_depth=8,
            min_child_weight=1,
            gamma=0.05,
            subsample=0.9,
            scale_pos_weight=1.0
            )
    #xgb.fit(x_train,y_train)
    #pickle.dump(xgb,open('./model/xgboost.pickle.dat','wb'))
    
    xgb=pickle.load(open('./model/xgboost.pickle.dat','rb'))
    y_val_pred_1=xgb.predict_proba(x_val1)
    y_val_pred_2=xgb.predict_proba(x_val2)
    y_val_pred_3=xgb.predict_proba(x_val3)
    y_val_test  =xgb.predict_proba(x_test)
    y_val_test = y_val_test.reshape(N_test, 2)
    data_new   = np.column_stack((data_test, y_val_test))
    print("The update data shape is: ", data_new.shape)
    np.savetxt("data/Updata_test.csv", data_new, delimiter="    ", fmt="%s")

    #accu_val1=accuracy_score(y_val1,y_val_pred_1)
    #accu_val2=accuracy_score(y_val2,y_val_pred_2)
    #accu_val3=accuracy_score(y_val3,y_val_pred_3)
    #print("Accuracy is: ", accuracy_score(y_val1,xgb.predict(x_val1)))
    #print("Accuracy is: ", accuracy_score(y_val2,xgb.predict(x_val2)))
    #print("Accuracy is: ", accuracy_score(y_val3,xgb.predict(x_val3)))
    print("Accuracy is: ", accuracy_score(y_test,xgb.predict(x_test)))

main()
