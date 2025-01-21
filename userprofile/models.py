from django.db import models
from django.conf import settings

# Create your models here.
class Userproflie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userprofile")
    user_avatar = models.BinaryField(blank=True)
    residence_county = models.CharField(max_length=128)
    residence_city = models.CharField(max_length=128)
    disability_id = models.CharField(max_length=128)
    front_id_img = models.BinaryField(blank=True)
    back_id_img = models.BinaryField(blank=True)

