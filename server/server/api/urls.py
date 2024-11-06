from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.main.main_views import BudgetItemViewSet, ChecklistDeleteView, ChecklistUpdateView, GuestDeleteView, GuestUpdateView, GuestViewSet, VendorViewSet, WeddingVendorViewSet, WeddingViewSet,ChecklistViewSet


router = DefaultRouter()
router.register(r'wedding', WeddingViewSet)
router.register(r'guest', GuestViewSet)
router.register(r'checklist',ChecklistViewSet)
router.register(r'budgetitem', BudgetItemViewSet)
router.register(r'vendor',VendorViewSet)
router.register(r'weddingvendor',WeddingVendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('guest/<int:pk>/delete/',GuestDeleteView.as_view(),name='guest-delete'),
    path('guest/<int:pk>/update/',GuestUpdateView.as_view(), name = "guest-update" ),
    path('checklist/<int:pk>/update/',ChecklistUpdateView.as_view(), name= "checklist-update"),
    path('checklist/<int:pk>/delete/',ChecklistDeleteView.as_view(), name = "checklist-update")
]