from django.urls import path, include
from rest_framework import routers

from .views.BranchViewSet import BranchViewSet
from .views.DealerViewSet import DealerViewSet
from .views.GenderViewSet import GenderViewSet

rest_router = routers.DefaultRouter()
rest_router.register(r'gender', GenderViewSet)
rest_router.register(r'branch', BranchViewSet)
rest_router.register(r'dealer', DealerViewSet)

urlpatterns = [
    path('', include(rest_router.urls)),
]
