# Generated by Django 5.1 on 2024-08-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(default=False, max_length=254)),
                ('subject', models.TextField(max_length=25)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]
