# Generated by Django 4.2.3 on 2023-08-01 10:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_delete_tags"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="News",
            new_name="New",
        ),
    ]
