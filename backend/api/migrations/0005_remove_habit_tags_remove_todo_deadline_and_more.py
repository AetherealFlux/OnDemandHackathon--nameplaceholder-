# Generated by Django 4.2.16 on 2024-11-09 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_todo_subtasks_subtodo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="habit",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="deadline",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="priority",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="tags",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
