# Generated by Django 4.2.7 on 2023-11-05 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0003_agent_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='code',
        ),
    ]
