from rest_framework.viewsets import ModelViewSet
from api.models.Engine import Engine
from api.serializers.engine_serializer import EngineSerializer

class EngineViewSet(ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    