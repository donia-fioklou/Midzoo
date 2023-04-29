from api.models.School import School
from rest_framework.serializers import ModelSerializer

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'