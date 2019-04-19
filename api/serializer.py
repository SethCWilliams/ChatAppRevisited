
from rest_framework.serializers import ModelSerializer

from chat.models import Message


# this is the template that gets returned in JSON
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'text', 'date')
        depth = 1
# depth will generate nested..the depth get different PK
# this knows how to go from queryset to json and then back----two way street