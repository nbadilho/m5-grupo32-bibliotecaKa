# Generated by Django 4.2 on 2023-05-04 12:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserFollowing",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="books.book"
                    ),
                ),
            ],
        ),
    ]