from django.db import models

# Create your models here.
class CityModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class SchoolModel(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(CityModel, related_name='schools', on_delete=models.CASCADE )
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class StudentModel(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return self.firt_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name