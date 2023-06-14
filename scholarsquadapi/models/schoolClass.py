from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=20)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='classrooms')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='classrooms')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value

