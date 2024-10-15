from rest_framework import routers
from .api import ProductoViewSet

router = routers.DefaultRouter()
router.register('api/inventario', ProductoViewSet, 'inventario')

urlpatterns = router.urls