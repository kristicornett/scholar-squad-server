# Generated by Django 4.2.1 on 2023-06-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarsquadapi', '0007_remove_teacher_classroom_remove_teacher_school_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
        migrations.AddField(
            model_name='student',
            name='classrooms',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='scholarsquadapi.classroom'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
