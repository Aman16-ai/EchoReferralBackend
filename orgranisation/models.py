from django.db import models

# Create your models here.
class Organisations(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="organisation_img")
    link = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name