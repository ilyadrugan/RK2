from rest_framework import viewsets
from rk.models import Orchestra, Musician
from .serializers import OrchestraSerializer, MusicianSerializer
class OrchestraListAPIView(viewsets.ModelViewSet):

    serializer_class = OrchestraSerializer
    queryset = Orchestra.objects.all()

class MusicianListAPIView(viewsets.ModelViewSet):

    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()