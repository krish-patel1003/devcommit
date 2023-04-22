from django.urls import path, include
from rest_framework.routers import SimpleRouter
from enrollments.views import EnrollmentViewSet

router = SimpleRouter()

router.register('hackathon_registration', EnrollmentViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]