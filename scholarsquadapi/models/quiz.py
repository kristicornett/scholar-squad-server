from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    created_by = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='teachers')
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='students_quiz')
    description = models.CharField(max_length=350)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='quiz_questions')
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='answers')
    start_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
