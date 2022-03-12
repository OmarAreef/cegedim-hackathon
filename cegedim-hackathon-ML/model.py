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
  
  model = SVC(kernel='poly', degree=5, probability=True)
  
  df.drop_duplicates(inplace=True)
  df.dropna()
  df = df[df['age_60_and_above'].notna()]
  df = df[df['corona_result'].notna()]

  X = df[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above']]

  

  y = df.corona_result
  
  res=0

  i=0
  while i<1:
      i+=1
      X_train, X_test, y_train, y_test = train_test_split(
      X, y, test_size=0.3,stratify=y)
    

      model.fit(X_train, y_train)
      
      y_pred = model.predict(X_test.values)
     
      test_acc = precision_recall_fscore_support(y_test, y_pred)

      
  print(test_acc); 
  print(classification_report(y_test, y_pred))
  return model
  
def predictModel(X_test, model): 
  arr=np.array(X_test)
  newarr = arr.reshape(1, -1)
  return model.predict_proba(newarr)[0][1]
# regressionModel=trainModel(data)
# print(predictModel([1,1,1,1,1],regressionModel))