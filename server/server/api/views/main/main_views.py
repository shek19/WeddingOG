from rest_framework import viewsets

from .serializers import WeddingSerializer
from ...models import Wedding


class WeddingViewSet(viewsets.ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer

    def perform_create(self, serializer):
        serializer.save(planner = self.request.user)

