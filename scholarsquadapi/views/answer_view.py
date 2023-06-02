from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Answer 

class AnswerView(ViewSet):

    def list(self, request):

        answers = Answer.objects.all()
        serialized = AnswerSerializer(answers, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            answer = Answer.objects.get(pk=pk)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Answer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer')