import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVR
from sklearn.linear_model import BayesianRidge
from sklearn import preprocessing, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error, accuracy_score, balanced_accuracy_score, classification_report, precision_score,average_precision_score,precision_recall_fscore_support, r2_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
# data = pd.read_csv('data.csv')
def trainModel(df):
  print("start")
  model = LogisticRegression()
  
  #df.drop_duplicates(inplace=True)
  df.dropna()
  df = df[df['age_60_and_above'].notna()]
  df = df[df['corona_result'].notna()]

  X = df[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above']]

  
  print("startttt")
  y = df.corona_result
  



  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.3,stratify=y)


  model.fit(X_train, y_train)
      
     

      

  return model
  
def predictModel(X_test, model): 
  arr=np.array(X_test)
  newarr = arr.reshape(1, -1)
  return model.predict_proba(newarr)[0][1]
# regressionModel=trainModel(data)
# print(predictModel([1,1,1,1,1],regressionModel))