from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userinfo (models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    bdate = models.DateField(("Doğum tarihi"), auto_now=False, auto_now_add=False)
    agree = models.BooleanField(("Şart ve koşul onayı"),null=True)
    photo = models.ImageField(("Foto"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    def __str__(self):
        return self.user.first_name

class Comments (models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    comment = models.TextField(("Yorumlar"), max_length=150)
    
class Twitts (models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    userinfo = models.ForeignKey(Userinfo, verbose_name=("Userinfo"), on_delete=models.CASCADE, null=True)
    twitt_header = models.TextField(("Twitt Konusu"), null=True)
    twitt = models.TextField(("Twitt yazısı"), max_length=150)
    like = models.IntegerField(("Like sayısı"))
    retweet = models.IntegerField(("RT sayısı") )
    media = models.ImageField(("Twitt Media"), upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    