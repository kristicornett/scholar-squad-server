from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Question

class QuestionView(ViewSet):

    def list(self, request):
        questions = Question.objects.all()
        serialized = QuestionSerializer(questions)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):

        question = Question.objects.get(pk=pk)
        serialized = QuestionSerializer(question)
        return Response(serialized.data, status=status.HTTP_200_OK)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'quiz')