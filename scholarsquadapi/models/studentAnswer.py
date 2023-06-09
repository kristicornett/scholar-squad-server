from django.db import models

class StudentAnswer(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='studentQuiz')
    student_quiz = models.ForeignKey('StudentQuiz', on_delete=models.CASCADE, related_name='student_answer')
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)