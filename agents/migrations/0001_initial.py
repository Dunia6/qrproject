# Generated by Django 4.2.7 on 2023-11-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
