from django.db import models

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=20)
    isCorrect = models.BooleanField(blank=False, null=False)