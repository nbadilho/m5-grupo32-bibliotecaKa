# Generated by Django 4.2 on 2023-05-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="days_to_borrow",
            field=models.IntegerField(default=14),
        ),
    ]
