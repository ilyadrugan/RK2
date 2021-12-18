from rest_framework import serializers
from rk.models import Orchestra, Musician

class OrchestraSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Orchestra
        fields =[
            'id', 'name'
        ]

class MusicianSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    orchestra_id = serializers.IntegerField()

    class Meta:
        model = Musician
        fields =[
            'id', 'name','age', 'orchestra_id'
        ]