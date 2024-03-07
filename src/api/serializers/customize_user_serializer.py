from django.conf import settings
from rest_framework import serializers
from django_filters import rest_framework as filters

from api.models import CustomizeUser
MIN_LENGTH = 8
class CustomizeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUser
        fields = ['id','first_name', 'last_name','email','username','password','gender','adress','phone',
                  'birth_date','photo_profile','school','user_type','id_card']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = CustomizeUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(CustomizeUserSerializer, self).update(instance, validated_data)

        
class GetUserByEmailFilter(filters.FilterSet):
    class Meta:
        model = CustomizeUser
        fields = ['email']