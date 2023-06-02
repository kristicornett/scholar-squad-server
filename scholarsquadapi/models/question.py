from django.db import models

class Question(models.Model):
    correct_answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='correct answer')
    question = models.TextField()
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quizzes')