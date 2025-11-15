from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)


    def __str__(self):
        return self.username
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    bio = models.CharField(max_length=300, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png') 

    def __str__(self):
        return self.user.username


    
    

