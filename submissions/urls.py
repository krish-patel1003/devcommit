from django.urls import path, include
from rest_framework.routers import SimpleRouter
from submissions.views import SubmissionViewSet

router = SimpleRouter()

router.register('', SubmissionViewSet)


urlpatterns = [
    path(r'', include(router.urls))
]