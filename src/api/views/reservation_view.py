from rest_framework.viewsets import ModelViewSet
from api.models.Reservation import Reservation
from api.serializers.reservation_serializer import ReservationSerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer