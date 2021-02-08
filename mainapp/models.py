from django.db import models


# Create your models here.

class Colors(models.Model):
    cname = models.CharField(max_length=20, null=False)
