from django.db import models
from django.conf import settings
class Message(models.Model):
    
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Expéditeur')
    #receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Destinataire', related_name='receiver')
    path = models.ForeignKey('Path', on_delete=models.CASCADE, verbose_name='Trajet')
    content = models.TextField(verbose_name='Contenu')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date d\'envoi')
    def __str__(self):
        return self.sender + ' - ' + self.receiver