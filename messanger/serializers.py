from rest_framework.serializers import ModelSerializer

from messanger.models import Message


class MessagesSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ['content', 'views_count']
