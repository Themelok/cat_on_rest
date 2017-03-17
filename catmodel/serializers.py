from rest_framework import serializers
from catmodel.models import Cat, Breed


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ("name", "age", "breed")


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
