from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Teacher
from django.contrib.auth.models import User

class TeacherView(ViewSet):
    def list(self, request):
        school_id = request.query_params.get("school_id")
        if (school_id is not None):
            teachers = Teacher.objects.filter(school=school_id)
        else:
            teachers = Teacher.objects.all()

        serialized = TeacherSerializer(teachers, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        teacher = Teacher.objects.get(pk=pk)
        serialized= TeacherSerializer(teacher)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user = User.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            password= request.data['password']

        )
        serializer = UserSerializer(user=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'school', 'classroom', 'full_name')
        depth = 1

class CreateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'full_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'password')