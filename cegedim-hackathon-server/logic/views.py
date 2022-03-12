from django.shortcuts import render
from rest_framework import status 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import result_store
from .serializers import resultSerializer
from .model import trainModel, predictModel
from sqlalchemy import create_engine
import pandas as pd
from joblib import dump, load




@api_view(['POST'])
@parser_classes([JSONParser])
def results (request):
    data = request.data
    serializer = resultSerializer(data = data)
    serializer.is_valid(raise_exception = True)
    record = serializer.save()
    # df = pd.read_csv('ML/data.csv')

    # trainModel(df)
    print(record.id)
    return Response("hi")


@api_view(['POST'])
#@parser_classes([JSONParser])
def train (param):
    
# Create an engine instance

    conn_string = 'postgresql://postgres:password@localhost:5432/cegedim'
  
    db = create_engine(conn_string)

    conn = db.connect()

    # Read data from PostgreSQL database table and load into a DataFrame instance

    

    df2=pd.read_sql("SELECT * FROM public.logic_result_store ", conn)
    
    df2 = df2[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above','corona_result']]
    df3= pd.DataFrame()
    df3['fever']=df2['fever'].astype(int)
    df3['sore_throat']=df2['sore_throat'].astype(int)
    df3['shortness_of_breath']=df2['shortness_of_breath'].astype(int)
    df3['head_ache']=df2['head_ache'].astype(int)
    df3['age_60_and_above']=df2['age_60_and_above'].astype(int)
    df3['corona_result']=df2['corona_result']
    
    df3.to_sql("train_data", db, if_exists='append', index=False, chunksize=10000)
    print("gazara1")
    df= pd.read_sql("SELECT * FROM train_data ", conn)
  
    pd.set_option('display.expand_frame_repr', False)

    db.execute("DELETE FROM public.logic_result_store")
    print("gazara")
    model=trainModel(df)
    # df = pd.read_csv('ML/data.csv')
    res=predictModel([0,0,0,0,0],model)
    print(res)
    # trainModel(df)
    #dump(model, 'model.joblib') 
    return Response(res)


@api_view(['POST'])
#@parser_classes([JSONParser])
def predict (param):
    
# Create an engine instance

    
    return Response("2")
