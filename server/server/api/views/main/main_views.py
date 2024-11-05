from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import WeddingSerializer,GuestSerializer,ChecklistSerializer,BudgetItemSerializer,VendorSerializer,WeddingVendorSerializer
from ...models import Wedding,Guest,Checklist,BudgetItem,Vendor,WeddingVendor


class WeddingViewSet(viewsets.ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer

    def perform_create(self, serializer):
        serializer.save(planner = self.request.user)

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)

class ChecklistViewSet(viewsets.ModelViewSet):
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)

class BudgetItemViewSet(viewsets.ModelViewSet):
    queryset = BudgetItem.objects.all()
    serializer_class = BudgetItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

class WeddingVendorViewSet(viewsets.ModelViewSet):
    queryset = WeddingVendor.objects.all()
    serializer_class = WeddingVendorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        wedding_id = self.request.data.get('wedding')
        wedding = Wedding.objects.get(id=wedding_id)
        serializer.save(wedding=wedding)