from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Seed,
    Tag
)
from .serializers import (
    SeedSerializer,
    TagSerializer
)


class SeedView(ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer
    http_method_names = ["get"]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.filter(deleted=False)
    serializer_class = TagSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsAdminUser()]
        return super().get_permissions()

    def destroy(self, request, pk=None):
        self.queryset.filter(id=pk).update(deleted=True)
        return Response(status=status.HTTP_204_NO_CONTENT)
