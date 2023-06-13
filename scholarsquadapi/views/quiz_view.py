from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Quiz, Teacher, Student, Question, Answer
from django.contrib.auth.models import User

class QuizView(ViewSet):

    def list(self, request):
        teacher_id = request.query_params.get("teacher_id")
        if (teacher_id is not None):
            quizzes = Quiz.objects.filter(created_by=teacher_id)
        else:
            quizzes = Quiz.objects.all()
       
      
        serialized = QuizSerializer(quizzes, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):

        question = Quiz.objects.get(pk=pk)
        serialized = QuizSerializer(question)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        questions = request.data['questions']
        created_by = Teacher.objects.get(user=request.auth.user)
        quiz = Quiz.objects.create(
            title=request.data['title'],
            created_by=created_by,
            description=request.data['description'],
            start_date=request.data['start_date'],
            expire_date=request.data['expire_date']
            

        )
        for question in questions:
            newQuestion = Question.objects.create(
                question = question['question'],
                quiz = quiz
            )
            
            correctAnswer = question['correctAnswer']
            allAnswers = question['answers']
            for a in allAnswers:
               
                Answer.objects.create(
                    answer=a,
                    isCorrect = (a == correctAnswer),
                    question = newQuestion
                )

        serializer = CreateQuizSerializer(quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def update(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        quiz.title = request.data['title']
        quiz.created_by = Teacher.objects.get(pk=request.data['created_by'])
        quiz.description = request.data['description']
        quiz.start_date = request.data['start_date']
        quiz.expire_date = request.data['expire_date']
        quiz.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        quiz.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'isCorrect', 'answer')

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'question', 'answers')

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'created_by', 'description', 'start_date', 'expire_date', 'questions')

class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'created_by',
            'description',
            'start_date',
            'expire_date'
        )
        depth = 1