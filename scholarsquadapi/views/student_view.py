"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scholarsquadapi.models import Student, School
from django.contrib.auth.models import User

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
        username = request.data['email']
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            username=request.data['email'],
            email=request.data['email'],
            password= request.data['password'],
            is_staff = False
        )

        school = School.objects.get(pk=request.data['school'])

        teacher = Student.objects.create(
            user = user,
            school = school
        )
        serializer = StudentSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            user = User.objects.get(pk=student.user.id)
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.email = request.data['email']
            user.save()
            school = School.objects.get(pk=request.data['school'])
            student.school = school
            student.grade = request.data.get('grade', student.grade)
            student.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

        except School.DoesNotExist:
                return Response("School not found.", status=status.HTTP_404_NOT_FOUND)

        except Student.DoesNotExist:
                return Response("Teacher not found.", status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'school', 'grade', 'full_name')
        depth = 1

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'school', 'grade', 'full_name',]