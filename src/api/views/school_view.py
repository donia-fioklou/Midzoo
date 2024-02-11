from rest_framework.viewsets import ModelViewSet
from api.models.School import School
from api.serializers.school_serializer import SchoolSerializer

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer