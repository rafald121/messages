from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from messanger import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = SimpleRouter()
router.register('messages', views.MessagesViewSet)
