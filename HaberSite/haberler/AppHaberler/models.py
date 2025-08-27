from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category= models.CharField(max_length=150)
    def __str__(self):
        return self.category
 



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    haber_baslik = models.CharField(max_length=255)
    haber_link = models.URLField()
    haber_kaynak = models.CharField(max_length=100, blank=True, null=True)
    haber_tarih = models.CharField(max_length=100, blank=True, null=True)
    haber_resim = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.haber_baslik}"
