
from django.conf import settings
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models.CustomizeUser import CustomizeUser
from django_filters import rest_framework as filters

from api.serializers.customize_user_serializer import CustomizeUserSerializer, GetUserByEmailFilter

class Registration(ModelViewSet):
    queryset = CustomizeUser.objects.all()
    serializer_class = CustomizeUserSerializer
    



class GetUserByEmail(generics.ListAPIView):
    queryset = CustomizeUser.objects.all()
    serializer_class = CustomizeUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GetUserByEmailFilter
   
        
    
    


        
    
    
    
    
    