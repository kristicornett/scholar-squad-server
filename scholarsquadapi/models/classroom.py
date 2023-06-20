from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    roomNumber = models.CharField(max_length=10)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='classrooms')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='classrooms', blank=True, null=True)


