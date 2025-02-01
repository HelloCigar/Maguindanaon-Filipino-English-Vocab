from django.db import models

# Create your models here.

class Translation(models.Model):
    english = models.CharField(max_length=255, unique=True)
    filipino = models.CharField(max_length=255, blank=True, null=True)
    maguindanaon = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.english
