from rest_framework import viewsets, permissions
from .models import Alumno
from .serializers import AlumnoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset  = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnoSerializer