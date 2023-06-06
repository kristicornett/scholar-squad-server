from django.db import models

class SchoolClass(models.Model):
    name = models.CharField(max_length=20)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='school_name')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='schools_teachers')