from django.shortcuts import render
from rest_framework import status 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import result_store
from .serializers import resultSerializer
from .ML.model import trainModel, predictModel





@api_view(['POST'])
@parser_classes([JSONParser])
def results (request):
    data = request.data
    serializer = resultSerializer(data = data)
    serializer.is_valid(raise_exception = True)
    record = serializer.save()
    print(record.id)
    return Response("hi")
