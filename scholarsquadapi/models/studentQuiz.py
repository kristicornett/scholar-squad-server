from django.db import models

class StudentQuiz(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quizzes')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='students')
    date_assigned = models.DateTimeField()
    date_completed = models.DateTimeField()