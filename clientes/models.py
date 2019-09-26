from django.db import models


class Cliente(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    foto = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
