from api.models.Engine import Engine
from rest_framework.serializers import ModelSerializer


class EngineSerializer(ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'