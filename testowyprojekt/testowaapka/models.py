from django.db import models

# Create your models here.

class Klasa(models.Model):
    nazwa = models.CharField(max_length=3)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "Klasy"

class Uczen(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    klasa = models.ForeignKey('Klasa', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Uczniowie"