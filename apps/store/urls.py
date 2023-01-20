from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.StoreAPIView.as_view(), name="stores"),
    path("<str:store_id>/", views.StoreDetailView.as_view(), name="store-detail"),
    path("<str:store_id>/get-all-products/", views.StoreProductAPIView.as_view(), name="products"),
]


