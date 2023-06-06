from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ManyToManyField('School', related_name='student_schools')
    grade = models.IntegerField(blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
