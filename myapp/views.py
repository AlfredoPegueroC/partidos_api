from django.shortcuts import render
from .models import Partidos, PartidosSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("THIS API IS RUNNING")

@api_view(['GET'])
def getAlldata(request):
  lista = Partidos.objects.all()
  ser = PartidosSerializer(lista,many=True)
  return Response(ser.data)


#   @api_view(['GET'])
# def getAllPais(request):
#   list = Pais.objects.all()
#   ser = PaisSerializer(list, many=True)
#   return Response(ser.data)
