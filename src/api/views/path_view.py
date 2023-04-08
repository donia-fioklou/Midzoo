from rest_framework.viewsets import ModelViewSet
from api.models.Path import Path
from api.serializers.path_serializer import PathSerializer

class PathViewSet(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer