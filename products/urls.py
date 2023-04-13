from django.urls import path, include
from rest_framework import routers
from .views import ProductsViewSets

app_name = "products"

router = routers.SimpleRouter()
router.register("", ProductsViewSets, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
