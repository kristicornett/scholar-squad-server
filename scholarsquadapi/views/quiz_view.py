from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Quiz

class QuizView(ViewSet):

    def list(self, request):
        questions = Quiz.objects.all()
        serialized = QuizSerializer(questions)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):

        question = Quiz.objects.get(pk=pk)
        serialized = QuizSerializer(question)
        return Response(serialized.data, status=status.HTTP_200_OK)


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'created_by', 'student', 'description', 'question', 'answer', 'start_date', 'expire_date')
