from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, AllocationViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'allocations', AllocationViewSet)

urlpatterns = router.urls
