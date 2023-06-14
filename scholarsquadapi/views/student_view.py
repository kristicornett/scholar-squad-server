"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Student

class StudentView(ViewSet):
    def list(self, request):
        school_id = request.query_params.get("school_id")
        if (school_id is not None):
            students = Student.objects.filter(school=school_id)
        else:
            students = Student.objects.all()

        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            serialized = StudentSerializer(student)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"},
                            status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Handles Post"""
        serializer = CreateStudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'school', 'grade', 'full_name')
        depth = 1

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'school', 'grade', 'full_name']