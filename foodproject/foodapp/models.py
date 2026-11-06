from django.db import models


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    hotel_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='foods/',
        blank=True,
        null=True
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food_name

    class Meta:
        ordering = ['food_name']


class Order(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Preparing", "Preparing"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    customer_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    address = models.TextField()

    quantity = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.food.food_name}"

class Payment(models.Model):

    PAYMENT_METHODS = [
        ("UPI", "UPI"),
        ("Credit Card", "Credit Card"),
        ("Debit Card", "Debit Card"),
        ("Cash On Delivery", "Cash On Delivery"),
    ]

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Paid", "Paid"),
        ("Failed", "Failed"),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHODS
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.order.customer_name} - {self.payment_status}"