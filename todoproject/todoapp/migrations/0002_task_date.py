# Generated by Django 4.2.2 on 2023-06-29 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-03-22'),
            preserve_default=False,
        ),
    ]
