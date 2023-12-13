from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import NewConnectorsdvsdvdbrViewSet

router = DefaultRouter()
router.register(
    "newconnectorsdvsdvdbr",
    NewConnectorsdvsdvdbrViewSet,
    basename="newconnectorsdvsdvdbr",
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
