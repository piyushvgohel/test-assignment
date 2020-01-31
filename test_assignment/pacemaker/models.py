import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Pacemaker(models.Model):
    uuid = models.UUIDField(primary_key = True,
                            default=uuid.uuid4(), 
                            editable=False)
    name = models.CharField(max_length=100)
    model_number = models.TextField()
    dimensions_description = models.TextField()

    def __str__(self):
        return self.name