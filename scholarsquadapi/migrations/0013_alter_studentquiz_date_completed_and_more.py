# Generated by Django 4.2.1 on 2023-06-19 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarsquadapi', '0012_classroom_description_classroom_roomnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentquiz',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentquiz',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_quizzes', to='scholarsquadapi.quiz'),
        ),
        migrations.AlterField(
            model_name='studentquiz',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_quizzes', to='scholarsquadapi.student'),
        ),
    ]
