# Generated by Django 4.1.7 on 2023-02-19 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("content", models.URLField()),
                ("like", models.PositiveIntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
