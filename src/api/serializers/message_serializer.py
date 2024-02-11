from rest_framework.serializers import ModelSerializer
from api.models.Message import Message
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'path', 'content', 'date')
        read_only_fields = ('id', 'date')