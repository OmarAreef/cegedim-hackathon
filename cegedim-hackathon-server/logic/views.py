from django.shortcuts import render
from rest_framework import status 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
@parser_classes([JSONParser])
def results (request):
    return Response("hi")
