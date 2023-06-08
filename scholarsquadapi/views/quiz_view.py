from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Quiz, Teacher, Student, Question, Answer

class QuizView(ViewSet):

    def list(self, request):
        questions = Quiz.objects.all()
        teacher = Teacher.objects.get(user=request.auth.user)
        test_giver = request.query_params.get('_user', None)

        if test_giver is not None:
            questions = questions.filter(teacher_id=teacher.id)
        serialized = QuizSerializer(questions)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):

        question = Quiz.objects.get(pk=pk)
        serialized = QuizSerializer(question)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        created_by = Teacher.objects.get(user=request.auth.user)
        serializer = CreateQuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=created_by)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        quiz.title = request.data['title']
        quiz.created_by = Teacher.objects.get(pk=request.data['created_by'])
        quiz.student = Student.objects.get(pk=request.data['student'])
        quiz.description = request.data['description']
        quiz.question = Question.objects.get(pk=request.data['question'])
        quiz.answer = Answer.objects.get(pk=request.data['answer'])
        quiz.start_date = request.data['start_date']
        quiz.expire_date = request.data['expire_date']
        quiz.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        quiz.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'created_by', 'student', 'description', 'question', 'answer', 'start_date', 'expire_date')

class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'created_by',
            'student',
            'description',
            'question',
            'answer',
            'start_date',
            'expire_date'
        )
        depth = 1