from django.shortcuts import render
from rest_framework import status 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import result_store
from .serializers import resultSerializer
# from .ML.model import trainModel, predictModel
# from .ML import *
import pandas as pd

from .model import trainModel, predictModel
from sqlalchemy import create_engine
from  joblib import dump , load

# model = load('model.joblib')


@api_view(['POST'])
@parser_classes([JSONParser])
def results(request):
    data = request.data
    serializer = resultSerializer(data = data)
    serializer.is_valid(raise_exception = True)
    record = serializer.save()
    param=data
    print (param)
    query=[param["fever"],param["sore_throat"],param["shortness_of_breath"],param["head_ache"],param["age_60_and_above"],param["gender"],param["testReason_Abroad"],
    param["testReason_Other"],param["testReason_Contact_with_confirmed"]]
   
    res=2
    model = load('model.joblib')
    res=predictModel(query,model)
    print(res)

    return Response({
        "id": record.id,
        "prediction": res})

@api_view(['POST'])
@parser_classes([JSONParser])
def test(request):
    data = request.data
    try: 
        record = result_store.objects.filter(id = data['id']).first()
    except result_store.DoesNotExist: 
        return Response("this does not exist", status=status.HTTP_400_BAD_REQUEST)
    
    record.corona_result = data['result']
    record.save()
    
    return Response(resultSerializer(record).data)

def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]

@api_view(['POST'])
#@parser_classes([JSONParser])
def train (request):
    
# Create an engine instance

    conn_string = 'postgresql://postgres:password@localhost:5432/cegedim'
    db = create_engine(conn_string)
    conn = db.connect()

    


    records = result_store.objects.filter(corona_result__isnull= False).values();
    result_list = querySet_to_list(records)
    if(result_list == []):
        return Response("model will not update",  status=status.HTTP_400_BAD_REQUEST)
    df2 = pd.DataFrame(result_list);
    
    df2 = df2[['fever', 'sore_throat','shortness_of_breath','head_ache','age_60_and_above','gender','testReason_Abroad','testReason_Other','testReason_Contact_with_confirmed','corona_result']]

    df3= pd.DataFrame()
    df3['fever']=df2['fever'].astype(int)
    df3['sore_throat']=df2['sore_throat'].astype(int)
    df3['shortness_of_breath']=df2['shortness_of_breath'].astype(int)
    df3['head_ache']=df2['head_ache'].astype(int)
    df3['age_60_and_above']=df2['age_60_and_above'].astype(int)
    df3['gender']=df2['gender'].astype(int)
    df3['testReason_Abroad']=df2['testReason_Abroad'].astype(int)
    df3['testReason_Other']=df2['testReason_Other'].astype(int)
    df3['testReason_Contact_with_confirmed']=df2['testReason_Contact_with_confirmed'].astype(int)
    df3['corona_result']=df2['corona_result']
    
    df3.to_sql("train_data", db, if_exists='append', index=False, chunksize=10000)

    df= pd.read_sql("SELECT * FROM train_data ", conn)

    pd.set_option('display.expand_frame_repr', False)

    db.execute("DELETE FROM public.logic_result_store where corona_result is not null")
    
    model=trainModel(df)


    # df = pd.read_csv('ML/data.csv')
    
    # trainModel(df)
    dump(model, 'model.joblib') 
    # model = load('model.joblib')
    return Response("model trained successfully",  status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([JSONParser])
def predict (req):  
# Create an engine instance
    param=req.data
    print (param)
    query=[param["fever"],param["sore_throat"],param["shortness_of_breath"],param["head_ache"],param["age_60_and_above"],param["gender"],param["testReason_Abroad"],
    param["testReason_Other"],param["testReason_Contact_with_confirmed"]]
   
    res=2
    model = load('model.joblib')
    res=predictModel(query,model)
    print(res)

    return Response(res)
