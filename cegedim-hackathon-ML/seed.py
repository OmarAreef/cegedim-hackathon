import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2

conn_string = 'postgresql://postgres:password@localhost:5432/cegedim'
  
db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv('data.csv')
#df.drop_duplicates(inplace=True)
df.dropna()
df = df[df['age_60_and_above'].notna()]
df = df[df['corona_result'].notna()]
df = df[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above', 'gender','test_indication','corona_result']]


df=pd.get_dummies(df, prefix=['testReason'])
#X = X[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above','gender','testReason_Abroad','testReason_Other','testReason_Contact with confirmed']]

# df = df.reset_index()

df.to_sql('train_data', con=conn, if_exists='replace',
          index=False)
        
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  


conn.close()