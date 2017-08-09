# Django dependencies
from django.conf.urls import url, include

# REST framework dependencies
from rest_framework import routers
# Views
from views import UserViewSet, CurrentUser

# Set up router for viewset
router = routers.DefaultRouter()
# Users viewset
router.register(r'users', UserViewSet, 'users')

# generic views urls
genericviewsurl = [
     url(r'^currentuser', CurrentUser.as_view()),
]

#Final Url pattern combines viewsets and generic views
urlpatterns = router.urls + genericviewsurl