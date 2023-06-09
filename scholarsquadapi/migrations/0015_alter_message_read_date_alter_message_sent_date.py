# Generated by Django 4.2.1 on 2023-06-20 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scholarsquadapi', '0014_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='read_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='sent_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
