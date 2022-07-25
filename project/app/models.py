from django.db import models

# Create your models here.

class todo(models.Model):
    text = models.CharField(max_length=300)
    Complete = models.BooleanField(default=False)


    def __str__(self):
        return self.text


