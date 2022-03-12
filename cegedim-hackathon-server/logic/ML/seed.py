import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import psycopg2

conn_string = 'postgres://postgres:password@localhost/cegedim'
  
db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv('data.csv')

df.to_sql('logic_result_store', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  


conn.close()