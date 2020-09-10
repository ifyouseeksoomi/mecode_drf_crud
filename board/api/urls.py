from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board.api.views import BoardViewSet

router = DefaultRouter()
router.register(r'board', BoardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
