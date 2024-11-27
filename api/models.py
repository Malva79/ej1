from django.db import models
# Create your models here.


class programmer(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)

    def __str__(self):
        return f"{self.fullname} - {self.language}"
