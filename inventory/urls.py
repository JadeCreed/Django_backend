from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, AllocationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'allocations', AllocationViewSet)

urlpatterns = [
    path('', include(router.urls)),  # <- important
]