from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='teachers', blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'