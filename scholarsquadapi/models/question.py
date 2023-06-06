from django.db import models

class Question(models.Model):
    question = models.TextField()
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quizzes')