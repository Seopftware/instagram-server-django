# Generated by Django 4.1.7 on 2023-02-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_review_feed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="content",
            field=models.CharField(max_length=150),
        ),
    ]