from django.db import models
from django.contrib.auth.models  import User

# Create your models here.
class recepie(models.Model):
    user=models.ForeignKey( User ,on_delete=models.CASCADE, null=True,blank=True)
    recepie_name= models.CharField(max_length=100)
    recepie_desc=models.TextField()
    recepie_imp=models.ImageField(upload_to="recepie")

