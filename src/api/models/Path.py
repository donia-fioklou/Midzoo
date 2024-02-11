from django.db import models
from django.conf import settings
class Path(models.Model):
    creator=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Créateur')
    
    start_point=models.CharField(max_length=30, verbose_name='Point de départ')
    #start point with latitude and longitude 
    start_point_latitude=models.FloatField(verbose_name='Latitude du point de départ')
    start_point_longitude=models.FloatField(verbose_name='Longitude du point de départ')
    
    end_point=models.CharField(max_length=30, verbose_name='Point d\'arrivée')
    #end point with latitude and longitude 
    end_point_latitude=models.FloatField(verbose_name='Latitude du point d\'arrivée')
    end_point_longitude=models.FloatField(verbose_name='Longitude du point d\'arrivée')
    #date and time
    
    departure_date=models.DateField(verbose_name='Date')
    departure_time=models.TimeField(verbose_name='Heure')
    
    arrival_date=models.DateField(verbose_name='Date')
    arrival_time=models.TimeField(verbose_name='Heure')
    #price=models.FloatField(verbose_name='Prix')
    number_places=models.IntegerField(verbose_name='Nombre de places')
    active_path=models.BooleanField(default=True, verbose_name='Trajet actif')
    #engine=models.ForeignKey(Engine, on_delete=models.CASCADE, verbose_name='Moteur')
    #passager=models.ForeignKey(CustomerUser, on_delete=models.CASCADE, verbose_name='Passager')
    def __str__(self):
        return self.start_point + ' - ' + self.end_point