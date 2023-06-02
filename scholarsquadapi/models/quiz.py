from django.db import models

class Quiz(models.Model):
    created_by = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teachers')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='students')
    description = models.CharField(max_length=350)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questions')
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='answers')
    start_date = models.DateField(blank=True)
    expire_date = models.DateField(blank=True)