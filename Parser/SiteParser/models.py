from django.db import models

class SiteLinkModel(models.Model):
    title = models.CharField(max_length=9999)
    link = models.CharField(max_length=9999)

