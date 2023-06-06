"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Student

class StudentView(ViewSet):
    def list(self, request):

        students = Student.objects.all()
        serialized = StudentSerializer(students)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serialized = StudentSerializer(student)
        return Response(serialized.data, status=status.HTTP_200_OK)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'school', 'grade')