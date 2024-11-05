from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.main.main_views import BudgetItemViewSet, GuestViewSet, VendorViewSet, WeddingVendorViewSet, WeddingViewSet,ChecklistViewSet


router = DefaultRouter()
router.register(r'wedding', WeddingViewSet)
router.register(r'guest', GuestViewSet)
router.register(r'checklist',ChecklistViewSet)
router.register(r'budgetitem', BudgetItemViewSet)
router.register(r'vendor',VendorViewSet)
router.register(r'weddingvendor',WeddingVendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]