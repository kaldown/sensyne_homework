from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    """
    API endpoint get Product by PK
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

    def handle_exception(self, exc):
        return Response(exc.args[0])


class ListProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint get list of Products
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
