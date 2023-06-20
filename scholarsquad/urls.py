"""
URL configuration for scholarsquad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from scholarsquadapi.views import register_user, login_user
from rest_framework import routers
from scholarsquadapi.views import SchoolView, AnswerView, QuestionView, QuizView, ClassroomView, StudentView, TeacherView, UserView, getAllSchools, ScholarAI
from django.contrib.auth.models import User

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'schools', SchoolView, 'school')
router.register(r'teachers', TeacherView, 'teacher')
router.register(r'students', StudentView, 'student')
router.register(r'quizzes', QuizView, 'quizzes')
router.register(r'answers', AnswerView, 'answer')
router.register(r'classes', ClassroomView, 'class')
router.register(r'quiz_generate', ScholarAI, 'ai' )
router.register(r'questions', QuestionView, 'question')
router.register(r'users', UserView, 'user')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('registerschool', getAllSchools),
    

]
