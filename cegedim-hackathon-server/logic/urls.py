from django.urls import path;
from . import views;

urlpatterns = [
    path('results/' , views.results),
    path('test/' , views.test),
    path('train/' , views.train),
   
    
]