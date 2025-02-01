from django.db import models

# Create your models here.

class Translation(models.Model):
    maguindanaon = models.CharField(max_length=255, unique=True)
    filipino = models.CharField(max_length=255, blank=True, null=True)
    english = models.CharField(max_length=255, blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.maguindanaon
