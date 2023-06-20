from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Message
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.decorators import action

class MessageView(ViewSet):

    def list(self, request):
        messages = Message.objects.filter(recipient = request.auth.user)

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        message = Message.objects.get(pk=pk, recipient = request.auth.user)
        serialized= MessageSerializer(message)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    @action(methods=['PUT'], detail=True, url_path='mark-read')
    def mark_read(self, request, pk):
        message = Message.objects.get(pk=pk, recipient = request.auth.user)
        message.read_date = timezone.now()
        message.save()
        serialized= MessageSerializer(message)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = CreateMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        message = Message.objects.get(pk=pk)
        message.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        

class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for messages"""
    class Meta:
        model = Message
        fields = ('id', 'recipient', 'sender', 'subject', 'body', 'sent_date', 'read_date')
        depth = 1

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'recipient', 'sender', 'subject', 'body', 'sent_date', 'read_date']


