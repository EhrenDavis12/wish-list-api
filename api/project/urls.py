from django.urls import include, path
from rest_framework import routers
from .views import (ItemViewSet, ItemLinkViewSet)
from rest_framework import renderers



router = routers.DefaultRouter()
# router.trailing_slash = "/?"

router.register(r'item', ItemViewSet,
                basename='Item')
router.register(r'item_link', ItemLinkViewSet,
                basename='Itemlink')

urlpatterns = [
    path('', include(router.urls)),
]