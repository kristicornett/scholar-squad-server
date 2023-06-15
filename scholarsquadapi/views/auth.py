from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from scholarsquadapi.models import Teacher, Student, School


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Handles the authentication of user"""

    email = request.data['username']
    password = request.data['password']
    teacher_id = None
    authenticated_user = authenticate(username=email, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)

        if(authenticated_user.is_staff):
            teacher = Teacher.objects.get(user_id = authenticated_user.id)
            if(teacher is not None):
                teacher_id = teacher.id

        data = {
            'valid': True,
            'token': token.key,
            'user': {
                'isStaff': authenticated_user.is_staff,
                'id': authenticated_user.id,
                'isAdmin': authenticated_user.is_superuser,
                'teacherId': teacher_id
            }
        }
        return Response(data)
    
    else:
        data = {'valid': False}
        return Response(data)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles creation of new user for authentication
    Methods: request -- Full HTTP request object'''

    account_type = request.data.get('account_type', None)
    email = request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)


    if account_type is not None \
        and email is not None \
        and first_name is not None \
        and last_name is not None \
        and password is not None:
        
        
        if account_type == 'student':
            grade = request.data.get('grade', None)
            school = request.data.get('school', None)
            if grade is None:
                return Response(
                    {'message': 'You must provide a grade for a student'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif school is None:
                return Response(
                    {'message': 'You must provide a grade for a student'},
                    status=status.HTTP_400_BAD_REQUEST
                )


        elif account_type == 'teacher':
            school = request.data.get('school', None)
            if school is None:
                return Response(
                    {'message': 'You must provide a grade for a student'},
                    status=status.HTTP_400_BAD_REQUEST
                )
           
        else:
            return Response(
                {'message': 'Invalid account type. Valid values are \'student\' or \'teacher\''},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Create a new user by invoking the create_user helper method on Django's user model

            new_user = User.objects.create_user(
                username=request.data['email'],
                email=request.data['email'],
                password=request.data['password'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
              
            )
        
        except IntegrityError:
            return Response(
                {'message': 'An account with that email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        account = None

        if account_type == 'student':
            account = Student.objects.create(
                grade=request.data['grade'],
                user=new_user

            )
            school_name = request.data['school']
            schoolObject = School.objects.filter(name=school_name).first()
           # if schoolObject is not None:
               # account.school.set(schoolObject)
        elif account_type == 'teacher':
            new_user.is_staff = True
            new_user.save()

            account = Teacher.objects.create(user=new_user)
            school_name = request.data['school']
            schoolObject = School.objects.filter(name=school_name).first()
           # if schoolObject is not None:
              #  account.school.set(schoolObject)
        token = Token.objects.create(user=account.user)
        data = { 'token': token.key, 'staff': new_user.is_staff }
        return Response(data)
    
    return Response({'message': 'You must provide email, password, first_name, last_name, school, and account_type' }, status=status.HTTP_400_BAD_REQUEST)