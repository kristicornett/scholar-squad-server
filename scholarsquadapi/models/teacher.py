from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ManyToManyField('School', related_name='schools')
    schoolClass = models.ForeignKey('schoolClass', on_delete=models.CASCADE, related_name='classes', blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'