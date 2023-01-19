from django.db import models
from apps.common.models import TimeStampUUIDModel

class Store(TimeStampUUIDModel):
    name = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class StoreProduct(TimeStampUUIDModel):
    store = models.ForeignKey(Store, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False)
    quantity = models.PositiveIntegerField(default=0)
    temperature = models.IntegerField(default=0)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name}"
    

class BookStore(TimeStampUUIDModel):
    store = models.ForeignKey(Store, related_name="book_store", on_delete=models.CASCADE)
    store_product = models.ForeignKey(StoreProduct, related_name="book_store_product", on_delete=models.CASCADE)
    duration = models.CharField(max_length=128, blank=False, null=False)
    quantity = models.PositiveBigIntegerField(default=0)


    def __str__(self):
        return f"{self.store.name}__{self.store_product.name}"

