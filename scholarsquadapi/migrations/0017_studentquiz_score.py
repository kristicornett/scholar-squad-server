# Generated by Django 4.2.1 on 2023-06-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarsquadapi', '0016_alter_message_recipient_alter_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentquiz',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
