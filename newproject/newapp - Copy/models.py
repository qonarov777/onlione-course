from django.db import models
from distutils.command.upload import upload


class AboutUs(models.Model):
    title=models.CharField( max_length=50)
    text= models.TextField(max_length=500)
    image=models.ImageField(upload_to='media/about/')
    

    class Meta:
        verbose_name ='Biz haqimizda'
        verbose_name_plural='Biz haqimizda'

    def __str__(self):
        return self.title

class Homepage(models.Model):
    title=models.CharField( max_length=50)
    text= models.TextField(max_length=500)
    image=models.ImageField(upload_to='media/home/')

    class Meta:
        verbose_name ='Reklama'
        verbose_name_plural='Reklamalar'
      

    def __str__(self):
        return self.title