from rest_framework import viewsets
from catmodel.models import Cat, Breed
from catmodel.serializers import CatSerializer, BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
