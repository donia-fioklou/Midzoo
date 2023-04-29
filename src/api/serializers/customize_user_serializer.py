from django.conf import settings
from rest_framework import serializers

from api.models import CustomizeUser
MIN_LENGTH = 8
class CustomizeUserSerializer(serializers.ModelSerializer):
    """
    password=serializers.CharField(write_only=True,min_length=MIN_LENGTH,
    error_messages={
      "min_length": f"Password must be longer than {MIN_LENGTH} characters."
    })
    password2=serializers.CharField(write_only=True,min_length=MIN_LENGTH,label='Confirm password',
    error_messages={
        "min_length": f"Password must be longer than {MIN_LENGTH} characters."
    })
    """
    class Meta:
        model = CustomizeUser
        fields = ['id','first_name', 'last_name','email','username','gender','adress','phone',
                  'birth_date','photo_profile','school','user_type','id_card','validation_step1','validation_step2','validation_step3']
    """
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data
  
    def create(self, validated_data):
        user = CustomizeUser.objects.create(
        username=validated_data["username"],
        email=validated_data["email"],
        first_name=validated_data["first_name"],
        last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user

# serializer for change password
class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomizeUser
        old_password = serializers.CharField(required=True)
        new_password = serializers.CharField(required=True)
"""