# Generated by Django 4.2.9 on 2024-01-24 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_point_table_alter_prize_table_alter_role_table_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="point",
            old_name="assignee",
            new_name="student",
        ),
    ]
