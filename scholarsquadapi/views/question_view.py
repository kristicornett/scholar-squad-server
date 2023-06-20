from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Question, Answer,Quiz

class QuestionView(ViewSet):

    def list(self, request):
        questions = Question.objects.all()
        serialized = QuestionSerializer(questions, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):

        question = Question.objects.get(pk=pk)
        serialized = QuestionSerializer(question)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        """Handles PUT request for school"""
        currentQuestion = Question.objects.get(pk=pk)
        newQuestionText = request.data["question"]
        currentQuestion.question = newQuestionText

        newAnswers = request.data["answers"]
        for answer in newAnswers:
            oldAnswer = Answer.objects.get(pk=answer['id'])
            oldAnswer.answer = answer['answer']
            oldAnswer.isCorrect = answer['isCorrect']
            oldAnswer.save()
        
        currentQuestion.save()
        serializer = QuestionSerializer(currentQuestion)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        quiz = Quiz.objects.get(pk=request.data['quizId'])
        newQuestion = Question.objects.create(
            question = request.data['question'],
            quiz = quiz
        )
        
        allAnswers = request.data['answers']
        for a in allAnswers: 
            Answer.objects.create(
                answer=a['answer'],
                isCorrect = a['isCorrect'],
                question = newQuestion
            )

        serializer = QuestionSerializer(newQuestion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question', 'answers')
        depth = 1