from django.db import models

# Create your models here.
class Image_upload(models.Model):
    dr_image = models.ImageField(upload_to="images/", blank=True)
