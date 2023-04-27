from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import (
    SeedView,
    TagViewSet
)

app_name = "core"

router = DefaultRouter()
router.register(r"tags", TagViewSet, basename="tag")
router.register(r"seeds", SeedView, basename="seed")

urlpatterns = router.urls
