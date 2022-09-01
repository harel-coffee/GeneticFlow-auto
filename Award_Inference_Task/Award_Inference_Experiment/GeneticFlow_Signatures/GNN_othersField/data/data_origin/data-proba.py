import numpy as np
import os
import pandas as pd

import pickle
file = open('saved_model.pickle','rb')
# file = open('saved_model_5depth.pickle','rb')
model = pickle.load(file)

for root, dirs, files in os.walk("../data_origin", topdown=False):
    for name in files:
        if(name[0]=='l'):
            print(name)
            try:
                df=pd.read_csv(name,sep='\t',header=None)
            except:
                np.savetxt(name, np.array([]), fmt="%s", delimiter="	")
                continue
            edge=df[[0,1]]
            df=df.drop(columns=[0,1])
            print(df)
            result=model.predict_proba(df)[:,0]
            result=pd.DataFrame(result)
            # print(result)
            edge=pd.concat([edge,result],axis=1)
            print(edge.values.shape)
            np.savetxt(name, edge.values, fmt="%s", delimiter="	")



