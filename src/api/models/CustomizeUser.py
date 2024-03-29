from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class CustomizeUser(AbstractUser):
    gender_choice = (('M','Masculin'),('F','Feminin'))
    user_type_choice = (('PASSAGER','Passager'),('CONDUCTEUR','Conducteur'))
    
    gender=models.CharField(max_length=30, choices=gender_choice, verbose_name='Genre')
    adress=models.CharField(max_length=30, verbose_name='Adresse')
    phone=models.CharField(max_length=30, verbose_name='Téléphone')
    birth_date=models.DateField(null=True, verbose_name='Date de naissance')
    photo_profile=models.ImageField(upload_to='images/', verbose_name='Image de profil')
    school=models.ForeignKey('School', on_delete=models.CASCADE, verbose_name='Ecole', blank=True, null=True)
    user_type=models.CharField(max_length=30, choices=user_type_choice, verbose_name='Type d\'utilisateur')
    id_card=models.ImageField(upload_to='images/', verbose_name='Carte d\'identité', blank=True, null=True)
    username = models.CharField(max_length=50,unique=True,default='')
    
    
    IMAGE_MAX_SIZE = (800, 800)

    def resize_images(self):
        image = Image.open(self.photo_profile)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.photo_profile.path)
        image = Image.open(self.id_card)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.id_card.path)
    
    
        
        
    def __str__(self):
        return self.username
    

