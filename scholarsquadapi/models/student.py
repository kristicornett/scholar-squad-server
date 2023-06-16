from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    grade = models.IntegerField(blank=True, null=True)
    classrooms = models.ManyToManyField('Classroom', related_name='students')

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
