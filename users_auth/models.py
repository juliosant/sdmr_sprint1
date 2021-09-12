from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    PROFILE_TYPE_CHOICES = [
        ("D", "Doador"),
        ("R", "Ponto de Coleta")
    ]
    code = models.CharField(max_length=11)
    email = models.EmailField(unique=True, 
            error_messages={'unique': "Já existe um usuário com este email", 'required': 'Por favor dgite um email'})
    phone = models.CharField(max_length=11)
    profile_type = models.CharField(max_length=1, choices=PROFILE_TYPE_CHOICES)
    about = models.TextField(max_length=300)
    #img_profile = models.ImageField(upload_to='img_profile', null=True, blank=True)
