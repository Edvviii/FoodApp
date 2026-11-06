from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Q
from .models import Food, Order, Payment
from .serializers import FoodSerializer, OrderSerializer, PaymentSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import random


def home(request):
    return HttpResponse("Welcome to Food App API!")


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = Food.objects.all()
        search = self.request.query_params.get("search")

        if search:
            queryset = queryset.filter(
                Q(food_name__icontains=search) |
                Q(hotel_name__icontains=search) |
                Q(category__icontains=search)
            )

        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-ordered_date")
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all().order_by("-payment_date")

    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        transaction = "TXN" + str(random.randint(100000, 999999))

        payment = serializer.save(
            transaction_id=transaction,
            payment_status="Paid"
        )

        order = payment.order
        order.status = "Paid"
        order.save()