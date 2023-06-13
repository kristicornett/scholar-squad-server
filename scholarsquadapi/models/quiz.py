from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    created_by = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='quizzes_by_teacher')
    description = models.CharField(max_length=350)
    start_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)
