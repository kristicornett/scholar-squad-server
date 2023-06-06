from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Teacher

class TeacherView(ViewSet):
    def list(self, request):
        teachers = Teacher.objects.all()
        serialized = TeacherSerializer(teachers, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        teacher = Teacher.objects.get(pk=pk)
        serialized= TeacherSerializer(teacher)
        return Response(serialized.data, status=status.HTTP_200_OK)
        


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'school', 'schoolClass', 'full_name')