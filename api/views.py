from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MessageSerializer
from django.http import HttpResponse
from chat.models import Message
from rest_framework.renderers import JSONRenderer


class MessageViewSet(viewsets.ModelViewSet):
    model = Message
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
