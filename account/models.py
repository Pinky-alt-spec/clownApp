from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    image = models.ImageField(default='Avatar.jpeg', upload_to='Profile_Images')

    def __str__(self):
        return f'{self.client.username}-Profile'
