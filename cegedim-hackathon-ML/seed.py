import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2

conn_string = 'postgresql://postgres:password@localhost:5432/cegedim'
  
db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv('data.csv')
df.drop_duplicates(inplace=True)
df.dropna()
df = df[df['age_60_and_above'].notna()]
df = df[df['corona_result'].notna()]


# X = df[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above']]

df.to_sql('train_data', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  


conn.close()