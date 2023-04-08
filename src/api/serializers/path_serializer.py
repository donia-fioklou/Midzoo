from rest_framework.serializers import ModelSerializer
from api.models.Path import Path


class PathSerializer(ModelSerializer):
    class Meta:
        model = Path
        fields = ['creator',
'start_point',
'start_point_latitude',
'start_point_longitude',
'end_point',
'end_point_latitude',
'end_point_longitude',
'departure_date',
'departure_time',
'arrival_date',
'arrival_time',
'number_places',
'active_path',]