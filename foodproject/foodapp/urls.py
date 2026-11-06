from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, OrderViewSet, PaymentViewSet

router = DefaultRouter()

router.register("foods", FoodViewSet)
router.register("orders", OrderViewSet)
router.register("payments", PaymentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]