from django.db import models

class order(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)