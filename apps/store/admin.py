from django.contrib import admin
from .models import Store, StoreProduct, BookStore


admin.site.register(Store)
admin.site.register(StoreProduct)
admin.site.register(BookStore)

