from django.db import models

# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to="images")
    date=models.DateTimeField(auto_now_add=True)
    