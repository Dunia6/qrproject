# Generated by Django 4.2.7 on 2023-11-03 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_alter_agent_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='agents/'),
        ),
    ]
