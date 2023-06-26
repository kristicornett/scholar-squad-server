from django.db import models

class StudentQuiz(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='assigned_quizzes')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='assigned_quizzes')
    date_assigned = models.DateTimeField()
    date_completed = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)