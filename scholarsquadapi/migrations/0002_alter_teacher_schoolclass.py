# Generated by Django 4.2.1 on 2023-06-06 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scholarsquadapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='schoolClass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='scholarsquadapi.schoolclass'),
        ),
    ]
