from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Store, StoreProduct
from .serializers import StoreSerializer, StoreProductSerializer


class StoreAPIView(APIView):
    def get(self, request, *args, **kwargs):
        stores = Store.objects.all()
        serializer = StoreSerializer(instance=stores, many=True)
        return Response(serializer.data)


class StoreProductAPIView(APIView):
    def get(self, request, store_id, *args, **kwargs):
        print(id)
        products = StoreProduct.objects.filter(store__id=store_id)
        serializer = StoreProductSerializer(instance=products, many=True)
        return Response(serializer.data)


class StoreDetailView(APIView):
    def get(self, request, store_id, *args, **kwargs):
        store = Store.objects.get(id=store_id)
        serializer = StoreSerializer(instance=store)
        return Response(serializer.data)
    
    
