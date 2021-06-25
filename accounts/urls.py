from rest_framework import routers
from django.urls import path, include

from .views import AuthViewSet

app_name = "accounts"

router = routers.DefaultRouter()
router.register(r'api/auth', AuthViewSet, 'auth')
urlpatterns = [
    path('', include(router.urls)),
]