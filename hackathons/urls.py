from django.urls import path, include
from rest_framework.routers import SimpleRouter
from hackathons.views import HackathonViewSet

router = SimpleRouter()

router.register('', HackathonViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]