from django.db import models
class School(models.Model):
    school_name=models.CharField(max_length=30, verbose_name='Nom de l\'école')
    school_adress=models.CharField(max_length=30, verbose_name='Adresse de l\'école')
    school_phone=models.CharField(max_length=30, verbose_name='Téléphone de l\'école')
    school_email=models.EmailField(max_length=30, verbose_name='Email de l\'école')
    """school_contact_name=models.CharField(max_length=30, verbose_name='Nom du contact à l\'école')
    school_contact_phone=models.CharField(max_length=30, verbose_name='Téléphone du contact à l\'école')
    school_contact_email=models.EmailField(max_length=30, verbose_name='Email du contact à l\'école')
    school_contact_adress=models.CharField(max_length=30, verbose_name='Adresse du contact à l\'école')
    school_contact_postal_code=models.CharField(max_length=30, verbose_name='Code postal du contact à l\'école')
    school_contact_city=models.CharField(max_length=30, verbose_name='Ville du contact à l\'école')
    school_contact_country=models.CharField(max_length=30, verbose_name='Pays du contact à l\'école')
    """
    def __str__(self):
        return self.school_name
    