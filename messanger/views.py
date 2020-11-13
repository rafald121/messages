from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from messanger.models import Message
from messanger.serializers import MessagesSerializer


class MessagesViewSet(ModelViewSet):

    serializer_class = MessagesSerializer
    queryset = Message.objects.all()
    permission_classes = [DjangoModelPermissions, ]

    def update(self, request, *args, **kwargs):
        message = self.get_object()
        message.reset_views_count()
        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        message = self.get_object()
        message.increment_views_count()
        return super().retrieve(request, *args, **kwargs)

