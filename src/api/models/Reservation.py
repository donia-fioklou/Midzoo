from django.db import models

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ForeignKey('Path', on_delete=models.CASCADE, verbose_name='Trajet')
    passager = models.ForeignKey('CustomizeUser', on_delete=models.CASCADE, verbose_name='Passager')
    # is_accepted_by_driver_choice = ((ACCEPTE,'Accepté'),(REFUSE,'Refusé'))
    # is_accepted_by_driver = models.CharField(max_length=30, choices=is_accepted_by_driver_choice, verbose_name='Accepté par le conducteur')
    
    is_cancelled_by_passager=models.BooleanField(default=False, verbose_name='Annulé par le passager')
    
    
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date de réservation')
    #price = models.FloatField(verbose_name='Prix')
    def __str__(self):
        return self.path.start_point + ' - ' + self.path.end_point