from rest_framework import routers

from .views import AuthViewSet

app_name = "accounts"

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = router.urls