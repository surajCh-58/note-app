from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    gender_choices=[('M','Male'),('F','Female'),('O','Others')]
    picture=models.ImageField(upload_to='avatar',blank=True,null=True)
    phone=models.CharField(max_length=13)
    gender=models.CharField(max_length=10,choices=gender_choices)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username