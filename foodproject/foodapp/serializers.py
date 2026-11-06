from rest_framework import serializers
from .models import Food, Order, Payment


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    # Display Food Name
    food_name = serializers.CharField(
        source="food.food_name",
        read_only=True
    )

    # Display Food Image
    food_image = serializers.ImageField(
        source="food.image",
        read_only=True
    )

    class Meta:
        model = Order
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source="order.customer_name",
        read_only=True
    )

    food_name = serializers.CharField(
        source="order.food.food_name",
        read_only=True
    )

    mobile = serializers.CharField(
        source="order.mobile",
        read_only=True
    )

    address = serializers.CharField(
        source="order.address",
        read_only=True
    )

    quantity = serializers.IntegerField(
        source="order.quantity",
        read_only=True
    )

    class Meta:
        model = Payment
        fields = "__all__"

        read_only_fields = (
            "transaction_id",
            "payment_status",
            "payment_date",
        )