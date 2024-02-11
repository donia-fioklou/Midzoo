from django.db import models
from django.conf import settings
from PIL import Image

class Engine(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Propriétaire')
    engine_type_choice = (('VOITURE','Voiture'),('MOTO','Moto'))
    engine_type=models.CharField(max_length=30, choices=engine_type_choice, verbose_name='Type de moteur')
    mark=models.CharField(max_length=30, verbose_name='Marque')
    model=models.CharField(max_length=30, verbose_name='Modèle', blank=True, null=True)
    Immatriculation=models.CharField(max_length=30, verbose_name='Immatriculation')
    image=models.ImageField(upload_to='images/', verbose_name='Image', blank=True, null=True)
    
    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)