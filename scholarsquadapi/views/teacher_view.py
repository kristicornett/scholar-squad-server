from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Teacher, Classroom, School
from django.contrib.auth.models import User
from rest_framework.decorators import action

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
        username = request.data['email']
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            username=request.data['email'],
            email=request.data['email'],
            password= request.data['password'],
            is_staff = True

        )
        teacher = Teacher.objects.create(
            user = user
        )
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
            user = User.objects.get(pk=teacher.user.id)
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.email = request.data['email']
            user.save()
            school = School.objects.get(pk=request.data['school'])
            teacher.school = school
            teacher.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
           return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

        except School.DoesNotExist:
            return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

        except Teacher.DoesNotExist:
            return Response("Teacher not found.", status=status.HTTP_404_NOT_FOUND)
        
    @action(methods=['GET'], detail=True, url_path='classrooms')
    def getClassrooms(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherClassroomSerializer(teacher.classrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'password', 'is_staff')

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'school', 'classrooms', 'full_name')
        depth = 1

class CreateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'full_name', 'user')

class TeacherClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'roomNumber', 'description', 'school', 'students']
        depth = 1
