from django.db import models
from rest_framework import serializers

# Create your models here.
class Partidos(models.Model):
  id = models.IntegerField(primary_key = True)
  Nombre = models.CharField(max_length=50, null=False)

  def __str__(self):
    return self.Nombre

class PartidosSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  Nombre = serializers.CharField(max_length=50)

  class Meta:
    model: Partidos
    fields=['__all__']