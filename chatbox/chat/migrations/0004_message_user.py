# Generated by Django 4.2.11 on 2025-03-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.TextField(blank=True),
        ),
    ]
