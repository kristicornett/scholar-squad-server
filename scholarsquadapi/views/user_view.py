from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Student, Teacher

class UserView(ViewSet):
    def list(self, request):

        teachers = Teacher.objects.all()
        serialized = TeacherSerializer(teachers)
        return Response(serialized.data, status=status.HTTP_200_OK)
    


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'school', 'schoolClass', 'full_name')


