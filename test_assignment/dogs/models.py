from django.db import models
import uuid

# Create your models here.

SIZE_CHOICES = (
    ('Tiny','Tiny'),
    ('Small','Small'),
    ('Medium','Medium'),
    ('Large','Large'),    

)

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female')
)


class Breed(models.Model):
    uuid = models.UUIDField(primary_key = True,
                            default=uuid.uuid4(), 
                            editable=False)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    shedding_amount = models.IntegerField()
    exercise_needs = models.IntegerField()


    def __str__(self):
        return "{} - {}".format(self.name,self.size)

class Dog(models.Model):
    uuid = models.UUIDField(primary_key = True,
                            default=uuid.uuid4(), 
                            editable=False)
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=50, blank=True, null=True)
    favorite_toy = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name
