
# Create your models here.
from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='member_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"