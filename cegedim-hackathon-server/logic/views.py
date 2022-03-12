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





@api_view(['POST'])
@parser_classes([JSONParser])
def results(request):
    data = request.data
    serializer = resultSerializer(data = data)
    serializer.is_valid(raise_exception = True)
    record = serializer.save()
    print(record.id)
    return Response({
        "id": record.id})

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


@api_view(['GET'])
@parser_classes([JSONParser])
def retrain(request):
    records = result_store.objects.filter(corona_result__isnull= False).values();
    result_list = querySet_to_list(records)
    data = pd.DataFrame(result_list);
    data
    return Response(resultSerializer(records , many = True).data)