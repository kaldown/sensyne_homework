"""sensyne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from marketplace import views


router = routers.DefaultRouter()
router.register(r'products', views.ListProductViewSet)
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('openapi', get_schema_view(
        title="Sensyne Schema",
        description="API" ,
        version="1.0.0"
    ), name='openapi-schema'),
    path('', include(router.urls)),
]
