
from django.conf import settings
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.models.CustomizeUser import CustomizeUser
from django_filters import rest_framework as filters

from api.serializers.customize_user_serializer import CustomizeUserSerializer, GetUserByEmailFilter

class Registration(ModelViewSet):
    User=CustomizeUser
    serializer_class = CustomizeUserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_active = True
        user.save()
        return user


class GetUserByEmail(generics.ListAPIView):
    queryset = CustomizeUser.objects.all()
    serializer_class = CustomizeUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GetUserByEmailFilter
   
        
    
    


        
    
    
    
    
    
