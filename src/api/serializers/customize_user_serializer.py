from django.conf import settings
from rest_framework import serializers

from api.models import CustomizeUser
class CustomizeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUser
        fields = ['id','first_name', 'last_name','email','gender','adress','phone',
                  'birth_date','photo_profile','school_name','user_type','id_card']
