from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.main.main_views import WeddingViewSet


router = DefaultRouter()
router.register(r'weddings', WeddingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]