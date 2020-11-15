from rest_framework.routers import SimpleRouter

from messanger import views


router = SimpleRouter()
router.register('messages', views.MessagesViewSet)
