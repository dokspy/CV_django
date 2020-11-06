from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('cvofficial', views.cvOfficial, name='cvofficial'),
    path('engcv', views.engcv, name='engCV'),
    path('UACVOfficial', views.UA_CV_Official, name='UA_CV_Official'),
    path('data', views.data, name='data'),
]
