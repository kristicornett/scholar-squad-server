from django.db import models

class StudentQuiz(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='quiz')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='completed_quizzes')
    date_assigned = models.DateTimeField()
    date_completed = models.DateTimeField()