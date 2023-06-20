from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Classroom, School, Teacher, Student
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import action

class ClassroomView(ViewSet):
    
    def list(self, request):
        school_id = request.query_params.get("school_id")
        if (school_id is not None):
            classroom = Classroom.objects.filter(school=school_id)
        else:
            classroom = Classroom.objects.all()

        serialized = ClassroomSerializer(classroom, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
 
    def retrieve(self, request, pk=None):
        try:
            classroom = Classroom.objects.get(pk=pk)
            serializer = ClassroomSerializer(classroom)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Classroom.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def create(self, request):
        """Handles Post"""
        serializer = CreateClassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT request for school"""
        classroom = Classroom.objects.get(pk=pk)
        classroom.name = request.data['name']
        school = School.objects.get(pk=request.data['school'])
        classroom.school = school
        teacher = Teacher.objects.get(pk=request.data['teacher'])
        classroom.teacher = teacher
        classroom.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        classroom = Classroom.objects.get(pk=pk)
        classroom.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True, url_path='students')
    def add_student(self, request, pk):
        try: 
            classroom = Classroom.objects.get(pk=pk)
            studentId = request.data['studentId']
            student = Student.objects.get(pk=studentId)

            classroom.students.add(student)
            classroom.save()
            return Response(None, status=status.HTTP_200_OK)
        except Classroom.DoesNotExist:
            return Response("Classroom not found.", status=status.HTTP_404_NOT_FOUND)

        except Student.DoesNotExist:
            return Response("Student not found.", status=status.HTTP_404_NOT_FOUND)
    
    @action(methods=['get'], detail=True)
    def get_students(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
            serialized = StudentSerializer(classroom.students, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        
        except Classroom.DoesNotExist:
            return Response("Classroom not found.", status=status.HTTP_404_NOT_FOUND)

       
            
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'full_name')
        depth = 1
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'school', 'grade', 'full_name')
        depth = 1
class ClassroomSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    teacher = TeacherSerializer()
    class Meta:
        model = Classroom
        fields = ('id', 'name', 'description', 'roomNumber', 'school', 'teacher', 'students', 'quizzes')
        depth = 2

class CreateClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'school', 'teacher', 'description', 'roomNumber']
