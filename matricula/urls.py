from rest_framework import routers
from .api import AlumnoViewSet

router = routers.DefaultRouter()
router.register('api/alumno',AlumnoViewSet,'projects')

urlpatterns = router.urls