# Generated by Django 3.0.7 on 2021-01-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='assignment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
