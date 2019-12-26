from django.urls import path
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from call.views.api_orders import OrdersViewSet

router = DefaultRouter()
router.include_format_suffixes = False
router.register(r'orders',OrdersViewSet,basename='orders')
urlpatterns = [
    url(r'^', include(router.urls)),
    # path('')
]