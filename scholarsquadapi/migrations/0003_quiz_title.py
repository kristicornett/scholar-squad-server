# Generated by Django 4.2.1 on 2023-06-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarsquadapi', '0002_alter_teacher_schoolclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]