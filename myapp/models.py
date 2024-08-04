from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " อายุ " + str(self.age)