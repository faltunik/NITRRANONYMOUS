from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image

# Create your models here.

BRANCH_CHOICES = [
    ("ARCH", "ARCH"),
    ("BME", "BME"),
    ("BIOTECH", "BIOTECH"),
    ("CHEM", "CHEM"),
    ("CIVIL", "CIVIL"),
    ("CSE", "CSE"),
    ("ECE", "ECE"),
    ("EE", "EE"),
    ("IT", "IT"),
    ("MECH", "MECH"),
    ("META", "META"),
    ("MINING", "MINING"),
    ]

class CustomUser(AbstractUser):
    email = models.EmailField(unique= True)
    branch = models.CharField(
        max_length = 20,
        choices = BRANCH_CHOICES,
        default = 'ARCH',
        unique= False
        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
  image= models.ImageField(default= 'default.jpg', upload_to= 'profilepics/%Y/%m/%d')  # upload_to= 'profilepics/%Y/%m/%d' 
  bio = models.TextField(max_length=500, blank=True)

  def __str__(self):
    return f'{self.user.username} Profile'

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    img= Image.open(self.image.path)
    #img.name = self.user.username + '%Y/%m/%d'
    if img.height > 300 or img.width > 300 :
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)

